''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
# Import Flask, render_template, request from the flask pramework package : TODO
from flask import Flask,render_template,request
import json
import sentiment_analysis
# Import the sentiment_analyzer function from the package created: TODO
from sentiment_analysis import keyword_finder, text_summarizer
#Initiate the flask app : TODO
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/keyword_finder", methods=["POST","GET"])
def keyword_finder():
    if request.method == "GET":
        return render_template("keyword_finder.html")
    else:
        text = request.form['text']
        lang = request.form['lang']
        response = sentiment_analysis.keyword_finder(str(text),str(lang))
        # Parse the JSON data
        data = json.loads(response)

        # Extract keywords and their importance
        items = data['ibm']['items']
        sorted_items = sorted(items, key=lambda x: x['importance'], reverse=True)

        # Get the first 3 most important keywords and their importance
        most_important = sorted_items[:3]

        # Get the last 3 least important keywords and their importance
        least_important = sorted_items[-3:]

        return  most_important, least_important
@app.route("/text_summarizer", methods=["POST", "GET"])
def text_summarizer():
    if request.method == "GET":
        return render_template("text_summarizer.html")
    else:
        text = request.form['text']
        response = sentiment_analysis.text_summarizer(str(text))
        # Parse the JSON data
        data = json.loads(response)
        # Access the result value
        result = data['alephalpha']['result']
        return result



if __name__ == "__main__":
    app.run(debug="True")

