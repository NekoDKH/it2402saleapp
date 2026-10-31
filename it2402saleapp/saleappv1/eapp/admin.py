from flask_admin.contrib.sqla import ModeView

from eapp import app, db
from flask_admin import Admin
from eapp.models import Category, Product

admin = Admin(app=app, name="E-commerce's Admin")
admin.add_view(ModeView(Category, db.session))
admin.add_view(ModeView(Product, db.session))