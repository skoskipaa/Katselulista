from application import app, db
from application.lists.models import Watchlist
from application.lists.forms import ListForm
from application.lists.forms import EditForm

from application.content.models import Content

from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

@app.route("/lists", methods=["GET"])
@login_required
def lists_index():
    lists = Watchlist.query.filter_by(account_id=current_user.id).all()
    return render_template("lists/list.html", lists = lists, total_length=Content.total_length_for_a_user(current_user.id))


@app.route("/lists/new/")
@login_required
def lists_form():
    return render_template("lists/new.html", form = ListForm())

@app.route("/lists/", methods=["POST"])
@login_required
def lists_create():
    form = ListForm(request.form)

    if not form.validate():
        return render_template("lists/new.html", form = form)

    l = Watchlist(form.name.data)
    l.account_id = current_user.id

    db.session().add(l)
    db.session().commit()

    return redirect(url_for("lists_index"))
    
@app.route("/lists/<list_id>/edit", methods=["GET", "POST"])
@login_required
def lists_update(list_id):
    l = Watchlist.query.get(list_id)
    
    if request.method == "GET":
        return render_template("lists/edit.html", form = EditForm(), list_id=list_id, name = l.name)

    if request.method == "POST":
        form = EditForm(request.form)

        if not form.validate():
            return render_template("lists/edit.html", form = form)

        l.name = form.name.data

        db.session().add(l)
        db.session().commit()

        return redirect(url_for("content_for_list", list_id=list_id))


