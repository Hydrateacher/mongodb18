from flask import Flask, render_template, redirect, url_for, session, request
from pymongo import MongoClient
import requests
from uuid import uuid4 
# MongoDB-ga bog'lanish
client = MongoClient('mongodb+srv://doadmin:56Hx14L97FMUYv23@db-mongodb-fra1-82504-ec7e84b0.mongo.ondigitalocean.com/admin?tls=true&authSource=admin&replicaSet=db-mongodb-fra1-82504')
db = client['NEW']
collection = db['kun']


app = Flask(__name__)
app.secret_key = 'supersecretkey'




@app.route('/')
def index():    
    return render_template('index.html')

# database
@app.route('/mongodb', methods=['GET', 'POST'])
def mongodb():
    if request.method == 'POST':
        kun = request.form.get('kun')
        harorat = request.form.get('harorat')      
        
        if kun  and harorat:
            collection.insert_one({'kun': kun, 'harorat': harorat})
            
            render_template('mongodb.html')        
        
    # Ma'lumotlarni olish
    records = list(collection.find({}))
    
    # Ma'lumotlarni HTML sahifasiga uzatish
    return render_template('mongodb.html', records=records)



  
  

if __name__ == '__main__':
    app.run(debug=True)



