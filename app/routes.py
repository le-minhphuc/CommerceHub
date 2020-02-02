from flask import render_template

from app import commerce_hub_app

@commerce_hub_app.route('/home')
def home():
    return render_template('home.html')

@commerce_hub_app.route('/register')
def register():
    return "This is /register view"

@commerce_hub_app.route('/login')
def login():
    return "This is /login view"

# TODO: how to capture item-id in a route?
@commerce_hub_app.route('/buy')
def buy():
    return "This is /buy view"

@commerce_hub_app.route('/sell/new')
def sell_new():
    return "This is /sell/new view"

@commerce_hub_app.route('/monitor/view')
def monitor_view():
    return "This is /monitor/view view"

@commerce_hub_app.route('/monitor/edit')
def monitor_edit():
    return "This is /monitor/edit view"

@commerce_hub_app.route('/admin/requests')
def admin_requests():
    return "This is /admin/requests view"

@commerce_hub_app.route('/collect/assigned')
def collect_assigned():
    return "This is /collect/assigned view"

@commerce_hub_app.route('/collect/completed')
def collect_completed():
    return "This is /collect/completed view"