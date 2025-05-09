from flask import Flask, render_template, request
import instaloader
import os

app = Flask(__name__)
L = instaloader.Instaloader()

@app.route("/", methods=["GET", "POST"])
def index():
    posts, stories, highlights = [], [], []
    if request.method == "POST":
        target_username = request.form["target_username"]

        try:
            profile = instaloader.Profile.from_username(L.context, target_username)
            posts = [post.url for post in profile.get_posts()[:5]]  # Top 5 posts

            for story in L.get_stories(userids=[profile.userid]):
                for item in story.get_items():
                    stories.append(item.url)

            for highlight in profile.get_highlights():
                for item in highlight.get_items():
                    highlights.append(item.url)

        except Exception as e:
            print(f"Error: {e}")

    return render_template("index.html", posts=posts, stories=stories, highlights=highlights)

if __name__ == "__main__":
    # تحديد المنفذ الذي توفره Render أو استخدام المنفذ الافتراضي 5000
    port = int(os.environ.get("PORT", 5000))  # تحديد المنفذ
    app.run(host="0.0.0.0", port=port)  # استمع على المنفذ المحدد
