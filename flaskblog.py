from flask import Flask, render_template, url_for, redirect
app = Flask(__name__)

list1 = [
  {
  		'author':'Prashanth',
  		'title' : 'Blog Post-1',
  		'content' : 'First post content',
  		'date_posted' : 'April 24,2001'
  },

  {
  		'author':'Mothishwaran',
  		'title' : 'Blog Post-2',
  		'content' : 'Second post content',
  		'date_posted' : 'June 13,2019'
  }
]

@app.route("/")
@app.route("/home")
def home():
	return render_template('home.html',posts=list1)

@app.route("/about")
def about():
	return render_template('about.html')

# @app.route("/<name>")
# def user(name):
# 	return f"Hello {name} You are in {name}'s Page! Try again later"

# @app.route("/admin")
# def admin():
# 	return redirect(url_for("user", name="Prashanth"))

if __name__ == "__main__":
	app.run(debug=True)






