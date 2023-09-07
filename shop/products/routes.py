from flask import redirect, render_template, url_for, flash, request
from shop import db, app
from .models import Brand, Category
from .forms import Addproducts
import secrets 

@app.route('/addbrand', methods=['GET', 'POST'])
def addbrand():
    if request.method=='POST':
        getbrand = request.form.get('brand')
        brand = Brand(name=getbrand)
        db.session.add(brand) 
        flash(f'The Brand {getbrand} was added to your databse', 'success')
        db.session.commit()
        return redirect(url_for('addbrand'))
    
    return render_template('products/addbrand.html', brands='brands')

@app.route('/addcat', methods=['GET', 'POST'])
def addcat():
    if request.method=='POST':
        getbrand = request.form.get('category')
        cat = Category(name=getbrand)
        db.session.add(cat)
        flash(f'The Category {getbrand} was added to your databse', 'success')
        db.session.commit()
        return redirect(url_for('addcat'))
    
    return render_template('products/addbrand.html')

@app.route('/Addproduct', methods=['GET', 'POST'])
def addproduct():
    form = Addproducts(request.form)
    return render_template('products/addproduct.html', title='Add Product Page', form=form)