from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Recipe:
    db_name = 'film_schema'

    def __init__(self,db_data):
        self.id = db_data['id']
        self.name = db_data['title']
        self.date_made = db_data['date_made']
        self.user_id = db_data['user_id']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']

    @classmethod
    def save(cls,data):
        query = "INSERT INTO films (title, date_made, user_id) VALUES (%(title)s,%(date_made)s,%(user_id)s);"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM films;"
        results =  connectToMySQL(cls.db_name).query_db(query)
        all_films = []
        for row in results:
            print(row['date_made'])
            all_films.append( cls(row) )
        return all_films

    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM films WHERE id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query,data)
        return cls( results[0] )

    @classmethod
    def update(cls, data):
        query = "UPDATE films SET title=%(title)s, date_made=%(date_made)s,updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query,data)

    @classmethod
    def delete(cls,data):
        query = "DELETE FROM films WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query,data)

    @staticmethod
    def validate_recipe(recipe):
        is_valid = True
        if len(recipe['title']) < 2:
            is_valid = False
            flash("Name must be at least 2 characters","film")
        if recipe['date_made'] == "":
            is_valid = False
            flash("Please enter a date","film")
        return is_valid
