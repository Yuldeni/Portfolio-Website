from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

app = Flask(__name__) #Es el archivo actual (main)
Bootstrap5(app)
app.config['SECRET_KEY'] = "Contraseña123"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/portfolio")
def portfolio():
    return render_template("service-details.html")

@app.route("/learnings")
def learnings():
    return render_template("starter-page.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
	app.run(debug=True) 
