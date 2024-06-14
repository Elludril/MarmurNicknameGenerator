import streamlit as st
from openai import OpenAI

# Access the OpenAI API key from Streamlit secrets
client = OpenAI(
    api_key=st.secrets["OPENAI_API_KEY"],
    base_url="https://api.aimlapi.com"
)

st.title('Marmur Nickname Generator')
theme = st.text_input('Wpisz temat dla nicków')
if st.button('OGIYŃ 🔥'):
    if theme:
        # Use OpenAI to generate nicknames
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": f"Please assign the name based on the theme for the following users. If it's possible, use character names. No duplicates are allowed. Here is the theme: {theme}. Here are the users:\n- Ada\n- Adam\n- Ala\n- Asia\n- Daria\n- Ewa\n- Efa\n- Fifi\n- Gromek\n- Inez\n- Kewin\n- Krzysiu\n- Kuba\n- Bogóh\n- Koper\n- Maciuś\n- Sikor\n- Manuela\n- Marta\n- Martyna\n- Tysia\n- Fapu\n- Nasio\n- Nat\n- Natalka\n- Nina\n- Daniel\n- Paweł\n- Piotr\n- Przemek\n- Rafał\n- Tomek\n- Wojtas\nPlease write the answer in Polish. Skip original message before translation."}
            ],
        )
        # Correctly access the message content
        nicknames = response.choices[0].message.content
        st.write(nicknames)
    else:
        st.error('Wpisz temat!')