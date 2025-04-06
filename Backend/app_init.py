from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

# Enable CORS for frontend domain
CORS(app, origins=["https://strangeabhi.github.io"], supports_credentials=True)

# Use the original secret key
app.secret_key = "Abhi2705"

# MongoDB config (make sure this URI is correct for your local setup)
app.config["MONGO_URI"] = "mongodb://localhost:27017/hotelbooking"
