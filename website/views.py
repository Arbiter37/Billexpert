from flask import Blueprint, render_template   #this file is basically a blueprint of our website having various routes and links
from flask_login import login_required, current_user
from flask_sqlalchemy import SQLAlchemy
from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User, Uploaded
from werkzeug.security import generate_password_hash, check_password_hash
from . import db 
from flask_login import login_user, login_required, logout_user, current_user



views = Blueprint('views', __name__)



@views.route('/', methods=['GET', 'POST'])   
@login_required
def home():                 # for different route we can use /something to lead to that page.
    return render_template("home.html", user=current_user)

@views.route('/upload', methods=['GET','POST'])
@login_required
def upload():
    if request.method == 'POST':
        file = request.file['file']
        print('yes')

        upload = Uploaded(filename=file.filename, data=file.read())
        db.session.add(upload)
        db.session.commit()

        flash('File uploaded successfully!', category='success')
        
    
        

    return render_template("upload.html", user=current_user)

@views.route('/info', methods=['GET', 'POST'])   
@login_required
def info():                 
    return render_template("info.html", user=current_user)