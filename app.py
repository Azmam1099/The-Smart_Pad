import streamlit as st

# --- PAGE CONFIGURATION ---
# This must be the first Streamlit command.
st.set_page_config(
    page_title="The Smart Pad",  # Corrected typo
    page_icon="🛍️",
    layout="wide"  # Use "wide" layout for a grid
)

# --- PRODUCT DATA ---
# A list of dictionaries. Each dictionary is a product.
# This is the ONLY section you need to edit to add/change products.
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

# --- HEADER SECTION ---
# Create columns for logo and title
#logo_col, title_col = st.columns([1, 4]) # Logo column is 1/5, title is 4/5

with logo_col:
    # Add your logo here.
    st.image(
        # This is the corrected "RAW" link
        "https://raw.githubusercontent.com/Azmam1099/The-Smart_Pad/8ffea45bad2d08b33d15163d9e6bbf9b11ba833e/The%20Smart%20Pad.png",
        width=150  # Adjust width as needed
    )

# Add a banner image (optional)
st.image(
    # This is the corrected "RAW" link
    "https://raw.githubusercontent.com/Azmam1099/The-Smart_Pad/8ffea45bad2d08b33d15163d9e6bbf9b11ba833e/White%20Black%20Cute%20Minimalist%20and%20Elegant%20Toys%20Review%20Banner.png",
    use_column_width=True
)

# It's important to have an affiliate disclosure!
#st.caption("As an affiliate, I may earn a commission from qualifying purchases. This helps support my content!")

st.markdown("---")

# --- PRODUCT GRID ---
# Define the number of columns you want in your grid.
# The Beebom site uses 3 columns on a wide screen.
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
# Also added a footer caption
st.caption("© 2025 The Smart Pad | All products recommended are based on personal use and research.")
