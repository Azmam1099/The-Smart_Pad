import streamlit as st
from datetime import datetime
import random

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="The Smart Pad — Modern Minimalist",
                   page_icon="🛍️",
                   layout="wide")

# ---------------- SESSION INIT ----------------
if "wishlist" not in st.session_state:
    st.session_state.wishlist = set()
if "ratings" not in st.session_state:
    st.session_state.ratings = {}  # key: product title -> rating (1-5)

# ---------------- PRODUCT DATA (EDIT HERE) ----------------
PRODUCTS = [
    {
        "id": "cob_keychain",
        "title": "COB Keychain Light",
        "category": "Gadgets",
        "description": "A super bright, rechargeable mini-light that fits on your keychain.",
        "image_url": "https://placehold.co/600x600/ffffff/111111?text=COB+Keychain+Light",
        "affiliate_link": "https://www.amazon.com/your-link-here",
        "price": 9.99,
        "rating": 4.3
    },
    {
        "id": "air_purifier",
        "title": "Smart Air Purifier",
        "category": "Home",
        "description": "A Wi-Fi enabled air purifier that you can control with your phone.",
        "image_url": "https://placehold.co/600x600/ffffff/111111?text=Smart+Air+Purifier",
        "affiliate_link": "https://www.amazon.com/your-link-here",
        "price": 129.99,
        "rating": 4.6
    },
    {
        "id": "portable_blender",
        "title": "Portable Blender",
        "category": "Kitchen",
        "description": "Make smoothies on the go. USB-rechargeable and easy to clean.",
        "image_url": "https://placehold.co/600x600/ffffff/111111?text=Portable+Blender",
        "affiliate_link": "https://www.amazon.com/your-link-here",
        "price": 34.99,
        "rating": 4.1
    },
    {
        "id": "wireless_earbuds",
        "title": "Wireless Earbuds",
        "category": "Audio",
        "description": "Noise-cancelling earbuds with a 30-hour battery charging case.",
        "image_url": "https://placehold.co/600x600/ffffff/111111?text=Wireless+Earbuds",
        "affiliate_link": "https://www.amazon.com/your-link-here",
        "price": 79.99,
        "rating": 4.4
    },
    {
        "id": "sunrise_alarm",
        "title": "Sunrise Alarm Clock",
        "category": "Home",
        "description": "Wake up naturally with a light that simulates a sunrise.",
        "image_url": "https://placehold.co/600x600/ffffff/111111?text=Sunrise+Alarm+Clock",
        "affiliate_link": "https://www.amazon.com/your-link-here",
        "price": 49.99,
        "rating": 4.2
    },
    {
        "id": "mag_phone_mount",
        "title": "Magnetic Phone Mount",
        "category": "Gadgets",
        "description": "A sleek and strong magnetic mount for your car dashboard.",
        "image_url": "https://placehold.co/600x600/ffffff/111111?text=Magnetic+Phone+Mount",
        "affiliate_link": "https://www.amazon.com/your-link-here",
        "price": 14.99,
        "rating": 4.0
    },
]

# ---------------- STYLES: Modern Minimalist ----------------
# CSS is minimal, subtle animations, hover effects, dark-mode variation
st.markdown(
    """
    <style>
    :root{
      --bg: #f7f8fb;
      --card: #ffffff;
      --muted: #6b6f76;
      --accent: #0f1724;
      --glass: rgba(255,255,255,0.6);
    }
    .block-container{
      padding-top: 1.5rem;
      padding-left: 2rem;
      padding-right: 2rem;
      max-width: 1400px;
    }

    /* Header */
    .header-row { display:flex; align-items:center; gap: 1rem; margin-bottom: 0.4rem; }
    .brand-title { font-size: 1.4rem; font-weight:700; letter-spacing: -0.3px; margin:0; }
    .brand-sub { margin:0; color:var(--muted); font-size:0.95rem; }

    /* Page background */
    .page {
      background: linear-gradient(180deg, var(--bg), #ffffff);
      padding: 1rem;
      border-radius: 16px;
    }

    /* Deal of the Day */
    .hero {
      background: linear-gradient(90deg, rgba(255,255,255,0.5), rgba(250,250,252,0.6));
      border-radius: 14px;
      padding: 20px;
      display:flex;
      gap: 18px;
      align-items:center;
      box-shadow: 0 8px 30px rgba(15,23,36,0.06);
    }
    .hero-img { width: 250px; border-radius: 12px; overflow:hidden; }
    .hero-meta { flex:1; }
    .deal-badge { background: #eef2ff; color:#1e293b; padding:6px 10px; border-radius:999px; font-weight:700; display:inline-block; margin-bottom:10px; }

    /* Grid & cards */
    .product-grid { display:grid; grid-template-columns: repeat(auto-fill, minmax(260px, 1fr)); gap:18px; margin-top:18px; }
    .card {
      background: var(--card);
      border-radius: 14px;
      padding: 14px;
      box-shadow: 0 6px 20px rgba(10,12,14,0.04);
      transition: transform .22s ease, box-shadow .22s ease;
      border: 1px solid rgba(15,23,36,0.03);
    }
    .card:hover { transform: translateY(-6px); box-shadow: 0 18px 40px rgba(10,12,14,0.06); }
    .img-wrap { border-radius: 10px; overflow:hidden; display:block; }
    .img-wrap img { width:100%; display:block; transition: transform .45s cubic-bezier(.2,.9,.2,1); }
    .card:hover .img-wrap img { transform: scale(1.06); }

    .title { font-weight:700; margin-top:10px; font-size:1.03rem; color:var(--accent);}
    .desc { color:var(--muted); font-size:0.92rem; margin-top:6px; height:44px; overflow:hidden; }
    .price-row { display:flex; justify-content:space-between; align-items:center; margin-top:12px; gap:8px; }
    .price { font-weight:700; font-size:1.05rem; }
    .muted { color:var(--muted); font-size:0.9rem; }

    /* Buttons */
    .btn {
      display:inline-block;
      background: transparent;
      border: 1px solid rgba(15,23,36,0.08);
      padding:10px 12px;
      border-radius: 10px;
      font-weight:700;
      cursor:pointer;
      transition: transform .12s ease, box-shadow .12s ease;
    }
    .btn:active { transform: translateY(1px) scale(0.997); }
    .btn-primary {
      background: white;
      border: 1px solid rgba(2,6,23,0.06);
      box-shadow: 0 6px 20px rgba(2,6,23,0.03);
    }

    /* small icons */
    .heart {
      font-size:1.1rem; cursor:pointer;
      border-radius: 999px; padding:6px;
    }

    /* responsive tweaks */
    @media (max-width: 680px) {
      .hero { flex-direction:column; gap:12px; }
      .hero-img { width:100%; }
    }

    /* Dark mode */
    .dark :root, .dark .block-container { --bg: #0b1020; --card: #071023; --muted: #aab3c3; --accent: #e6eefc; color: #e6eefc; }
    .dark .hero { background: linear-gradient(90deg, rgba(255,255,255,0.02), rgba(255,255,255,0.01)); }
    .dark .card { border: 1px solid rgba(255,255,255,0.03); box-shadow: 0 8px 30px rgba(0,0,0,0.6); }
    .dark .btn { border-color: rgba(255,255,255,0.03); color: var(--accent); }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------- HEADER (brand + controls) ----------------
c1, c2, c3 = st.columns([2, 3, 2])
with c1:
    st.markdown('<div class="header-row"><div><img src="https://raw.githubusercontent.com/Azmam1099/The-Smart_Pad/8ffea45bad2d08b33d15163d9e6bbf9b11ba833e/The%20Smart%20Pad.png" width=86 style="border-radius:8px"></div><div style="margin-left:8px"><p class="brand-title">The Smart Pad</p><p class="brand-sub">Minimal picks for cleaner living</p></div></div>', unsafe_allow_html=True)

with c2:
    # Search & category filters
    query = st.text_input("Search products", placeholder="Search by name or description...", key="search_input")
    categories = ["All"] + sorted({p["category"] for p in PRODUCTS})
    category = st.selectbox("Category", categories, key="category_filter")
with c3:
    # Dark mode toggle + wishlist button
    dark = st.checkbox("Dark mode", value=False, key="dark_toggle")
    # wishlist toggle
    if st.button("View Wishlist ❤️", key="open_wishlist"):
        st.session_state._show_wishlist = True

# Apply dark container class by adding a wrapper (simple trick)
if dark:
    st.markdown('<div class="dark">', unsafe_allow_html=True)

st.markdown('<div class="page">', unsafe_allow_html=True)

# ---------------- Deal of the Day (hero) ----------------
# Choose a hero product dynamically (first in list or random)
hero = PRODUCTS[0]
hero_discount = 0.25  # 25% off for show
hero_price = hero["price"]
hero_sale = round(hero_price * (1 - hero_discount), 2)

st.markdown(
    f"""
    <div class="hero">
      <div class="hero-img">
        <img src="{hero['image_url']}" alt="hero" style="width:100%; display:block;">
      </div>
      <div class="hero-meta">
        <div class="deal-badge">Deal of the Day</div>
        <h2 style="margin:0 0 6px 0; font-size:1.45rem; color:var(--accent)">{hero['title']}</h2>
        <p style="margin:0 0 10px 0; color:var(--muted);">{hero['description']}</p>
        <div style="display:flex; gap:12px; align-items:center; margin-top:8px;">
          <div style="font-weight:700; font-size:1.25rem;">${hero_sale:.2f}</div>
          <div style="color:var(--muted); text-decoration: line-through;">${hero_price:.2f}</div>
          <div style="padding:6px 10px; background:#eaf3ff; border-radius:8px; font-weight:700; color:#0f1724;">-{int(hero_discount*100)}%</div>
        </div>
        <div style="margin-top:14px;">
          <a href="{hero['affiliate_link']}" target="_blank"><button class="btn btn-primary">Buy Deal</button></a>
        </div>
      </div>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

# ---------------- FILTER PRODUCTS ----------------
def filter_products(products, q, cat):
    q = (q or "").strip().lower()
    out = []
    for p in products:
        if cat and cat != "All" and p["category"] != cat:
            continue
        if q:
            hay = f"{p['title']} {p['description']} {p.get('category','')}".lower()
            if q not in hay:
                continue
        out.append(p)
    return out

visible_products = filter_products(PRODUCTS, query, category)

# ---------------- TOOLBAR: sort, show ratings ----------------
t1, t2, t3 = st.columns([2, 1, 1])
with t1:
    st.write("")  # spacer
with t2:
    sortby = st.selectbox("Sort by", ["Featured", "Price: Low → High", "Price: High → Low", "Top Rated"], key="sort_select")
with t3:
    show_ratings = st.checkbox("Show Ratings", value=True, key="show_ratings")

# apply sorting
if sortby == "Price: Low → High":
    visible_products = sorted(visible_products, key=lambda x: x["price"])
elif sortby == "Price: High → Low":
    visible_products = sorted(visible_products, key=lambda x: -x["price"])
elif sortby == "Top Rated":
    visible_products = sorted(visible_products, key=lambda x: -x.get("rating", 0))

# ---------------- PRODUCT GRID ----------------
st.markdown('<div class="product-grid">', unsafe_allow_html=True)

for p in visible_products:
    pid = p["id"]
    # Card HTML wrapper
    # Title, desc, image, price, rating, wishlist-heart, buy button, user rating control
    liked = pid in st.session_state.wishlist
    user_rating = st.session_state.ratings.get(pid, None)

    # Build rating stars display
    base_rating = p.get("rating", 0)
    display_rating = user_rating if user_rating is not None else base_rating
    filled = int(round(display_rating))

    # Unique keys for interactive widgets per product
    heart_key = f"heart_{pid}"
    rate_key = f"rate_{pid}"
    buy_key = f"buy_{pid}"

    # Card HTML start
    st.markdown('<div class="card">', unsafe_allow_html=True)

    # Image
    st.markdown(f'<div class="img-wrap"><img src="{p["image_url"]}" loading="lazy"></div>', unsafe_allow_html=True)

    # Title and description
    st.markdown(f'<div class="title">{p["title"]}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="desc">{p["description"]}</div>', unsafe_allow_html=True)

    # Price + rating row
    col_a, col_b = st.columns([2, 1])
    with col_a:
        st.markdown(f'<div class="price-row"><div><div class="price">${p["price"]:.2f}</div><div class="muted">Category: {p["category"]}</div></div></div>', unsafe_allow_html=True)
    with col_b:
        if show_ratings:
            stars = " ".join(["★" if i < filled else "☆" for i in range(5)])
            st.markdown(f'<div style="text-align:right; font-weight:700; color:#f59e0b; font-size:1.05rem;">{stars}</div>', unsafe_allow_html=True)

    # Buttons row (Wishlist + Buy)
    b1, b2 = st.columns([1, 2])
    with b1:
        # Wishlist toggle (heart)
        if st.button("❤️" if liked else "🤍", key=heart_key):
            # toggle
            if liked:
                st.session_state.wishlist.remove(pid)
            else:
                st.session_state.wishlist.add(pid)
            # trigger rerun so UI updates
            st.experimental_rerun()
    with b2:
        st.write("")  # small spacer to align
        st.markdown(f'<a href="{p["affiliate_link"]}" target="_blank"><button class="btn btn-primary" style="width:100%;">Buy Now →</button></a>', unsafe_allow_html=True)

    # Rating control (user can set 1-5)
    cols_rate = st.columns([1, 1, 1, 1, 1])
    st.markdown('<div style="margin-top:8px; color:var(--muted); font-size:0.9rem">Rate this product:</div>', unsafe_allow_html=True)
    for i in range(5):
        def make_rate_callback(pid=pid, val=i+1):
            def _cb():
                st.session_state.ratings[pid] = val
            return _cb
        if cols_rate[i].button("★" if (user_rating and i < user_rating) else "☆", key=f"{rate_key}_{i}", on_click=make_rate_callback()):
            st.experimental_rerun()

    st.markdown("</div>", unsafe_allow_html=True)  # card end

st.markdown("</div>", unsafe_allow_html=True)  # grid end

st.markdown("---")

# ---------------- WISHLIST PANEL ----------------
# Show wishlist in a sidebar-style area below
if getattr(st.session_state, "_show_wishlist", False):
    st.session_state._show_wishlist = False
    st.markdown("## ❤️ Your Wishlist")
    if st.session_state.wishlist:
        for pid in st.session_state.wishlist:
            prod = next((x for x in PRODUCTS if x["id"] == pid), None)
            if not prod:
                continue
            col1, col2, col3 = st.columns([1, 3, 1])
            with col1:
                st.image(prod["image_url"], width=80)
            with col2:
                st.markdown(f"**{prod['title']}**  \n{prod['description']}")
            with col3:
                if st.button("Remove", key=f"remove_{pid}"):
                    st.session_state.wishlist.remove(pid)
                    st.experimental_rerun()
    else:
        st.info("Your wishlist is empty — tap the 🤍 icons to add products you like!")

# ---------------- FOOTER ----------------
st.caption("As an affiliate, I may earn a commission from qualifying purchases. © 2025 The Smart Pad")

# Close dark wrapper if used
st.markdown("</div>", unsafe_allow_html=True)
if dark:
    st.markdown("</div>", unsafe_allow_html=True)
