from flask import Blueprint, render_template, request, flash, redirect, url_for;
from .models import Record;
from . import db;
from datetime import datetime;

auth = Blueprint('auth',__name__)

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
