from django.shortcuts import render, redirect
from .keys import ApiKeys
import pyrebase

# Create your views here.
authKey = ApiKeys.authKey
mapKey = ApiKeys.mapsKey

config = {
    # contact sean for keys.py file
    'apiKey': authKey,
    'authDomain': "uscg-responder.firebaseapp.com",
    'databaseURL': "https://uscg-responder.firebaseio.com",
    'projectId': "uscg-responder",
    'storageBucket': "uscg-responder.appspot.com",
    'messagingSenderId': "181260395230"
}
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
database = firebase.database()

def noquote(s):
    return s

def index(request):
    return render(request, "index.html")


def postsign(request):
    pyrebase.pyrebase.quote = noquote
    email = request.POST.get('email')
    password = request.POST.get("pass")
    db = database.child("uscg-responder").child("user_locations").child("bobbyBoater").get()
    #print(db.key())

    user = auth.sign_in_with_email_and_password(email, password)
    return render(request, "welcome.html", {"e": email, "mk": mapKey, "db": db.key})



    
