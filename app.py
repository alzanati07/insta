from flask import Flask, render_template, request
import instaloader

app = Flask(__name__)
L = instaloader.Instaloader()

# إعداد بروكسي (بدّله عند الحاجة)
L.context.proxy = "http://185.199.229.156:7492"

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
