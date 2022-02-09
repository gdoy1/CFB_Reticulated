"""
NAME:          database\controllers.py
AUTHOR:        Alan Davies (Lecturer Health Data Science)
EMAIL:         alan.davies-2@manchester.ac.uk
DATE:          17/12/2019
INSTITUTION:   University of Manchester (FBMH)
DESCRIPTION:   Contains the Database class that contains all the methods used for accessing the database
"""

from sqlalchemy.sql import func
from flask import Blueprint

from app import db
from app.database.models import PrescribingData, PracticeData

database = Blueprint('dbutils', __name__, url_prefix='/dbutils')

class Database:
    """Class for managing database queries."""
    def get_total_number_items(self):
        """Return the total number of prescribed items."""
        return int(db.session.query(func.sum(PrescribingData.items).label('total_items')).first()[0])

    def get_avg_act_cost(self):
        """Return average cost."""
        return db.session.query(func.avg(PrescribingData.ACT_cost)).all()

    def get_prescribed_items_per_pct(self):
        """Return the total items per PCT."""
        return db.session.query(func.sum(PrescribingData.items).label('item_sum')).group_by(PrescribingData.PCT).all()

    def get_distinct_pcts(self):
        """Return the distinct PCT codes."""
        return db.session.query(PrescribingData.PCT).distinct().all()

    def get_max_item(self):
        """Return the maximum quantity item codes."""
        return db.session.query(PrescribingData.BNF_name, func.max(PrescribingData.quantity)).all()[0]

    def get_distinct_items(self):
        """Return the distinct item codes."""
        return db.session.query(PrescribingData.BNF_name).distinct().all()

    def get_n_data_for_PCT(self, pct, n):
        """Return all the data for a given PCT."""
        return db.session.query(PrescribingData).filter(PrescribingData.PCT == pct).limit(n).all()

    def get_percentage(self):
        """Return all the data for a given PCT."""
        totesum = int(db.session.query(func.sum(PrescribingData.quantity)).all()[0][0])
        methsum = int(db.session.query(func.max(PrescribingData.quantity)).all()[0][0])
        return round((methsum/totesum)*100, 2)

    def get_infection(self):
        """Return all the data for a given PCT."""
        return db.session.query(PrescribingData.BNF_code).filter(PrescribingData.BNF_code.startswith('05')).all()

    def get_bacteria(self):
        """Return all the data for a given PCT."""
        return db.session.query(PrescribingData.BNF_code).filter(PrescribingData.BNF_code.startswith('0501')).all()

    def get_fungal(self):
        """Return all the data for a given PCT."""
        return db.session.query(PrescribingData.BNF_code).filter(PrescribingData.BNF_code.startswith('0502')).all()

    def get_virus(self):
        """Return all the data for a given PCT."""
        return db.session.query(PrescribingData.BNF_code).filter(PrescribingData.BNF_code.startswith('0503')).all()

    def get_protozoa(self):
        """Return all the data for a given PCT."""
        return db.session.query(PrescribingData.BNF_code).filter(PrescribingData.BNF_code.startswith('0504')).all()

    def get_helminth(self):
        """Return all the data for a given PCT."""
        return db.session.query(PrescribingData.BNF_code).filter(PrescribingData.BNF_code.startswith('0505')).all()

    def get_bacteria_p(self):
        """Return all the data for a given PCT."""
        return round(len(db.session.query(PrescribingData.BNF_code).filter(PrescribingData.BNF_code.startswith('0501')).all()) / len(db.session.query(PrescribingData.BNF_code).filter(PrescribingData.BNF_code.startswith('05')).all()) * 100, 2)

    def get_fungal_p(self):
        """Return all the data for a given PCT."""
        return round(len(db.session.query(PrescribingData.BNF_code).filter(PrescribingData.BNF_code.startswith('0502')).all()) / len(db.session.query(PrescribingData.BNF_code).filter(PrescribingData.BNF_code.startswith('05')).all()) * 100, 2)

    def get_virus_p(self):
        """Return all the data for a given PCT."""
        return round(len(db.session.query(PrescribingData.BNF_code).filter(PrescribingData.BNF_code.startswith('0503')).all()) / len(db.session.query(PrescribingData.BNF_code).filter(PrescribingData.BNF_code.startswith('05')).all()) * 100, 2)

    def get_protozoa_p(self):
        """Return all the data for a given PCT."""
        return round(len(db.session.query(PrescribingData.BNF_code).filter(PrescribingData.BNF_code.startswith('0504')).all()) / len(db.session.query(PrescribingData.BNF_code).filter(PrescribingData.BNF_code.startswith('05')).all()) * 100, 2)

    def get_helminth_p(self):
        """Return all the data for a given PCT."""
        return round(len(db.session.query(PrescribingData.BNF_code).filter(PrescribingData.BNF_code.startswith('0505')).all()) / len(db.session.query(PrescribingData.BNF_code).filter(PrescribingData.BNF_code.startswith('05')).all()) * 100, 2)

    def creatinine_clearance(sex, age, weight, serum_creatinine):
        """Function to calculate creatinine clearance according to the Cockcroft-Gault equation
        Parameters:
            sex (string): F or M
            age (integer): Age of patient in years
            weight (integer): Weight of patient in kg
            serum_creatinine (integer): Serum creatinine in micromol/L
        Returns:
            creatinine clearance (mL/min)
        """

        if sex == "m":
            ccr = (((140 - age) * weight) / (serum_creatinine * 0.814))
        else:
            ccr = 0.85 * ((((140 - age) * weight) / (serum_creatinine * 0.814)))
        return ccr