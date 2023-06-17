from flask import Blueprint, render_template, request, flash, redirect, url_for;
from .models import User, Record;
from werkzeug.security import generate_password_hash, check_password_hash;
from . import db;
from datetime import datetime;

auth = Blueprint('auth',__name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        Username = request.form.get('username').title().strip()
        Password = request.form.get('password')

        user = User.query.filter_by(username=Username).first()
        if user:
            if check_password_hash(user.password, Password):
                flash('Login Successfully...', category='success')
                return redirect(url_for('auth.create_po'))
            else:
                flash('Wrong password entered..', category='error')
        else:
            flash('Username does not exists',category='error')
    return render_template('login.html')
    

@auth.route('/logout')
def logout():
    return render_template('logout.html')

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        FirstName = request.form.get('firstname').title().strip()
        LastName = request.form.get('lastname').title().strip()
        Username = request.form.get('username').title().strip()
        Password = request.form.get('password')

        user = User.query.filter_by(username=Username).first()
        if user:
            flash('Username Alredy Exists...',category='error')
        elif len(FirstName) < 3:
            flash('Firstname must be greater than 2 characters',category='error')
        elif len(LastName) < 3:
            flash('Lastname must be greater than 2 characters',category='error')
        elif len(Username) < 4:
            flash('Username must be greater than 3 characters',category='error')
        elif len(Password) < 5:
            flash('Password must be greater than 4 characters',category='error')
        else:
            try:
                new_user = User(first_name=FirstName,username=Username,last_name=LastName,password=generate_password_hash(Password, method='sha256'))
                db.session.add(new_user)
                db.session.commit()
                flash('Account Created Successfully!',category='success')
                return redirect(url_for('views.home'))
            except:
                flash('An Error occured while creating the user')
           
        
    return render_template('signup.html')


@auth.route('/create_po',methods=['GET', 'POST'])
def create_po():
    if request.method == 'POST':
        PO_NUM = request.form.get('po_num').title().strip()
        INV_NUM = request.form.get('inv_num').title().strip()
        INV_DATE = datetime.strptime(request.form.get('inv_date'),'%Y-%m-%d').date()
        DUE_DATE = datetime.strptime(request.form.get('due_date'),'%Y-%m-%d').date()
        try:
            new_record= Record(po_number=PO_NUM,invoice_number=INV_NUM,invoice_date=INV_DATE,due_date=DUE_DATE)
            db.session.add(new_record)
            db.session.commit()
            flash('PO Details Successfully Added...',category='success')
            return redirect(url_for('auth.create_po'))
        except:
            flash('There was an error while adding the PO...',category='error')
       
    
    return render_template('create_po.html')
