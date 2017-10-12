from flask import Flask
app = Flask(__name__)

@app.route("/home")
def home():
  return "Welcome to the Magic The Gathering collection"

@app.route("/colours")
def colours():
  return "This page is about the different colours and their attribuits"

@app.route("/card_types")
def cardtypes():
  return "There are many cardtypes in magic and here is information on all \
  of the different ones"

@app.route("/basics")
def basics():
  return "This page is all about the basics of the game"







@app.errorhandler(404)
def page_not_found(error):
  return "Page was not found.", 404

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
