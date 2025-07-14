#Import Statements
from flask import Flask, render_template, request, url_for, redirect, flash
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SubmitField
from wtforms.validators import DataRequired, Email
from email_validator import validate_email, EmailNotValidError
import smtplib
import os
from dotenv import load_dotenv

#Utilities
load_dotenv()
my_email = os.getenv("my_email")
my_password = os.getenv("my_password")
app = Flask(__name__)
Bootstrap5(app)
app.config['SECRET_KEY'] = "Contraseña123"

class ContactForm(FlaskForm):
    name = StringField(label="Your Name", validators=[DataRequired()])
    email = EmailField(label="Your Email", validators=[DataRequired(), Email()])
    subject = StringField(label="Subject", validators=[DataRequired()])
    message = StringField(label="Message", validators=[DataRequired()])
    submit = SubmitField(label="Send Message")               

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/portfolio")
def portfolio():
    return render_template("service-details.html")

@app.route("/learnings")
def learnings():
    return render_template("starter-page.html")

@app.route("/contact", methods=["POST", "GET"])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
         message = f"Subject:{form.subject.data}\n\n{form.message.data}\nBest Wishes, {form.name.data} (Email: {form.email.data}).".encode('utf-8')

         with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls() 
            connection.login(user=my_email, password=my_password) 
            connection.sendmail(from_addr=my_email, to_addrs=my_email, 
                                msg=message)
            
         flash("Message Sent!")
         return redirect(url_for("contact"))
    return render_template("contact.html", form=form)


if __name__ == "__main__":
	app.run(debug=True) 
