
from flask import Blueprint, render_template, url_for, redirect
# from app import db, app
import base64

from wtforms.form import Form

# from app.models import Item, Post, Project
# from app.site.forms import SearchForm

bp = Blueprint("site", __name__)

@bp.route('/', methods=['POST', 'GET'])
def index():
    return render_template("index.html")