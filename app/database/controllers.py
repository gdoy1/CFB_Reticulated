"""
NAME:          database\controllers.py
AUTHOR:        Alan Davies (Lecturer Health Data Science)
EMAIL:         alan.davies-2@manchester.ac.uk
DATE:          17/12/2019
INSTITUTION:   University of Manchester (FBMH)
DESCRIPTION:   Contains the Database class that contains all the methods used for accessing the database
"""

from sqlalchemy.sql import func
from sqlalchemy.sql import desc
from flask import Blueprint

from app import db
from app.database.models import PrescribingData, PracticeData

database = Blueprint('dbutils', __name__, url_prefix='/dbutils')

class Database:
    """Class for managing database queries."""
    def get_total_number_items(self):
        """Return the total number of prescribed items."""
        return int(db.session.query(func.sum(PrescribingData.items).label('total_items')).first()[0])

    def get_prescribed_items_per_pct(self):
        """Return the total items per PCT."""
        return db.session.query(func.sum(PrescribingData.items).label('item_sum')).group_by(PrescribingData.PCT).all()

    def get_distinct_pcts(self):
        """Return the distinct PCT codes."""
        return db.session.query(PrescribingData.PCT).distinct().all()

    def get_n_data_for_PCT(self, pct, n):
        """Return all the data for a given PCT."""
        return db.session.query(PrescribingData).filter(PrescribingData.PCT == pct).limit(n).all()

    def get_max_quantity(self):
        """Find item with the maximum summed quantity"""
        return db.session.query(PrescribingData.BNF_name, func.sum(PrescribingData.quantity)).group_by(PrescribingData.BNF_name).order_by(desc(func.sum(PrescribingData.quantity))).limit(1).all()

    def find_max_quantity_percentage(self):
        """Get the item with the maximum quantity as a percentage of all prescription"""
        max_quantity = db.session.query(func.sum(PrescribingData.quantity)).group_by(PrescribingData.BNF_name).order_by(desc(func.sum(PrescribingData.quantity))).limit(1).all()[0][0]
        all_quantities = db.session.query(func.sum(PrescribingData.quantity)).all()
        return float(int((max_quantity) / int(all_quantities)) * 100)