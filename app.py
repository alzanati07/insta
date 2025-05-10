from flask import Flask, render_template, request
import instaloader
import os
import base64

app = Flask(__name__)

# ✅ حفظ شهادة SSL من المتغير البيئي (مشفّرة base64)
ca_cert = os.environ.get("CA_CERT", "")
if ca_cert:
    try:
        decoded_cert = base64.b64decode(ca_cert.encode())
        with open("ca.crt", "wb") as f:  # حفظ بصيغة ثنائية
            f.write(decoded_cert)
        os.environ["REQUESTS_CA_BUNDLE"] = "ca.crt"  # ✅ تعيين متغير البيئة للشهادة
        print("✅ تم فك تشفير الشهادة وحفظها بنجاح")
    except Exception as e:
        print(f"⚠️ فشل فك تشفير الشهادة: {e}")

# ✅ تحميل بيانات الحساب من البيئة
IG_USERNAME = os.getenv("INSTAGRAM_USERNAME")
IG_PASSWORD = os.getenv("INSTAGRAM_PASSWORD")

# ✅ إعداد Instaloader مع الشهادة
L = instaloader.Instaloader()
if ca_cert:
    L.context._session.verify = "ca.crt"

# ✅ تسجيل الدخول
try:
    L.login(IG_USERNAME, IG_PASSWORD)
    print("✅ تم تسجيل الدخول بنجاح")
except Exception as e:
    print(f"❌ فشل تسجيل الدخول: {e}")
