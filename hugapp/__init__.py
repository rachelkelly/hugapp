from flask import Flask

app = Flask(__name__)
from hugapp import views
