import streamlit as st
import random

def send_otp(email):
    otp = str(random.randint(100000, 999999))
    st.session_state.otp = otp
    return otp

def login_flow():
    st.subheader("🔐 Two-Factor Authentication")
    email = st.text_input("Enter your email")

    if st.button("Send OTP"):
        otp = send_otp(email)
        st.success(f"OTP sent to {email} (simulated: {otp})")

    entered_otp = st.text_input("Enter OTP")
    if st.button("Verify OTP"):
        if entered_otp == st.session_state.get("otp"):
            st.session_state.authenticated = True
            st.success("✅ Authentication successful")
        else:
            st.error("❌ Invalid OTP")
