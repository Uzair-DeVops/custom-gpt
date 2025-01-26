from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp", api_key="AIzaSyDlGuiJOqQePVsQEu5gWiftb74RDGvcq-c") 
st.title("Translator")

Userquery = st.text_input("write which you want to translate ")

prompt =f"""
You have to work as a translator. Your task is to convert the given user query into five languages:

1. **Urdu**  
2. **French**  
3. **German**  
4. **Chinese**  
5. **Japanese**  

**User Query:** {Userquery}

You should provide the response in Markdown format only.  

you should not say the following line:  
**"Okay, I will translate 'how are you' into the five languages you requested. Here are the translations in Markdown format."**
"""



if Userquery:
    response = llm.invoke(prompt)
    st.write(response.content)