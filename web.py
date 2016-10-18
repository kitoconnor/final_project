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
	#create a string for the header to display at the top of the search page
	header = "GIF's tagged with ''{}'':".format(keyword)
	#setup giphy function 
	g = giphypop.Giphy()
	#set up list of results returned from giphy search using keyword
	results = g.search(keyword)
	#set up the page, passing along the giphy list, results, and the header string, header
	return render_template('gifresults.html',results=results,header=header)


app.run(debug=True)