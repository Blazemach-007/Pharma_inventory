from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
import random
import string
import uuid

db = SQLAlchemy()


def generate_random_id():
    return str(uuid.uuid4())


class DoctorDetails(db.Model):
    __tablename__ = 'doctor_details'
    doctor_id = db.Column(db.Integer, primary_key=True)
    doctor_name = db.Column(db.String(255), nullable=False)
    specialization = db.Column(db.String(255))
    license_number = db.Column(db.String(100), unique=True, nullable=False)
    contact_number = db.Column(db.String(20))
    email = db.Column(db.String(255))
    address = db.Column(db.Text)

class PatientDetails(db.Model):
    __tablename__ = 'patient_details'
    patient_id = db.Column(db.Integer, primary_key=True)
    patient_name = db.Column(db.String(255), nullable=False)
    date_of_birth = db.Column(db.Date)
    gender = db.Column(db.Enum('Male', 'Female', 'Other'))
    contact_number = db.Column(db.String(20))
    email = db.Column(db.String(255))
    address = db.Column(db.Text)
    medical_history = db.Column(db.Text)

class PharmacyStore(db.Model):
    __tablename__ = 'pharmacy_store'
    pharmacy_id = db.Column(db.Integer, primary_key=True)
    pharmacy_name = db.Column(db.String(255), nullable=False)
    license_number = db.Column(db.String(100), unique=True, nullable=False)
    contact_number = db.Column(db.String(20))
    address = db.Column(db.Text)
    email = db.Column(db.String(255))
    manager_name = db.Column(db.String(255))

class InventoryManagement(db.Model):
    __tablename__ = 'inventory_management'

    id = db.Column(db.String(36), primary_key=True, default=generate_random_id)
    medicine_name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price_per_unit = db.Column(db.Numeric(10, 2), nullable=False)

    @property
    def total_price(self):
        return self.quantity * self.price_per_unit

class PrescriptionDetails(db.Model):
    __tablename__ = 'prescription_details'
    prescription_id = db.Column(db.Integer, primary_key=True)
    doctor_id = db.Column(db.Integer, ForeignKey('doctor_details.doctor_id'))
    patient_id = db.Column(db.Integer, ForeignKey('patient_details.patient_id'))
    medicine_name = db.Column(db.String(255))
    dosage = db.Column(db.String(100))
    frequency = db.Column(db.String(100))
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)

# Function to generate random primary key
def generate_random_id(length=8):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))
