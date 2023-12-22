from flask import Flask, render_template, request, redirect, url_for, flash, jsonify

app = Flask(__name__)

JOBS = [{
    'id': 1,
    "Name": "Data Scientist",
    "Location": "Bangaluru, India"
}, {
    'id': 2,
    "Name": "Data Analyst",
    "Location": "Delhi, India"
}, {
    'id': 3,
    "Name": "Data Scientist",
    "Location": "Remote, India"
}, {
    'id': 4,
    "Name": "Data Scientist",
    "Location": "NYC, USA"
}]


@app.route('/')
def hello_world():
  return render_template('home.html', jobs=JOBS)


@app.route('/about')
def about():
  return render_template('about.html')


@app.route('/jobs')
def jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
