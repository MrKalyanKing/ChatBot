import streamlit as st
import google.generativeai as genai


key="AIzaSyAUypWVg79VQ5BXtUAmtuPygYLfMyL2QKo"

# configure

genai.configure(api_key=key)


st.title("Welcome to Kalyan Chat App")


# Initialize session state for chat history
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []




user_input=st.text_area("Enter yout question")





# create model 

model=genai.GenerativeModel("gemini-2.0-flash")


# Submit button
if st.button("Send"):
    if user_input:
        # Append user message
        st.session_state["chat_history"].append({"role": "user", "text": user_input})

        # Get response from Gemini
        response = model.generate_content(user_input)

        # Append AI reply
        st.session_state["chat_history"].append({"role": "assistant", "text": response.text})


# Display chat history
for chat in st.session_state["chat_history"]:
    if chat["role"] == "user":
        st.chat_message("user").markdown(chat["text"])
    else:
        st.chat_message("assistant").markdown(chat["text"])
