import streamlit as st
import openai

# Access the OpenAI API key from Streamlit secrets
openai.api_key = st.secrets["OPENAI_API_KEY"]

st.title('Marmur Nickname Generator')

theme = st.text_input('Wpisz temat dla nicków')

if st.button('OGIYŃ 🔥'):
    if theme:
        # Use OpenAI to generate nicknames
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": f"Split the answer on three separate answers. Generate creative nicknames for the following users based on the theme: {theme}. Here are the users:\n- Ada\n- Adam\n- Ala\n- Asia\n- Daria\n- Ewa\n- Efa\n- Fifi\n- Gromek\n- Inez\n- Kewin\n- Krzysiu\n- Kuba\n- Bogóh\n- Koper\n- Maciuś\n- Sikor\n- Manuela\n- Marta\n- Martyna\n- Tysia\n- Fapu\n- Nasio\n- Nat\n- Natalka\n- Nina\n- Daniel\n- Paweł\n- Piotr\n- Przemek\n- Rafał\n- Tomek\n- Wojtas"}
            ]
        )
        # Correctly access the message content
        nicknames = response.choices[0].message['content'].strip()
        st.write(nicknames)
    else:
        st.error('Wpisz temat!')