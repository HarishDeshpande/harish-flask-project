from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Mumbai, India',
    'salary': 'Rs. 10,00,000'
}, {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Delhi, India',
    'salary': 'Rs. 15,00,000'
}, {
    'id': 3,
    'title': 'Frontend Engineer',
    'location': 'Remote',
    'salary': 'Rs. 12,00,000'
}, {
    'id': 4,
    'title': 'Backend Engineer',
    'location': 'San Francisco, USA',
    'salary': '$150,000'
}]


# "/" for the default page or empty page
@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS, company_name='Harish')


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


# here if the script is invoked using the python command
# then the app will be run
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
