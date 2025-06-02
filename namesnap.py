import streamlit as st
import openai

# Use secret key stored in Streamlit
openai.api_key = st.secrets["OPENAI_API_KEY"]

# --- Streamlit App Layout ---
st.set_page_config(page_title="NameSnap", layout="centered")
st.title("🧠 NameSnap")
st.caption("AI-powered brand name & description generator")

keyword = st.text_input("Enter a product keyword or niche (e.g. beauty, fitness, pets):")

if st.button("Generate"):
    if keyword.strip() == "":
        st.warning("Please enter a keyword.")
    else:
        with st.spinner("Thinking..."):
            prompt = f"Generate 3 creative, brandable product names and one short product description for a business in the '{keyword}' niche. Make them catchy and market-ready."

            try:
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are a creative branding assistant."},
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.8,
                    max_tokens=300
                )
                output = response['choices'][0]['message']['content']
                st.success("Done!")
                st.write(output)
            except Exception as e:
                st.error(f"Something went wrong: {e}")

