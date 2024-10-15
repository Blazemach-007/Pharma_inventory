from flask import Flask, jsonify, request
from flask_cors import CORS
from config import Config
from models import db, DoctorDetails, PatientDetails, PharmacyStore, InventoryManagement, PrescriptionDetails, generate_random_id

app = Flask(__name__)
app.config.from_object(Config)
CORS(app)
db.init_app(app)

@app.before_request
def create_tables():
    with app.app_context():
        db.create_all()

# Route for adding a doctor
@app.route('/doctors', methods=['POST'])
def add_doctor():
    data = request.json
    new_doctor = DoctorDetails(
        doctor_name=data['doctor_name'],
        specialization=data.get('specialization'),
        license_number=data['license_number'],
        contact_number=data.get('contact_number'),
        email=data.get('email'),
        address=data.get('address'),
    )
    db.session.add(new_doctor)
    db.session.commit()
    return jsonify({'message': 'Doctor added successfully', 'doctor_id': new_doctor.doctor_id}), 201

# Route for retrieving all doctors
@app.route('/doctors', methods=['GET'])
def get_doctors():
    doctors = DoctorDetails.query.all()
    return jsonify([{ 'doctor_id': doctor.doctor_id, 'doctor_name': doctor.doctor_name } for doctor in doctors])

# Route for adding a patient
@app.route('/patients', methods=['POST'])
def add_patient():
    data = request.json
    new_patient = PatientDetails(
        patient_name=data['patient_name'],
        date_of_birth=data['date_of_birth'],
        gender=data['gender'],
        contact_number=data.get('contact_number'),
        email=data.get('email'),
        address=data.get('address'),
        medical_history=data.get('medical_history'),
    )
    db.session.add(new_patient)
    db.session.commit()
    return jsonify({'message': 'Patient added successfully', 'patient_id': new_patient.patient_id}), 201

# Route for retrieving all patients
@app.route('/patients', methods=['GET'])
def get_patients():
    patients = PatientDetails.query.all()
    return jsonify([{ 'patient_id': patient.patient_id, 'patient_name': patient.patient_name } for patient in patients])

# Route for adding a pharmacy
@app.route('/pharmacies', methods=['POST'])
def add_pharmacy():
    data = request.json
    new_pharmacy = PharmacyStore(
        pharmacy_name=data['pharmacy_name'],
        license_number=data['license_number'],
        contact_number=data.get('contact_number'),
        address=data.get('address'),
        email=data.get('email'),
        manager_name=data.get('manager_name'),
    )
    db.session.add(new_pharmacy)
    db.session.commit()
    return jsonify({'message': 'Pharmacy added successfully', 'pharmacy_id': new_pharmacy.pharmacy_id}), 201

# Route for adding inventory
@app.route('/inventory', methods=['POST'])
def add_inventory():
    data = request.json
    new_inventory = InventoryManagement(
        medicine_name=data['medicine_name'],
        quantity=data['quantity'],
        price_per_unit=data['price_per_unit'],
    )
    db.session.add(new_inventory)
    db.session.commit()
    return jsonify({'message': 'Inventory added successfully', 'inventory_id': new_inventory.id}), 201

# Route for retrieving all inventory records
@app.route('/inventory', methods=['GET'])
def get_inventory():
    inventory = InventoryManagement.query.all()
    return jsonify([{
        'inventory_id': inv.id,
        'medicine_name': inv.medicine_name,
        'quantity': inv.quantity,
        'price_per_unit': str(inv.price_per_unit),
        'total_price': str(inv.total_price),
    } for inv in inventory])

# Route for adding a prescription
@app.route('/prescriptions', methods=['POST'])
def add_prescription():
    data = request.json
    new_prescription = PrescriptionDetails(
        doctor_id=data['doctor_id'],
        patient_id=data['patient_id'],
        medicine_name=data['medicine_name'],
        dosage=data['dosage'],
        frequency=data['frequency'],
        start_date=data['start_date'],
        end_date=data['end_date'],
    )
    db.session.add(new_prescription)
    db.session.commit()
    return jsonify({'message': 'Prescription added successfully', 'prescription_id': new_prescription.prescription_id}), 201

# Route for retrieving all prescriptions
@app.route('/prescriptions', methods=['GET'])
def get_prescriptions():
    prescriptions = PrescriptionDetails.query.all()
    return jsonify([{
        'prescription_id': pres.prescription_id,
        'medicine_name': pres.medicine_name,
        'dosage': pres.dosage,
        'frequency': pres.frequency,
        'start_date': pres.start_date.isoformat(),
        'end_date': pres.end_date.isoformat()
    } for pres in prescriptions])

# @app.route('/test_db', methods=['GET'])
# def test_db():
#     try:
#         # Attempt to query the DoctorDetails table
#         doctors = DoctorDetails.query.limit(1).all()
#         return jsonify({'message': 'Database connection successful', 'doctors': [doctor.doctor_name for doctor in doctors]}), 200
#     except Exception as e:
#         return jsonify({'message': 'Database connection failed', 'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
