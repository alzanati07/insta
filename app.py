from flask import Flask, render_template, request
import instaloader
import os
from dotenv import load_dotenv

# تحميل متغيرات البيئة من .env
load_dotenv()

app = Flask(__name__)
L = instaloader.Instaloader()

# تسجيل الدخول بالحساب الوهمي
IG_USERNAME = os.getenv("IG_USERNAME")
IG_PASSWORD = os.getenv("IG_PASSWORD")

try:
    L.login(IG_USERNAME, IG_PASSWORD)
except Exception as e:
    print(f"فشل تسجيل الدخول: {e}")

@app.route("/", methods=["GET", "POST"])
def index():
    posts, stories, highlights = [], [], []
    if request.method == "POST":
        target_username = request.form["target_username"]

        try:
            profile = instaloader.Profile.from_username(L.context, target_username)
            posts = [post.url for post in profile.get_posts()[:5]]

            for story in L.get_stories(userids=[profile.userid]):
                for item in story.get_items():
                    stories.append(item.url)

            for highlight in profile.get_highlights():
                for item in highlight.get_items():
                    highlights.append(item.url)

        except Exception as e:
            print(f"Error: {e}")

    return render_template("index.html", posts=posts, stories=stories, highlights=highlights)
