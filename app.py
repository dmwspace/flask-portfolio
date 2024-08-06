from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def base_page():
    return render_template('base.html')