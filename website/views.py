from flask import Blueprint,render_template,send_file
from pyhtml2pdf import converter

url='https://docs.google.com/document/d/1dG2UeIWW7-paRedfL2POwSqPSAzhAXNC/edit?usp=sharing&ouid=109133290184854211953&rtpof=true&sd=true'

views= Blueprint('views',__name__)

@views.route('/')
def home():
    return render_template("home.html")

@views.route('/about')
def about():
    return render_template("about.html")

@views.route('/projects')
def projects():
    return render_template("projects.html")

@views.route('/resume')
def resume():
    return render_template("resume.html")

@views.route('/down')
def convert_to_pdf():
    converter.convert(url,'./website/static/docs/Pawan Kumar.pdf')
    path='static/docs/Pawan Kumar.pdf'
    return send_file(path,as_attachment=True)