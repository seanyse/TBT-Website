from flask import Blueprint, render_template, request, send_from_directory
import os
import requests
import datetime
import pytz


views = Blueprint(__name__, "views")

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
