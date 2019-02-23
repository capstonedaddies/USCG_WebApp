from django.shortcuts import render, redirect
import pyrebase

# Create your views here.

config = {
    'apiKey': "AIzaSyCiXxfNGJ4udL-zC42djLH5yaKMUo5kwEM",
    'authDomain': "uscg-responder.firebaseapp.com",
    'databaseURL': "https://uscg-responder.firebaseio.com",
    'projectId': "uscg-responder",
    'storageBucket': "uscg-responder.appspot.com",
    'messagingSenderId': "181260395230"
}
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

def index(request):
    return render(request, "index.html")

def postsign(request):
    email = request.POST.get('email')
    password = request.POST.get("pass")

    user = auth.sign_in_with_email_and_password(email, password)

    return render(request, "welcome.html", {"e":email})


