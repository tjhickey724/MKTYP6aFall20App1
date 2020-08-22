"""
  website_demo shows how to use the Flask packages
  to create a simple website
"""

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
@app.route('/main')
def main():
	return render_template('index.html')


@app.route('/sandbox')
def sandbox():
	return render_template('sandbox.html')

@app.route('/about')
def about():
	return render_template('about.html')

if __name__ == '__main__':
    app.run('0.0.0.0',port=3000)
