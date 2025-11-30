import streamlit as st
import openai

openai.api_key = st.secrets["OPENAI_API_KEY"]

st.set_page_config(page_title="Tete AI 💖", page_icon="💖")

st.title("💖 Tete AI 💖")
st.markdown("**Hi Sweetheart, chii chanetsa?** ❤️")

if "messages" not in st.session_state:
    st.session_state.messages = []

prompt = st.text_input("Nyora nyaya yako:")
if st.button("💬 Tete Dziva") and prompt:
    with st.spinner("Tete inodanoziva..."):
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Uri Tete, tete yemadzimai vese muZimbabwe. Taura SHONA CHETE yeHarare. Start: 'Hi Sweetheart, chii chanetsa?❤️'"},
                {"role": "user", "content": prompt}
            ],
            max_tokens=250
        )
        reply = response.choices[0].message.content
        st.session_state.messages.append({"user": prompt, "tete": reply})

for msg in st.session_state.messages:
    st.write(f"**You:** {msg['user']}")
    st.write(f"**Tete:** {msg['tete']}")

with st.sidebar:
    st.header("🚨 Zvinhu Zvekuchengetedza")
    st.markdown("- **Musasa**: *117#")
    st.markdown("- **ZLHR**: Queer safe spaces")
