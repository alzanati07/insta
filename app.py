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
        with open("ca.crt", "wb") as f:
            f.write(decoded_cert)
        os.environ["REQUESTS_CA_BUNDLE"] = "ca.crt"
        print("✅ تم فك تشفير الشهادة وحفظها بنجاح")
    except Exception as e:
        print(f"⚠️ فشل فك تشفير الشهادة: {e}")

# ✅ تعيين بيانات الحساب مباشرة
IG_USERNAME = "alzanatitik@gmail.com"
IG_PASSWORD = "12345678z"

# ✅ إعداد Instaloader مع الشهادة إن وجدت
L = instaloader.Instaloader()
if ca_cert:
    L.context._session.verify = "ca.crt"

# ✅ تسجيل الدخول
try:
    L.login(IG_USERNAME, IG_PASSWORD)
    print("✅ تم تسجيل الدخول بنجاح")
except Exception as e:
    print(f"❌ فشل تسجيل الدخول: {e}")
