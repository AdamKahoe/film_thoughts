from flask import render_template,redirect,session,request, flash
from flask_app import app
from flask_app.models.film import Film
from flask_app.models.user import User


@app.route('/new/film')
def new_film():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":session['user_id']
    }
    return render_template('new_film.html',user=User.get_by_id(data))


@app.route('/create/film',methods=['POST'])
def create_recipe():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Film.validate_film(request.form):
        return redirect('/new/film')
    data = {
        "title": request.form["title"],
        "date_made": request.form["date_made"],
        "info": request.form["info"],
        "user_id": session["user_id"]
    }
    Film.save(data)
    return redirect('/dashboard')

@app.route('/edit/film/<int:id>')
def edit_recipe(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    user_data = {
        "id":session['user_id']
    }
    return render_template("edit_film.html",edit=Film.get_one(data),user=User.get_by_id(user_data))

@app.route('/update/film',methods=['POST'])
def update_film():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Film.validate_film(request.form):
        return redirect('/new/film')
    data = {
        "title": request.form["title"],
        "date_made": request.form["date_made"],
        "info": request.form["info"],
        "id": request.form['id']
    }
    Film.update(data)
    return redirect('/dashboard')

@app.route('/recipe/<int:id>')
def show_film(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    user_data = {
        "id":session['user_id']
    }
    return render_template("show_film.html",film=Film.get_one(data),user=User.get_by_id(user_data))

@app.route('/delete/film/<int:id>')
def delete_film(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    Film.delete(data)
    return redirect('/dashboard')