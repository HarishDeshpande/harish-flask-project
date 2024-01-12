from flask import Flask

app = Flask(__name__)

# "/" for the default page or empty page
@app.route("/")
def hello_world():
  return "Namaste Harish"

# here if the script is invoked using the python command
# then the app will be run
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
