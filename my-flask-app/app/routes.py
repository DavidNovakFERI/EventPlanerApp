from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import User
from . import db

bp = Blueprint('main', __name__)

@bp.route('/')
def home():
    users = User.query.all()  # Query all users
    return render_template('index.html', users=users)

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        # Check if the email already exists
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash('Email already registered. Please use a different email.', 'error')
            return redirect(url_for('main.register'))
        
        new_user = User(username=username, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
        
        return redirect(url_for('main.login'))
    return render_template('register.html')

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            # Handle successful login (e.g., set session, redirect to home)
            return redirect(url_for('main.home'))
        else:
            # Handle login failure (e.g., show error message)
            return render_template('login.html', error='Invalid username or password')
    return render_template('login.html')