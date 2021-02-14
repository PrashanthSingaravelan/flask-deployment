from flask import Flask,render_template,request,url_for,redirect,session
app = Flask(__name__)
app.secret_key = "Poda"  # sessions are always encrypted on the server

@app.route("/")
@app.route("/home")
def home():
	return render_template('home.html')

@app.route("/login",methods=["POST","GET"])
def login():
	if request.method == "POST":
		user = request.form['nm']
		session['user'] = user    # session stores the data as a dictionary 
		return redirect(url_for("user"))

	elif request.method == "GET":
		if "user" in session:
			return redirect(url_for("user"))

		return render_template("login.html")

@app.route("/user")
def user():
	if "user" in session: 
		user = session['user']   # retrieving the data from the session
		return f"<h1>{user} you are so lucky </h1> "
	else:    # if the user doesn't login in to website/leave the website,the user can once again login
		return redirect(url_for('user'))

@app.route("/logout")
def logout():
	session.pop("user",None)   			# Clears all the session data's
	return redirect(url_for("login"))   # after clearing, it will redirect to the login page once again

if __name__=="__main__":
	app.run(debug=True)


# Sessions are temporary and they are stored on the web-server and not stored on the client side.
# For quick access of information and to pass stuffs around the server.
# Each and every time we have to create a new session and login again.