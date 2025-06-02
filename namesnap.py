import streamlit as st

st.set_page_config(page_title="NameSnap", layout="centered")

st.title("🔤 NameSnap")
st.caption("Snap fast brand names + SEO descriptions in seconds.")

st.markdown("---")

# User input
keyword = st.text_input("Enter a product keyword or niche:")

if keyword:
    st.markdown("### 💡 Brand Name Suggestions:")
    st.success(f"{keyword.capitalize()}Spark")
    st.success(f"Snap{keyword.capitalize()}")
    st.success(f"{keyword.capitalize()}Nest")
    
    st.markdown("### 📝 SEO Product Description:")
    st.info(f"{keyword.capitalize()} is the ultimate solution for anyone looking to boost their brand online. Perfect for entrepreneurs, creators, and marketers.")
