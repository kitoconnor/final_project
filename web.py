from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index(): #this needs to be right under the @app line
	return render_template('index.html')

app.run(debug=True)