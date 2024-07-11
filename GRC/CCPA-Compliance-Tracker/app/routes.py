from flask import Blueprint, render_template, redirect, url_for, request, flash
from .models import db, DataInventory, User, ComplianceRecord
from .forms import DataInventoryForm, RegistrationForm, LoginForm, RequestResetForm, ResetPasswordForm, ComplianceRecordForm
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from . import limiter, mail, serializer
from flask_mail import Message

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
@login_required
def home():
    form = DataInventoryForm()
    if form.validate_on_submit():
        new_data = DataInventory(
            data_type=form.data_type.data,
            data_usage=form.data_usage.data,
            data_sharing=form.data_sharing.data
        )
        db.session.add(new_data)
        db.session.commit()
        return redirect(url_for('main.home'))
    data_inventory = DataInventory.query.all()
    return render_template('home.html', form=form, data_inventory=data_inventory)

@main.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='pbkdf2:sha256')
        new_user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('main.login'))
    return render_template('register.html', form=form)

@main.route('/login', methods=['GET', 'POST'])
@limiter.limit("5 per minute")
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('main.home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', form=form)

@main.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.login'))

@main.route('/edit/<int:data_id>', methods=['GET', 'POST'])
@login_required
def edit(data_id):
    data = DataInventory.query.get_or_404(data_id)
    form = DataInventoryForm()
    if form.validate_on_submit():
        data.data_type = form.data_type.data
        data.data_usage = form.data_usage.data
        data.data_sharing = form.data_sharing.data
        db.session.commit()
        return redirect(url_for('main.home'))
    elif request.method == 'GET':
        form.data_type.data = data.data_type
        form.data_usage.data = data.data_usage
        form.data_sharing.data = data.data_sharing
    return render_template('edit.html', form=form, data_id=data.id)

@main.route('/delete/<int:data_id>', methods=['POST'])
@login_required
def delete(data_id):
    data = DataInventory.query.get_or_404(data_id)
    db.session.delete(data)
    db.session.commit()
    return redirect(url_for('main.home'))

@main.route('/compliance/<int:data_id>', methods=['GET', 'POST'])
@login_required
def compliance(data_id):
    data = DataInventory.query.get_or_404(data_id)
    form = ComplianceRecordForm()
    if form.validate_on_submit():
        new_compliance = ComplianceRecord(
            data_id=data.id,
            compliance_type=form.compliance_type.data,
            status=form.status.data,
            details=form.details.data
        )
        db.session.add(new_compliance)
        db.session.commit()
        return redirect(url_for('main.compliance', data_id=data.id))
    compliance_records = ComplianceRecord.query.filter_by(data_id=data.id).all()
    return render_template('compliance.html', form=form, compliance_records=compliance_records, data=data)

@main.route('/edit_compliance/<int:compliance_id>', methods=['GET', 'POST'])
@login_required
def edit_compliance(compliance_id):
    compliance_record = ComplianceRecord.query.get_or_404(compliance_id)
    form = ComplianceRecordForm()
    if form.validate_on_submit():
        compliance_record.compliance_type = form.compliance_type.data
        compliance_record.status = form.status.data
        compliance_record.details = form.details.data
        db.session.commit()
        return redirect(url_for('main.compliance', data_id=compliance_record.data_id))
    elif request.method == 'GET':
        form.compliance_type.data = compliance_record.compliance_type
        form.status.data = compliance_record.status
        form.details.data = compliance_record.details
    return render_template('edit_compliance.html', form=form, compliance_record=compliance_record)

@main.route('/delete_compliance/<int:compliance_id>', methods=['POST'])
@login_required
def delete_compliance(compliance_id):
    compliance_record = ComplianceRecord.query.get_or_404(compliance_id)
    data_id = compliance_record.data_id
    db.session.delete(compliance_record)
    db.session.commit()
    return redirect(url_for('main.compliance', data_id=data_id))

@main.route('/reset_password', methods=['GET', 'POST'])
def reset_request():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RequestResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            send_reset_email(user)
        flash('An email has been sent with instructions to reset your password.', 'info')
        return redirect(url_for('main.login'))
    return render_template('reset_request.html', form=form)

@main.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    try:
        email = serializer.loads(token, salt='password-reset-salt', max_age=3600)
    except:
        flash('That is an invalid or expired token', 'warning')
        return redirect(url_for('main.reset_request'))
    user = User.query.filter_by(email=email).first_or_404()
    form = ResetPasswordForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='pbkdf2:sha256')
        user.password = hashed_password
        db.session.commit()
        flash('Your password has been updated! You are now able to log in', 'success')
        return redirect(url_for('main.login'))
    return render_template('reset_token.html', form=form)

def send_reset_email(user):
    token = serializer.dumps(user.email, salt='password-reset-salt')
    msg = Message('Password Reset Request',
                  sender='noreply@demo.com',
                  recipients=[user.email])
    link = url_for('main.reset_token', token=token, _external=True)
    msg.body = f'''To reset your password, visit the following link:
{link}
If you did not make this request then simply ignore this email and no changes will be made.
'''
    mail.send(msg)

