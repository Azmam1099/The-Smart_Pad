import streamlit as st

# --- PAGE CONFIGURATION ---
# This must be the first Streamlit command.
st.set_page_config(
    page_title="The Samrt Pad",
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
logo_col, title_col = st.columns([1, 4]) # Logo column is 1/5, title is 4/5

with logo_col:
    # Add your logo here.
    st.image(
        "https://raw.githubusercontent.com/YourUsername/YourRepo/main/logo.png", # <-- PASTE YOUR LOGO URL HERE
        width=150  # Adjust width as needed
    )

with title_col:
    st.title("My Favorite Gadgets")
    st.write(
        """
        Explore the viral most trending products for Home and Garden
        """
    )

# Add a banner image (optional)
# Uncomment the line below and replace the URL to add a big graphic banner
st.image(
    "https://raw.githubusercontent.com/YourUsername/YourRepo/main/banner.jpg", # <-- PASTE YOUR BANNER URL HERE
    use_column_width=True
)
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
#st.caption("© 2025 Your Name Here | All products recommended are based on personal use and research.")
