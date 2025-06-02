import streamlit as st
from openai import OpenAI

# Set up OpenAI client using secret key
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Streamlit UI
st.set_page_config(page_title="NameSnap", page_icon="✨")
st.title("✨ NameSnap")
st.caption("Smart AI-powered product names & SEO descriptions")

# User input
keyword = st.text_input("Enter a product niche or keyword:")

if st.button("Generate") and keyword:
    with st.spinner("Generating product names and descriptions..."):
        # Construct the prompt for OpenAI
        prompt = (
            f"Generate 3 unique, catchy product names for the niche: '{keyword}'. "
            f"Also generate an SEO-optimized product description (2–3 sentences) for each name. "
            f"The tone should be clear, persuasive, and modern."
        )

        # Call OpenAI API using the latest SDK
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a branding expert who writes creative names and persuasive SEO product descriptions."},
                {"role": "user", "content": prompt}
            ]
        )

        # Extract and display the result
        result = response.choices[0].message.content
        st.markdown("---")
        st.markdown("### 🧠 Suggestions")
        st.write(result)
