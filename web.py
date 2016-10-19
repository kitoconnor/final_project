import os
from flask import Flask, render_template, request
import giphypop
app = Flask(__name__)


@app.route('/')
def index(): #this needs to be right under the @app line
		return render_template('index.html')

@app.route('/about')
def about(): #this needs to be right under the @app line
	return render_template('about.html')

@app.route('/gifresults')
def results():
	#get keyword that is inputted on the webpage
	keyword = request.values.get('gif_keyword')
	#error handling if no keyword is entered
	if keyword == "": 
		header = "You didn't enter a keyword! Click below to try again."
		return render_template('gifresults.html',header=header)
	else:
		#setup giphy function 
		g = giphypop.Giphy()
		#set up list of results returned from giphy search using keyword and create a header to display at top of page
		results = g.search(keyword)
		if len(list(results)) == 0: header = "No results were found for the keyword ''{}''! Click below to try again.".format(keyword)
		else: header = "GIFs tagged with ''{}'':".format(keyword)
		#again grab the list of results, set up the page, passing along the giphy list, results, and the header string, header
		results = g.search(keyword)
		return render_template('gifresults.html',results=results,header=header)


port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)