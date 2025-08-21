import random

def send_otp(email):
    otp = str(random.randint(100000, 999999))
    print(f"[DEBUG] OTP for {email}: {otp}")  # Replace with actual email service later
    return otp
