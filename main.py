from flask import Flask, render_template
import requests

app = Flask(__name__)


blog_url = "https://api.npoint.io/5409d7dfbf7ecbeb5fb6"
response = requests.get(url=blog_url).json()

@app.route('/')
def home():
    return render_template("index.html", blogs=response)


@app.route('/post/<blog_id>')
def post(blog_id):
    blog_id = int(blog_id)
    return render_template("post.html", blog=response[blog_id-1])


@app.route('/about')
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run()
