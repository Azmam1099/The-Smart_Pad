import streamlit as st

# -------------------- PAGE CONFIG --------------------
st.set_page_config(
    page_title="The Smart Pad",
    page_icon="🛍️",
    layout="wide"
)

# -------------------- PRODUCT DATA --------------------
PRODUCTS = [
    {
        "title": "COB Keychain Light",
        "description": "A super bright, rechargeable mini-light that fits on your keychain.",
        "image_url": "https://placehold.co/600x600/eeeeee/333333?text=COB+Keychain",
        "affiliate_link": "https://www.amazon.com/your-link-here"
    },
    {
        "title": "Smart Air Purifier",
        "description": "A Wi-Fi enabled air purifier you can control with your phone.",
        "image_url": "https://placehold.co/600x600/eeeeee/333333?text=Air+Purifier",
        "affiliate_link": "https://www.amazon.com/your-link-here"
    },
    {
        "title": "Portable Blender",
        "description": "Make smoothies anywhere. Rechargeable and easy to clean.",
        "image_url": "https://placehold.co/600x600/eeeeee/333333?text=Portable+Blender",
        "affiliate_link": "https://www.amazon.com/your-link-here"
    },
    {
        "title": "Wireless Earbuds",
        "description": "Noise-cancelling earbuds with a 30-hour battery life.",
        "image_url": "https://placehold.co/600x600/eeeeee/333333?text=Earbuds",
        "affiliate_link": "https://www.amazon.com/your-link-here"
    },
    {
        "title": "Sunrise Alarm Clock",
        "description": "Wake up naturally with a simulated sunrise light.",
        "image_url": "https://placehold.co/600x600/eeeeee/333333?text=Sunrise+Clock",
        "affiliate_link": "https://www.amazon.com/your-link-here"
    },
    {
        "title": "Magnetic Phone Mount",
        "description": "A strong, sleek magnetic mount for your car dashboard.",
        "image_url": "https://placehold.co/600x600/eeeeee/333333?text=Phone+Mount",
        "affiliate_link": "https://www.amazon.com/your-link-here"
    },
]

# -------------------- CUSTOM CSS (Beebom-Style) --------------------
st.markdown("""
<style>

body {
    background-color: #ffffff;
}

/* Page container spacing */
.block-container {
    padding-top: 1.5rem;
    padding-left: 2rem;
    padding-right: 2rem;
}

/* Product Card */
.product-card {
    background: white;
    border-radius: 14px;
    padding: 12px;
    border: 1px solid #f0f0f0;
    box-shadow: 0 2px 10px rgba(0,0,0,0.04);
    transition: 0.18s ease-in-out;
}

.product-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 6px 20px rgba(0,0,0,0.08);
}

/* Titles */
.product-title {
    font-size: 1.15rem;
    font-weight: 600;
    margin-top: 10px;
    color: #1a1a1a;
}

.product-desc {
    font-size: 0.92rem;
    color: #555;
    height: 45px;
    overflow: hidden;
    margin-bottom: 12px;
}

/* Buttons */
.stLinkButton > button {
    width: 100%;
    border-radius: 10px;
    padding: 0.55rem;
    font-size: 0.95rem;
    font-weight: 600;
    border: 1px solid #e0e0e0;
}

</style>
""", unsafe_allow_html=True)

# -------------------- HEADER --------------------
st.image(
    # This is the corrected "RAW" link
    "https://raw.githubusercontent.com/Azmam1099/The-Smart_Pad/8ffea45bad2d08b33d15163d9e6bbf9b11ba833e/White%20Black%20Cute%20Minimalist%20and%20Elegant%20Toys%20Review%20Banner.png",
    width=True # Set a fixed width to make it smaller
)

#st.caption("As an affiliate, I may earn a commission from qualifying purchases.")
st.markdown("---")

# -------------------- PRODUCT GRID (Beebom Style) --------------------
cols = st.columns(3)

for index, product in enumerate(PRODUCTS):
    with cols[index % 3]:
        st.markdown('<div class="product-card">', unsafe_allow_html=True)

        st.image(product["image_url"], use_container_width=True)

        st.markdown(f'<div class="product-title">{product["title"]}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="product-desc">{product["description"]}</div>', unsafe_allow_html=True)

        st.link_button(
            "Buy Now",
            product["affiliate_link"],
            use_container_width=True
        )

        st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")
st.caption("© 2025 The Smart Pad")
