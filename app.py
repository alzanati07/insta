from flask import Flask, render_template, request
import instaloader
import os
import base64

app = Flask(__name__)

# ✅ حفظ شهادة SSL من المتغير البيئي (مشفّرة base64)
ca_cert = os.environ.get("CA_CERT", "")
crt_path = "ca.crt"

if ca_cert:
    try:
        decoded_cert = base64.b64decode(ca_cert.encode())
        with open(crt_path, "wb") as f:  # حفظ بصيغة ثنائية
            f.write(decoded_cert)
        os.environ["REQUESTS_CA_BUNDLE"] = crt_path  # 🔑 ضبط الشهادة للـ requests
        print("✅ تم فك تشفير الشهادة وحفظها وتسجيلها في REQUESTS_CA_BUNDLE")
    except Exception as e:
        print(f"⚠️ فشل فك تشفير الشهادة: {e}")

# ✅ تحميل بيانات الحساب والبروكسي من البيئة
IG_USERNAME = os.getenv("INSTAGRAM_USERNAME")
IG_PASSWORD = os.getenv("INSTAGRAM_PASSWORD")
PROXY_HOST = os.getenv("PROXY_HOST")
PROXY_PORT = os.getenv("PROXY_PORT")
PROXY_USER = os.getenv("PROXY_USER")
PROXY_PASS = os.getenv("PROXY_PASS")

# ✅ إعداد البروكسي للبيئة
if all([PROXY_USER, PROXY_PASS, PROXY_HOST, PROXY_PORT]):
    proxy_url = f"http://{PROXY_USER}:{PROXY_PASS}@{PROXY_HOST}:{PROXY_PORT}"
    os.environ["http_proxy"] = proxy_url
    os.environ["https_proxy"] = proxy_url
    print("✅ تم إعداد البروكسي")
else:
    print("⚠️ لم يتم ضبط إعدادات البروكسي بشكل صحيح")

# ✅ إعداد Instaloader
L = instaloader.Instaloader()

# ✅ تسجيل الدخول
try:
    L.login(IG_USERNAME, IG_PASSWORD)
    print("✅ تم تسجيل الدخول بنجاح")
except Exception as e:
    print(f"❌ فشل تسجيل الدخول: {e}")
