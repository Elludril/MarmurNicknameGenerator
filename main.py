import streamlit as st
import requests

# Access the Llama 3 API key from Streamlit secrets
llama_api_key = st.secrets["LLAMA_API_KEY"]

st.title('Marmur Nickname Generator')

theme = st.text_input('Wpisz temat dla nicków')

def generate_nicknames_llama(theme):
    headers = {
        'Authorization': f'Bearer {llama_api_key}',
        'Content-Type': 'application/json'
    }
    payload = {
        "model": "llama-3-model",  # Replace with actual model name if different
        "messages": [
            {"role": "user", "content": f"Generate creative nicknames for the following users based on the theme: {theme}. Here are the users:\n- Ada\n- Adam\n- Ala\n- Asia\n- Daria\n- Ewa\n- Efa\n- Fifi\n- Gromek\n- Inez\n- Kewin\n- Krzysiu\n- Kuba\n- Bogóh\n- Koper\n- Maciuś\n- Sikor\n- Manuela\n- Marta\n- Martyna\n- Tysia\n- Fapu\n- Nasio\n- Nat\n- Natalka\n- Nina\n- Daniel\n- Paweł\n- Piotr\n- Przemek\n- Rafał\n- Tomek\n- Wojtas"}
        ]
    }
    response = requests.post("https://api.llama3.com/v1/chat/completions", headers=headers, json=payload)
    return response.json()

if st.button('OGIYŃ 🔥'):
    if theme:
        try:
            # Use Llama 3 API to generate nicknames
            response = generate_nicknames_llama(theme)
            # Extract message content
            nicknames = response['choices'][0]['message']['content'].strip()
            st.write(nicknames)
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.error('Wpisz temat!')