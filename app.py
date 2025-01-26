import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI

# Securely handle API key using Streamlit secrets

# Initialize LLM with Gemini model
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp", api_key="AIzaSyDlGuiJOqQePVsQEu5gWiftb74RDGvcq-c")

# Streamlit UI
st.title("Multilingual Translator Chat")

# Initialize conversation history in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input for translation
Userquery = st.chat_input("Enter text to translate...")

if Userquery:
    # Add user message to conversation
    st.session_state.messages.append({"role": "user", "content": Userquery})
    with st.chat_message("user"):
        st.markdown(Userquery)

    # Create prompt for translation
    prompt = f"""
    Act as a professional translator. Convert the user-provided query into **100+ languages** based on ISO 639-1 language codes or specified regions.  

**Rules:**  
1. Prioritize **business-relevant languages** (e.g., for global supply chains: Mandarin, Spanish, Arabic, etc.).  
2. Format translations in a **Markdown table** with columns: **Language**, **Code**, **Translation**.  
3. For underrepresented languages (e.g., Swahili, Bengali), note dialect preferences if unspecified.  
4. Preserve the original tone (formal/technical/casual).  

**User Query:**  
"{Userquery}"  

**Example Output Template:**  
```markdown  
| Language (Code)       | Translation                   |  
|-----------------------|-------------------------------|  
| Urdu (ur)             | [اردو میں ترجمہ]              |  
| French (fr)           | [Traduction en français]      |  
| German (de)           | [Deutsche Übersetzung]        |  
| ...                   | ...                           |  
    """

    # Invoke the model to get the response
    response = llm.invoke(prompt)
    bot_reply = response.content

    # Add bot message to conversation
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
    with st.chat_message("assistant"):
        st.markdown(bot_reply)
