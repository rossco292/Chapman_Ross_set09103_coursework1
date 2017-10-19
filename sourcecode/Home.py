from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route("/home")
def home():
  return render_template('home.html')

@app.route("/red")
def red():
  return render_template('red.html')

@app.route("/green")
def green():
  return render_template('green.html')

@app.route("/blue")
def blue():
  return render_template('blue.html')

@app.route("/black")
def black():
  return render_template('black.html')

@app.route("/white")
def white():
  return render_template('white.html')

@app.route("/creatures")
def creatures():
  return render_template('creatures.html')

@app.route("/land")
def land():
  return render_template('land.html')

@app.route("/spells")
def spells():
  return render_template('spells.html')









@app.errorhandler(404)
def page_not_found(error):
  return "Page was not found.", 404

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
