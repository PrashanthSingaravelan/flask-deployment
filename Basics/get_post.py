from flask import Flask, render_template, url_for, redirect, request
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
	return render_template("home.html")

@app.route("/login", methods=["POST","GET"])
def login():
	if request.method == "GET":
		return render_template("login.html")
	elif request.method == "POST":
		user = request.form["nm"]    			# Form of a dictionary
		return redirect(url_for("user", usr=user))
		
@app.route("/<usr>")
def user(usr):
	return f"<h1> {usr} you are so lucky</h1>"

if __name__=="__main__":
	app.run(debug=True)


