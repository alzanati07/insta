from flask import Flask, render_template, request
import instaloader
import os

app = Flask(__name__)

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

# إعداد Instaloader
L = instaloader.Instaloader()

try:
    L.login(IG_USERNAME, IG_PASSWORD)
    print("✅ تم تسجيل الدخول بنجاح")
except Exception as e:
    print(f"❌ فشل تسجيل الدخول: {e}")

@app.route("/", methods=["GET", "POST"])
def index():
    posts, stories, highlights = [], [], []
    if request.method == "POST":
        target_username = request.form["target_username"]
        try:
            profile = instaloader.Profile.from_username(L.context, target_username)
            posts = [post.url for post in profile.get_posts()[:5]]  # آخر 5 منشورات

            for story in L.get_stories(userids=[profile.userid]):
                for item in story.get_items():
                    stories.append(item.url)

            for highlight in profile.get_highlights():
                for item in highlight.get_items():
                    highlights.append(item.url)

        except Exception as e:
            print(f"❌ خطأ أثناء تحميل البيانات: {e}")

    return render_template("index.html", posts=posts, stories=stories, highlights=highlights)

# لا تستخدم app.run في الإنتاج (مثلاً عند النشر على Vercel أو Render)
