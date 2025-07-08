import streamlit as st
import numpy as np
import joblib

# Load model
model = joblib.load("RandomForest_diamond_price_model.pkl")

# Page config
st.set_page_config(page_title="DIAMOND PRICE PREDICTOR", layout="wide", page_icon="💎")

# Robust CSS: Assign grey background to the first column only
st.markdown("""
    <style>
    .css-1lcbmhc {  /* This class usually belongs to first column in 2-column layout */
        background-color: #f0f0f0 !important;
        min-height: 100vh;
        padding: 2rem;
        border-radius: 8px;
    }
    .left-col ul {
        padding-left: 1.2rem;
        line-height: 1.8;
    }
    .left-col li {
        font-size: 16px;
    }
    h1, h2, h3 {
        color: #2E86C1;
        text-align: center;
    }
    .stButton > button {
        background-color: #c2185b;
        color: white;
        font-weight: bold;
        border-radius: 12px;
        height: 3em;
        width: 100%;
        transition: 0.3s;
        border: none;
    }
    .stButton > button:hover {
        background-color: #ad1457;
    }
    </style>
""", unsafe_allow_html=True)

# Columns for layout
col1, col2 = st.columns([1, 2])

# LEFT COLUMN: Tips section with grey background and image
with col1:
    st.markdown('<div class="left-col">', unsafe_allow_html=True)

    st.markdown("### 💡 Diamond Tips")
    st.markdown("""
    <ul>
        <li>💎 Higher <b>cut</b> quality = more sparkle</li>
        <li>💎 <b>Color D</b> is most colorless</li>
        <li>💎 <b>IF clarity</b> = internally flawless</li>
        <li>💎 Larger <b>carat</b> increases price exponentially</li>
    </ul>
    ✴️ <i>Choose wisely to get the best value!</i>
    """, unsafe_allow_html=True)

    # Image placed BELOW the tips
    st.image("download.jpg", use_container_width=True)

    st.markdown('</div>', unsafe_allow_html=True)

# RIGHT COLUMN: User input and output
with col2:
    st.markdown("## 💍 **DIAMOND PRICE PREDICTOR**")
    st.markdown("✨ *Enter the diamond features to estimate its price in USD*")

    carat = st.slider("🔹 Carat Weight", 0.2, 5.0, 0.5)
    cut = st.selectbox("🔹 Cut Quality", ['Fair', 'Good', 'Very Good', 'Premium', 'Ideal'])
    color = st.selectbox("🔹 Diamond Color", ['D', 'E', 'F', 'G', 'H', 'I', 'J'])
    clarity = st.selectbox("🔹 Clarity Grade", ['I1', 'SI2', 'SI1', 'VS2', 'VS1', 'VVS2', 'VVS1', 'IF'])
    depth = st.slider("🔹 Depth (%)", 50.0, 70.0, 61.0)
    table = st.slider("🔹 Table (%)", 50.0, 70.0, 57.0)
    volume = st.slider("🔹 Volume (x × y × z)", 0.0, 600.0, 60.0)

    # Encoding
    def encode_inputs(cut, color, clarity):
        cut_map = {'Fair': 0, 'Good': 1, 'Very Good': 2, 'Premium': 3, 'Ideal': 4}
        color_map = {'J': 0, 'I': 1, 'H': 2, 'G': 3, 'F': 4, 'E': 5, 'D': 6}
        clarity_map = {'I1': 0, 'SI2': 1, 'SI1': 2, 'VS2': 3, 'VS1': 4, 'VVS2': 5, 'VVS1': 6, 'IF': 7}
        return cut_map[cut], color_map[color], clarity_map[clarity]

    cut_enc, color_enc, clarity_enc = encode_inputs(cut, color, clarity)
    input_features = np.array([[carat, depth, table, volume, cut_enc, color_enc, clarity_enc]])

    if st.button("💰 Predict Diamond Price"):
        prediction = model.predict(input_features.astype(np.float64))[0]
        st.success(f"💸 Estimated Price: **${prediction:,.2f}**")
