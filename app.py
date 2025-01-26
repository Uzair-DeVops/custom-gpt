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
    You have to work as a translator. Your task is to convert the given user query into five languages:

    1. **Urdu**  
    2. **French**  
    3. **German**  
    4. **Chinese**  
    5. **Japanese**  

    **User Query:** {Userquery}

    You should provide the response in Markdown format only.

    Do NOT include the following statement in your response:  
    **"Okay, I will translate 'how are you' into the five languages you requested. Here are the translations in Markdown format."**
    """

    # Invoke the model to get the response
    response = llm.invoke(prompt)
    bot_reply = response.content

    # Add bot message to conversation
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
    with st.chat_message("assistant"):
        st.markdown(bot_reply)
