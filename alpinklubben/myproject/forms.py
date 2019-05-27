###################
##### imports #####
###################
#!/usr/bin/env python3

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, RadioField, DateField
from wtforms.validators import DataRequired, Email, EqualTo, Required
from wtforms import ValidationError
from myproject.models import User

#################
##### Forms #####
#################

class RegisterForm(FlaskForm):

    username = StringField("Brukernavn: ", validators = [DataRequired()])
    name = StringField("Fult navn:", validators = [DataRequired()])
    email = StringField("E-post: ", validators = [DataRequired(), Email()])
    password = PasswordField("Passord: ", validators = [DataRequired()])
    submit_form = SubmitField("Registrer")

    # Check if the email is already in use
    def check_email(self, field):
        if User.query.filter_by(email=field.data).first():
            # Dersom den allerede er registrert, får brukeren en denne meldingen.
            raise ValidationError('Eposten din har allerede blitt brukt!')

class LoginForm(FlaskForm):
    username = StringField("Brukernavn:", validators = [DataRequired()])
    password = PasswordField("Passord: ", validators = [DataRequired()])
    submit = SubmitField("Logg inn")

class OrderPackage(FlaskForm):
    package = RadioField("Vennligst velg pakken du ønsker å bestille",
                            choices = [('Single', 'Single-pakke'), ('Duo','Duo-Pakke'),
                            ('Trio', 'Trio-pakke'), ('Quad','Quad-Pakke'),
                            ('Penta', 'Penta-pakke'), ('Custom','Custom-Pakke')])
    #date = DateField("Fyll inn ønsket leiedato: ", validators = [Required()], render_kw={"placeholder": "Eks. 01.01.2020"})
    date = StringField("Fyll inn ønsket leiedato: ", validators = [DataRequired()], render_kw={"placeholder": "Eks. 01.01.2020"})
    submit = SubmitField("Bestill")
