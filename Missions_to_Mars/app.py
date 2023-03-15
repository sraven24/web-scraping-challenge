from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

#create flask instance
app = Flask(__name__)

#establish link to mongo database
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

@app.route("/")
def home():
    
    # find one document from our mongo db and return it.
    mars_data = mongo.db.mars.find_one()
    
    # pass that listing to render_template
    return render_template("index.html", marsspecs=mars_data)

# set our path to trigger our scrape
@app.route("/scrape")
def scrape():
    
    #Run the scrap function
    mars_data = scrape_mars.scrape_info()

    # Update the Mongo database 
    mongo.db.mars.update_one({},{"$set": mars_data}, upsert = True)

    return redirect("/", code=302)





if __name__ == "__main__":
    app.run(debug=True)