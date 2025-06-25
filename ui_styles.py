import streamlit as st

def apply_styles():
    st.markdown("""
        <style>
        .main {
            background-color: #1a1a1a;
            color: #e0e0e0;
            font-family: 'Arial', sans-serif;
        }
        .stTextInput > div > div > input {
            background-color: #2a2a2a;
            color: #e0e0e0;
            border: 2px solid #555;
            border-radius: 10px;
            padding: 10px;
            font-size: 16px;
        }
        .stButton > button {
            background-color: #4a90e2;
            color: white;
            border: none;
            padding: 12px 24px;
            border-radius: 10px;
            font-size: 16px;
            transition: background-color 0.3s;
        }
        .stButton > button:hover {
            background-color: #357abd;
            transform: scale(1.05);
        }
        .stCodeBlock {
            background-color: #2a2a2a;
            padding: 15px;
            border-radius: 10px;
            border-left: 5px solid #4a90e2;
            font-size: 14px;
        }
        .stSuccess {
            background-color: #28a745;
            color: white;
            padding: 10px;
            border-radius: 5px;
            text-align: center;
        }
        .stError {
            background-color: #dc3545;
            color: white;
            padding: 10px;
            border-radius: 5px;
            text-align: center;
        }
        .stSpinner > div {
            border-top-color: #4a90e2 !important;
        }
        </style>
    """, unsafe_allow_html=True)

# Apply styles when the module is imported
apply_styles()