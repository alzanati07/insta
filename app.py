from flask import Flask, render_template, request
import instaloader

app = Flask(__name__)

# ✅ تعيين بيانات حساب إنستغرام مباشرة
IG_USERNAME = "your_username"
IG_PASSWORD = "your_password"

# ✅ إعداد Instaloader
L = instaloader.Instaloader()

# ✅ تسجيل الدخول
try:
    L.login(IG_USERNAME, IG_PASSWORD)
    print("✅ تم تسجيل الدخول بنجاح")
except Exception as e:
    print(f"❌ فشل تسجيل الدخول: {e}")
