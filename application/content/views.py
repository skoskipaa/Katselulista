from application import app, db
from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from application.content.models import Content
from application.content.forms import ContentForm

from application.lists.models import Watchlist 

@app.route("/content/<list_id>/new/")
@login_required
def content_form(list_id):
    li = Watchlist.query.filter_by(id=list_id).first()
    return render_template("content/new.html", form = ContentForm(), list_id=li.id)


@app.route("/content/<list_id>", methods=["GET"])
@login_required
def content_for_list(list_id):
    name = Watchlist.query.filter_by(id=list_id).first()
    item_name = name.name
    contentlist = Content.query.filter_by(watchlist_id = list_id).all()
    return render_template("content/list.html", contentlist = contentlist, name=item_name, list_id = list_id,
        watchlist_length = Content.total_length_of_a_watchlist(list_id))


@app.route("/content/<list_id>", methods=["POST"])
@login_required
def content_create(list_id):
    form = ContentForm(request.form)

    if not form.validate():
        return render_template("content/new.html", form = form, list_id=list_id)

    name = form.name.data
    length = form.length.data
    category = form.category.data
    cdn = form.cdn.data

    c = Content(name, length, category, cdn)
    c.watchlist_id = list_id

    db.session().add(c)
    db.session().commit()

    return redirect(url_for("content_for_list", list_id = list_id))