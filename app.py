import streamlit as st
from PIL import Image

# 1. Page Configuration
st.set_page_config(
    page_title="Tenix Digital | Web Solutions",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Custom CSS for "Attractive" Design
st.markdown("""
    <style>
    /* Hide Main Streamlit UI for Professionalism */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Background and Container Styling */
    .stApp {
        background-color: #f8f9fa;
    }

    /* Service Card Styling */
    .service-card {
        background-color: white;
        padding: 25px;
        border-radius: 15px;
        border-left: 5px solid #007BFF;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        transition: transform 0.3s ease;
        margin-bottom: 20px;
        height: 250px;
    }
    .service-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 15px rgba(0,0,0,0.2);
    }
    
    /* WhatsApp Button Styling */
    .wa-button {
        background-color: #25D366;
        color: white !important;
        padding: 12px 24px;
        border-radius: 30px;
        text-decoration: none;
        font-weight: bold;
        display: inline-block;
        margin-top: 10px;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Header & Logo
col1, col2 = st.columns([1, 4])
with col1:
    # Use st.image for your uploaded logo
    try:
        logo = Image.open("logo.png") 
        st.image(logo, width=150)
    except:
        st.info("Upload logo.png to your folder")

with col2:
    st.title("Tenix Digital")
    st.subheader("Your Vision, Our Code. Local Businesses, Global Presence.")

st.divider()

# 4. Service Menu (The Clickable Part)
st.write("### Choose Your Digital Transformation")

# Define WhatsApp Function
def get_wa_link(service_name):
    base_msg = f"Hi Tenix Digital! I am interested in your {service_name} for my business."
    # Replace with YOUR actual number (include country code)
    phone_number = "91XXXXXXXXXX" 
    return f"https://wa.me/{phone_number}?text={base_msg.replace(' ', '%20')}"

col_a, col_b, col_c = st.columns(3)

with col_a:
    st.markdown(f"""
    <div class="service-card">
        <h3>📄 Static Site</h3>
        <p>Perfect for Doctors, Lawyers, and Small Shops. A digital brochure that works 24/7.</p>
        <p><b>Starts at ₹1,999</b></p>
        <a href="{get_wa_link('Static Site')}" target="_blank" class="wa-button">Order on WhatsApp</a>
    </div>
    """, unsafe_allow_html=True)

with col_b:
    st.markdown(f"""
    <div class="service-card" style="border-left-color: #28a745;">
        <h3>⚡ Dynamic App</h3>
        <p>For Cafes & Gyms. Manage menus, prices, and member logins in real-time.</p>
        <p><b>Starts at ₹4,999</b></p>
        <a href="{get_wa_link('Dynamic App')}" target="_blank" class="wa-button">Order on WhatsApp</a>
    </div>
    """, unsafe_allow_html=True)

with col_c:
    st.markdown(f"""
    <div class="service-card" style="border-left-color: #6c757d;">
        <h3>🏨 Hostel Management</h3>
        <p>The Full Tenix Suite. Automated rent, tenant portals, and digital registers.</p>
        <p><b>Custom Pricing</b></p>
        <a href="{get_wa_link('Hostel Management')}" target="_blank" class="wa-button">Consult Us</a>
    </div>
    """, unsafe_allow_html=True)

# 5. Footer Info
st.divider()
st.info("📍 Based in Your Town | 🚀 Websites delivered within 48-72 hours")
