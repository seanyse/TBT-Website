from flask import Blueprint, render_template, request, send_from_directory, redirect, Flask, session
import os
import requests
import datetime
import pytz
import random


views = Blueprint("views", __name__)


@views.route("/")
def home():
    # try:
    #     webhook = os.environ["webhook"] 
    #     est = pytz.timezone('America/New_York')
    #     now = datetime.datetime.now(est)

    #     data = {
    #     "content": f"TBT New Website Vistor at {now.strftime('%Y-%m-%d %H:%M:%S')}"
    #     }
    #     response = requests.post(webhook, json=data)
    #     print(data)

    # except Exception as e:
    #     print(e)

    return render_template("home.html")



@views.route("/mission/")
def mission():
    return render_template("mission.html")

@views.route("/whyus/")
def whyus():
    return render_template("whyus.html")

@views.route("/contact/")
def contact():
    return render_template("contact.html")

@views.route("/faq/")
def faq():
    return render_template("faq.html")

@views.route("/about/")
def about():
    return render_template("about.html")

@views.route("/book/")
def book():
    return render_template("book.html")

@views.route('/courses/')
def courses():
    return render_template("courses.html")

@views.route('/tutor/')
def beatutor():
    return render_template("tutor.html")

@views.route('/board/')
def beBoard():
    return redirect("https://docs.google.com/forms/d/e/1FAIpQLSdsE_9r5CxcJwsfwZ39UzKz11YhqOC-v72KYm5H6_1lcHxwdw/viewform?vc=0&c=0&w=1&flr=0", code=302)

@views.route('/survey/')
def survey():
    return render_template("survey.html")
    num = random.randint(0,100)
    if (num < 50):
        print("1")
        return redirect("https://forms.gle/YCH17TF2MxVizYne8")
    else:
        print("2")
        return redirect("https://forms.gle/gT9ZdjBjJKV35VtJ8")


