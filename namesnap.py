import streamlit as st
import random

st.set_page_config(page_title="NameSnap", layout="centered")

st.title("🔤 NameSnap")
st.caption("Snap fast, fresh brand names + SEO-style product descriptions.")

st.markdown("---")

keyword = st.text_input("Enter a product keyword or niche:")

brand_starters = ["Snap", "Spark", "Go", "Nova", "Peak", "Core", "Glow", "Next"]
brand_endings = ["Lab", "Nest", "Works", "Co", "Wave", "Vibe", "Boost", "Zone"]

def generate_names(kw):
    kw_cap = kw.capitalize()
    return [
        f"{random.choice(brand_starters)}{kw_cap}",
        f"{kw_cap}{random.choice(brand_endings)}",
        f"{random.choice(brand_starters)}{random.choice(brand_endings)}"
    ]

def generate_description(kw):
    templates = [
        f"{kw.capitalize()} is changing the game — perfect for creators, entrepreneurs, and anyone looking to grow online.",
        f"Looking for an edge in the {kw} space? This product delivers clarity, style, and impact.",
        f"Whether you're just starting or scaling, {kw.capitalize()} gives your brand the professional feel it deserves.",
        f"The perfect name for your {kw} brand — stand out with confidence and style.",
    ]
    return random.choice(templates)

if keyword:
    st.markdown("### 💡 Brand Name Suggestions:")
    for name in generate_names(keyword):
        st.success(name)

    st.markdown("### 📝 SEO Product Description:")
    st.info(generate_description(keyword))

