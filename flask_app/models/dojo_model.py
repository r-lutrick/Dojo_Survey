from flask_app.config.mysqlconnection import MySQLConnection
from flask_app import DATABASE
from flask import flash
import re


# Model for interacting with DB
class Dojo:
    # name
    # location
    # language
    # comment
    def __init__(self, data):
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']

    @classmethod
    def add(cls, data):
        query = """
            INSERT INTO dojos (name, location, language, comment)
            VALUES (%(name)s, %(location)s, %(language)s, %(comment)s)
        """
        return MySQLConnection(DATABASE).query_db(query, data)

    @staticmethod
    def validate(data):
        valid = True

        if not len(data['name']) > 0:
            flash("Name required", 'name')
            valid = False
        if not len(data['comment']) > 0:
            flash("Comment required", 'comment')
            valid = False

        return valid
