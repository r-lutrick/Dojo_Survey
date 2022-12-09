from flask import Flask
app = Flask(__name__)
app.secret_key = "No secrets here..."

DATABASE = 'dojo_survey_schema'
