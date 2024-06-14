import streamlit as st
import google.generativeai as ggi

# Access the Gemini API key from Streamlit secrets
gemini_api_key = st.secrets["GEMINI_API_KEY"]
ggi.configure(api_key=gemini_api_key)

model = ggi.GenerativeModel("gemini-pro")
chat = model.start_chat()

def generate_nicknames(theme):
    question = f"Generate creative nicknames for the following users based on the theme: {theme}. Here are the users:\n- Ada\n- Adam\n- Ala\n- Asia\n- Daria\n- Ewa\n- Efa\n- Fifi\n- Gromek\n- Inez\n- Kewin\n- Krzysiu\n- Kuba\n- Bogóh\n- Koper\n- Maciuś\n- Sikor\n- Manuela\n- Marta\n- Martyna\n- Tysia\n- Fapu\n- Nasio\n- Nat\n- Natalka\n- Nina\n- Daniel\n- Paweł\n- Piotr\n- Przemek\n- Rafał\n- Tomek\n- Wojtas"
    response = chat.send_message(question,stream=True)
    return response

st.title('Marmur Nickname Generator')

theme = st.text_input('Wpisz temat dla nicków')
btn = st.button('OGIYŃ 🔥')

if btn and theme:
    result = generate_nicknames(theme)
    st.subheader("Response : ")
    for word in result:
        st.text(word.text)