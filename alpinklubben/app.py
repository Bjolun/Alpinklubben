###################
##### Imports #####
###################
#!/usr/bin/env python3

from myproject import app, db
from flask import render_template, url_for, redirect, session
from myproject.forms import RegisterForm, LoginForm, OrderPackage
from myproject.models import User, Orders


############################
##### Views with forms #####
############################

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/utleie')
def packages():

    return render_template('lei_utstyr.html')

@app.route('/omoss')
def about():
    return render_template('omoss.html')

@app.route('/bestill', methods = ['GET', 'POST'])
def order():

    form = OrderPackage()
    if form.validate_on_submit():
        order = Orders(package = form.package.data,
                    user_ordered=session['brukernavn'],
                    date = form.date.data)
        db.session.add(order)
        db.session.commit()
        return redirect(url_for('my_page'))

    return render_template('bestill.html', form = form)

@app.route('/minside', methods=['GET', 'POST'])
def my_page():
    order = Orders.query.filter_by(user_ordered=session['brukernavn'])
    user = User.query.filter_by(username=session['brukernavn']).first()
    return render_template('min_side.html', user = user, order = order)

@app.route('/logginn', methods=['GET', 'POST'])
def login():


    # SJEKK HELE DENNE!
    form = LoginForm()
    if form.validate_on_submit():
        # Går inn i databasen og sjekker om det finnes en bruker med brukernavnet som blir skrevet inn
        # i tekstfeltet. Henter all informasjon om brukeren.
        user = User.query.filter_by(username=form.username.data).first()
        # Denne er tricky, men skal prøve å forklare
        if user.password == form.password.data:
            # Setter navnet 'brukernavn' i session til å bli lik user sin username.
            # Denne linja MÅ vi ha for å få satt opp login
            # Etter man skriver denne kan vi bruke denne slik som vi f.eks gjør i view´en til minside
            # slik at vi kan printe ut i
            session['brukernavn'] = user.username
            return redirect(url_for('my_page'))


    return render_template('login.html', form = form)

@app.route('/registrer', methods =['GET', 'POST'])
def register():

    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username = form.username.data,
                    name = form.name.data,
                    email = form.email.data,
                    password = form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))



    return render_template('register.html', form = form)

@app.route('/logout', methods = ['GET', 'POST'])
def logout():

    # Sletter session, og logger med det brukeren ut av siden.
    del session['brukernavn']

    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
