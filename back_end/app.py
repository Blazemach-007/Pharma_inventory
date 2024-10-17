from flask import Flask, jsonify, request
from flask_cors import CORS
from config import Config
from models import db, DoctorDetails, PatientDetails, PharmacyStore, Medicines, InventoryManagement, PrescriptionDetails, Sales, UserAuthentication

app = Flask(__name__)
app.config.from_object(Config)
CORS(app)
db.init_app(app)

@app.before_first_request
def create_tables():
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
    return jsonify([{
        'doctor_id': doctor.doctor_id,
        'doctor_name': doctor.doctor_name,
        'specialization': doctor.specialization
    } for doctor in doctors])

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

# Route for adding medicine
@app.route('/medicines', methods=['POST'])
def add_medicine():
    data = request.json
    new_medicine = Medicines(
        name=data['name'],
        expiration_date=data['expiration_date'],
        cost=data['cost']
    )
    db.session.add(new_medicine)
    db.session.commit()
    return jsonify({'message': 'Medicine added successfully', 'medicine_id': new_medicine.medicine_id}), 201

# Route for adding inventory
@app.route('/inventory', methods=['POST'])
def add_inventory():
    data = request.json
    new_inventory = InventoryManagement(
        medicine_id=data['medicine_id'],
        quantity=data['quantity'],
        price_per_unit=data['price_per_unit'],
    )
    db.session.add(new_inventory)
    db.session.commit()
    return jsonify({'message': 'Inventory added successfully', 'inventory_id': new_inventory.id}), 201

# Route for adding a prescription
@app.route('/prescriptions', methods=['POST'])
def add_prescription():
    data = request.json
    new_prescription = PrescriptionDetails(
        doctor_id=data['doctor_id'],
        patient_id=data['patient_id'],
        medicine_id=data['medicine_id'],
        dosage=data['dosage'],
        frequency=data['frequency'],
        start_date=data['start_date'],
        end_date=data['end_date'],
    )
    db.session.add(new_prescription)
    db.session.commit()
    return jsonify({'message': 'Prescription added successfully', 'prescription_id': new_prescription.prescription_id}), 201

# Route for adding a sale
@app.route('/sales', methods=['POST'])
def add_sale():
    data = request.json
    new_sale = Sales(
        medicine_id=data['medicine_id'],
        quantity=data['quantity'],
        total_amount=data['total_amount']
    )
    db.session.add(new_sale)
    db.session.commit()
    return jsonify({'message': 'Sale added successfully', 'sale_id': new_sale.sale_id}), 201

# Route for user authentication
@app.route('/users', methods=['POST'])
def add_user():
    data = request.json
    new_user = UserAuthentication(
        username=data['username'],
        phone_number=data['phone_number'],
        password=data['password'],
        admin=data.get('admin', False)
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User added successfully', 'user_id': new_user.user_id}), 201

if __name__ == '__main__':
    app.run(debug=True)
