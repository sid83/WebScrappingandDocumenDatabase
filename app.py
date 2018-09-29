# import necessary libraries
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import mars_scrape

# create instance of Flask app
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_db1"
mongo = PyMongo(app)

# create route that renders index.html template and finds documents from mongo
@app.route("/")
def home():

    # Find data
    marsinfo = mongo.db.info_about_mars2.find()

    # return template and data
    return render_template("index1.html", marsinfo=marsinfo)
    
# create a route that will trigger the scrape function
@app.route("/scrape")
def scrape_data():
  # Run scraped function
    mars_data = mars_scrape.mars_scrape()

    # drop "info_about_mars2" collection if exists
    mongo.db.info_about_mars2.drop()

    # Insert mars data into database
    mongo.db.info_about_mars2.insert_one(mars_data)

    # Redirect back to home page
    return redirect("http://localhost:5000/", code=302)

if __name__ == "__main__":
    app.run(debug=True)
