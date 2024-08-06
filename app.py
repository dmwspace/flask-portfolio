from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def base_page():
    return render_template('base.html')

@app.route("/contact")
def contact_page():
    return render_template('contact.html')

@app.route("/skills")
def skills_page():
    return render_template('skills.html')

@app.route("/about")
def about_page():
    return render_template('about.html')

@app.route("/projects")
def projects_page():
    return render_template('projects.html')