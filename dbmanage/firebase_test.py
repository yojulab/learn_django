# Set Firebase with Authentication and Database
# https://www.juso.go.kr/addrlink/devAddrLinkRequestSubmit.do
# 승인키	devU01TX0FVVEgyMDIwMDgxOTE2MjYxMzExMDA4MDE=
import pyrebase

firebaseConfig = {
  'apiKey': "",
  'authDomain': "project-good.firebaseapp.com",
  'databaseURL': "https://project-good.firebaseio.com",
  'projectId': "project-good",
  'storageBucket': "project-good.appspot.com",
  'messagingSenderId': "237303631829",
  'appId': "1:237303631829:web:73578648e98c836346f75c",
  'measurementId': "G-5S3EKQ46F7"
}

firebase = pyrebase.initialize_app(firebaseConfig)

# Get a reference to the auth service
auth = firebase.auth()

# Log the user in
email = 'test_user@test.org'
password = 'test_user'
user = auth.sign_in_with_email_and_password(email, password)

# Get a reference to the database service
db = firebase.database()

# db.child("test_users01").child("Morty")

# data to save
data = {
    "name": "Mortimer 'Morty' Smith"
}

# Pass the user's idToken to the push method
results = db.child("users").push(data, user['idToken'])

print(results)