from flask import Flask,render_template, request
import pyrebase

config = {                              #paste your details here
    "apiKey": "*****************",
    "authDomain": "***************",
    "databaseURL": "********",
    "projectId": "**********",
    "storageBucket": "*******",
    "messagingSenderId": "*********",
    "appId": "************",
    "measurementId": "**************"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()
app = Flask(__name__)

@app.route("/",methods = ['GET', 'POST'])  #---------push data-------#
def pushdata():
    if (request.method == 'POST'):
        name = request.form.get('name')
        age = request.form.get('age')
        db.child("names").set(              #(.set) is used to create your own keys. whereas (.push) is used to create auto generated timestamp based keys.
            {
                "name": name,
                "age": age
            })
        status = "Data Submitted"
    return render_template('index.html',status = status)

@app.route("/update")  #---------update data-------#
def update():
    db.child("names").update({"name": "pundir"})
    return render_template('update.html')
                            
@app.route("/delete")  #---------delete data-------#
def delete():
    db.child("names").remove()
    return render_template('delete.html')

app.run(debug=True)
