import streamlit as st

st.set_page_config(
    page_title="The Smart Pad", 
    page_icon="🛍️",
    layout="wide" 
)

# --- PRODUCT DATA ---
PRODUCTS = [
    {
        "title": "COB Keychain Light",
        "description": "A super bright, rechargeable mini-light that fits on your keychain.",
        "image_url": "https://placehold.co/400x400/eeeeee/333333?text=Product+Image", # Replace with your image URL
        "affiliate_link": "https://www.amazon.com/your-link-here" # Replace with your affiliate link
    },
    {
        "title": "Smart Air Purifier",
        "description": "A Wi-Fi enabled air purifier that you can control with your phone.",
        "image_url": "https://placehold.co/400x400/eeeeee/333333?text=Product+Image", # Replace with your image URL
        "affiliate_link": "https://www.amazon.com/your-link-here" # Replace with your affiliate link
    },
    {
        "title": "Portable Blender",
        "description": "Make smoothies on the go. USB-rechargeable and easy to clean.",
        "image_url": "https://placehold.co/400x400/eeeeee/333333?text=Product+Image", # Replace with your image URL
        "affiliate_link": "https://www.amazon.com/your-link-here" # Replace with your affiliate link
    },
    {
        "title": "Wireless Earbuds",
        "description": "Noise-cancelling earbuds with a 30-hour battery life charging case.",
        "image_url": "https://placehold.co/400x400/eeeeee/333333?text=Product+Image", # Replace with your image URL
        "affiliate_link": "https://www.amazon.com/your-link-here" # Replace with your affiliate link
    },
    {
        "title": "Sunrise Alarm Clock",
        "description": "Wake up naturally with a light that simulates the sunrise.",
        "image_url": "https://placehold.co/400x400/eeeeee/333333?text=Product+Image", # Replace with your image URL
        "affiliate_link": "https://www.amazon.com/your-link-here" # Replace with your affiliate link
    },
    {
        "title": "Magnetic Phone Mount",
        "description": "A sleek and strong magnetic mount for your car dashboard.",
        "image_url": "https://placehold.co/400x400/eeeeee/333333?text=Product+Image", # Replace with your image URL
        "affiliate_link": "https://www.amazon.com/your-link-here" # Replace with your affiliate link
    }
]


# --- HEADER ---
logo_col, banner_col = st.columns([1, 5]) 

with logo_col:
    st.image(
        
        "https://raw.githubusercontent.com/Azmam1099/The-Smart_Pad/8ffea45bad2d08b33d15163d9e6bbf9b11ba833e/The%20Smart%20Pad.png",
        use_column_width=True  
    )

# Banner image 
with banner_col:
    st.image(
       
        "https://raw.githubusercontent.com/Azmam1099/The-Smart_Pad/8ffea45bad2d08b33d15163d9e6bbf9b11ba833e/White%20Black%20Cute%20Minimalist%20and%20Elegant%20Toys%20Review%20Banner.png",
        use_column_width=500
    )



st.markdown("---")

# --- PRODUCT GRID ---

num_columns = 3
cols = st.columns(num_columns)

# Loop through the products and display them in the grid.
for i, product in enumerate(PRODUCTS):
    # This places each product in the next available column, then wraps to the next row.
    with cols[i % num_columns]:
        # `st.container(border=True)` creates the "card" look
        with st.container(border=True):
            st.image(product["image_url"], use_column_width=True)
            st.subheader(product["title"])
            st.write(product["description"])
            
            # `use_container_width=True` makes the button fill the card width
            st.link_button(
                "Buy Now",
                product["affiliate_link"],
                use_container_width=True
            )

st.markdown("---")
# footer caption
st.caption("© 2025 The Smart Pad | All products recommended are based on personal use and research.")
