from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, Regexp, ValidationError
import re
from .models import User

class DataInventoryForm(FlaskForm):
    data_type = StringField('Data Type', validators=[DataRequired(), Length(max=100), Regexp(r'^[a-zA-Z0-9_ ]*$', message="Only alphanumeric characters and underscores are allowed.")])
    data_usage = StringField('Data Usage', validators=[DataRequired(), Length(max=200), Regexp(r'^[a-zA-Z0-9_ ]*$', message="Only alphanumeric characters and underscores are allowed.")])
    data_sharing = StringField('Data Sharing', validators=[DataRequired(), Length(max=200), Regexp(r'^[a-zA-Z0-9_ ]*$', message="Only alphanumeric characters and underscores are allowed.")])
    submit = SubmitField('Add Data')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=150), Regexp(r'^[a-zA-Z0-9_]*$', message="Only alphanumeric characters and underscores are allowed.")])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[
        DataRequired(),
        Length(min=8, message='Password must be at least 8 characters long'),
        Regexp(r'(?=.*[A-Z])', message='Password must contain at least one uppercase letter'),
        Regexp(r'(?=.*[a-z])', message='Password must contain at least one lowercase letter'),
        Regexp(r'(?=.*\d)', message='Password must contain at least one digit'),
        Regexp(r'(?=.*[@$!%*?&])', message='Password must contain at least one special character')
    ])
    submit = SubmitField('Register')

    def validate_password(self, field):
        password = field.data
        if not re.search(r'(?=.*[A-Z])', password):
            raise ValidationError('Password must contain at least one uppercase letter')
        if not re.search(r'(?=.*[a-z])', password):
            raise ValidationError('Password must contain at least one lowercase letter')
        if not re.search(r'(?=.*\d)', password):
            raise ValidationError('Password must contain at least one digit')
        if not re.search(r'(?=.*[@$!%*?&])', password):
            raise ValidationError('Password must contain at least one special character')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=150), Regexp(r'^[a-zA-Z0-9_]*$', message="Only alphanumeric characters and underscores are allowed.")])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField('Login')

class RequestResetForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError('There is no account with that email. You must register first.')

class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Reset Password')

class ComplianceRecordForm(FlaskForm):
    compliance_type = StringField('Compliance Type', validators=[DataRequired(), Length(max=100)])
    status = SelectField('Status', choices=[('Compliant', 'Compliant'), ('Non-Compliant', 'Non-Compliant')], validators=[DataRequired()])
    details = TextAreaField('Details', validators=[Length(max=500)])
    submit = SubmitField('Add Compliance Record')

