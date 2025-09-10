import streamlit as st
from deep_translator import GoogleTranslator

# Streamlit App Config
st.set_page_config(page_title="Multilingual Translator", layout="centered")
st.title("🌍 Multilingual Translator (No API Key)")

# Languages we want to support
custom_languages = {
    "Urdu": "ur",
    "Hindi": "hi",
    "German": "de",
    "French": "fr",
    "Chinese (Simplified)": "zh-CN",
    "English": "en"
}

# Sidebar language selection
source_lang = st.sidebar.selectbox("Select source language", list(custom_languages.keys()), index=list(custom_languages.keys()).index("English"))
target_lang = st.sidebar.selectbox("Select target language", list(custom_languages.keys()), index=list(custom_languages.keys()).index("Urdu"))

# Text input
text = st.text_area("Enter text to translate:", "")

if st.button("Translate"):
    if text.strip():
        try:
            translated = GoogleTranslator(
                source=custom_languages[source_lang],
                target=custom_languages[target_lang]
            ).translate(text)
            st.success(translated)
        except Exception as e:
            st.error(f"⚠️ Error: {e}")
    else:
        st.warning("⚠️ Please enter some text to translate.")

# Footer
st.markdown("---")
st.caption("Supports English, Urdu, Hindi, German, French, and Chinese. Powered by [deep-translator](https://pypi.org/project/deep-translator/)")
