from flask import Flask, render_template, request
import instaloader
import os

app = Flask(__name__)

# 🔐 كتابة ملف الشهادة من المتغير البيئي
with open("ca.crt", "w") as f:
    f.write(os.environ.get("CA_CERT", ""))

# تحميل بيانات الحساب والبروكسي من المتغيرات البيئية
IG_USERNAME = os.getenv("INSTAGRAM_USERNAME")
IG_PASSWORD = os.getenv("INSTAGRAM_PASSWORD")
PROXY_HOST = os.getenv("PROXY_HOST")
PROXY_PORT = os.getenv("PROXY_PORT")
PROXY_USER = os.getenv("PROXY_USER")
PROXY_PASS = os.getenv("PROXY_PASS")

# إعداد البروكسي للبيئة
proxy_url = f"http://{PROXY_USER}:{PROXY_PASS}@{PROXY_HOST}:{PROXY_PORT}"
os.environ["http_proxy"] = proxy_url
os.environ["https_proxy"] = proxy_url

# إعداد Instaloader مع التحقق من الشهادة
L = instaloader.Instaloader()
L.context._session.verify = "ca.crt"  # ⬅️ مهم جداً

try:
    L.login(IG_USERNAME, IG_PASSWORD)
    print("✅ تم تسجيل الدخول بنجاح")
except Exception as e:
    print(f"❌ فشل تسجيل الدخول: {e}")
