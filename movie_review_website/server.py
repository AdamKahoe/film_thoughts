from flask_app import app

from flask_app.controllers import users, films
from flask_app.models import user, film

if __name__=="__main__":
    app.run(debug=True)