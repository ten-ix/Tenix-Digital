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
    /* This targets the main st.title */
    .stApp h1 {
        color: #007BFF; /* You can change this to #003366 for a darker blue */
        font-weight: 800;
        letter-spacing: -0.5px;
    }

    /* This targets the subheaders (optional) */
    .stApp h3 {
        color: #003366;
    }
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
        
        /* The Magic Parts */
        display: flex;
        flex-direction: column;
        height: 100%; /* Makes cards in the same row equal height */
    }

    .card-content {
        flex-grow: 1; /* This pushes everything else down */
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
        /* This targets the footer and the bottom padding area */
    footer {
        background-color: #000000;
        color: white;
    }.black-footer {
        background-color: #000000;
        color: white;
        padding: 40px 20px;
        border-radius: 20px 20px 0 0; /* Rounds the top corners */
        margin-top: 50px;
    }
    /* This makes sure the text inside the footer stays white */
    .black-footer p, .black-footer h3 {
        color: white !important;
    }
      @media (max-width: 768px) {
        .service-card {
            margin-bottom: 15px;
        }
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

theme=Image.open("theme.png")
st.image(theme)

# 4. Service Menu (The Clickable Part)
st.write("### Choose Your Digital Transformation")

# Define WhatsApp Function
def get_wa_link(service_name):
    base_msg = f"Hi Tenix Digital! I am interested in your {service_name} for my business."
    # Replace with YOUR actual number (include country code)
    phone_number = "919301868258" 
    return f"https://wa.me/{phone_number}?text={base_msg.replace(' ', '%20')}"

col_a, col_b, col_c = st.columns(3)

st.success("📍 Based in Your Town | 🚀 Websites delivered within 48-72 hours")
# --- FOOTER SECTION ---
st.markdown('<div class="black-footer">', unsafe_allow_html=True)
col_f1, col_f2, col_f3 = st.columns(3)

with col_f1:
    if st.button("Terms of Service"):
        @st.dialog("Terms of Service")
        def tos():
            st.write("""
            **1. Services:** Tenix Digital provides web development services as described in the selected package.
            **2. Payments:** A 50% advance is required to start. Final files/access are handed over upon 100% payment.
            **3. Hosting:** We provide free hosting on community tiers. For custom domains or high-traffic needs, the client must pay third-party hosting costs.
            **4. Liability:** Tenix Digital is not responsible for business losses or data loss on the client's end.
            """)
        tos()

with col_f2:
    if st.button("Privacy Policy"):
        @st.dialog("Privacy Policy")
        def privacy():
            st.write("""
            **1. Data Collection:** We only collect your name and business details when you contact us via WhatsApp or Form.
            **2. Usage:** Your data is only used to build your website and contact you. We never sell your data.
            **3. DPDP Compliance:** In accordance with Indian laws, you can request us to delete your data at any time.
            **4. Cookies:** We use basic cookies to make this Streamlit app run faster.
            """)
        privacy()

with col_f3:
    st.write("© 2026 Tenix Parent Company")
    st.markdown("<p style='text-align: right; margin-top: 10px;'>© 2026 Tenix Parent Company</p>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
with col_a:
    st.markdown(f"""
    <div class="service-card">
        <div class="card-content">
            <h3>📄 Static Site</h3>
            <p>Perfect for Doctors and Small Shops. A digital brochure that works 24/7.</p>
            <p><b>Starts at ₹1,999</b></p>
        </div>
        <a href="{get_wa_link('Static Site')}" target="_blank" class="wa-button">Order on WhatsApp</a>
    </div>
    """, unsafe_allow_html=True)

with col_b:
    st.markdown(f"""
    <div class="service-card" style="border-left-color: #28a745;">
        <div class="card-content">
            <h3>⚡ Dynamic Site</h3>
            <p>For Cafes & Gyms. Manage menus, prices, and member logins in real-time.</p>
            <p><b>Starts at ₹4,999</b></p>
        </div>
        <a href="{get_wa_link('Dynamic Site')}" target="_blank" class="wa-button">Order on WhatsApp</a>
    </div>
    """, unsafe_allow_html=True)

with col_c:
    st.markdown(f"""
    <div class="service-card" style="border-left-color: #6c757d;">
    <div class="card-content">
        <h3>📊 Business Dashboard</h3>
        <p>For Distributors, wedding halls & Schools. Track sales, inventory, or student records in a private secure portal.</p>
        <p><b>Custom Pricing</b></p>
        </div>
        <a href="{get_wa_link('Custom Dashboard')}" target="_blank" class="wa-button">Consult Us</a>
    </div>
    """, unsafe_allow_html=True)

