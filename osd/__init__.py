from flask import Flask

from flask import Flask, request, session, redirect, url_for, render_template, flash, abort
app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')

@app.route('/osd', methods=['GET', 'POST'])
def index():
    return render_template("index.html")

print("starting app on port: 5000") 
