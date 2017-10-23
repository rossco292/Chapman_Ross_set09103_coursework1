from flask import Flask, render_template, url_for
app = Flask(__name__)#This is where we gather the methods for use in this app 

@app.route("/home")#This is the path for the home page
def home():
  return render_template('home.html')#This is where we call/use the templates

@app.route("/red")
def red():
  return render_template('red.html')#""

@app.route("/green")
def green():
  return render_template('green.html')#""

@app.route("/blue")
def blue():
  return render_template('blue.html')#""

@app.route("/black")
def black():
  return render_template('black.html')#""

@app.route("/white")
def white():
  return render_template('white.html')#""

@app.route("/creatures")
def creatures():
  return render_template('creatures.html')#""

@app.route("/land")
def land():
  return render_template('land.html')#""

@app.route("/spells")
def spells():
  return render_template('spells.html')#""

@app.errorhandler(404)#This is so the user gets an understandable error
def page_not_found(error):
  return "Page was not found.", 404#This replaces the error with this text

if __name__ == "__main__":#This runs the app on host '0.0.0.0'
  app.run(host='0.0.0.0', debug=True)#The debug allows for changes to be made
  #while the app is running 
