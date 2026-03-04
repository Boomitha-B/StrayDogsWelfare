from flask import Flask, request, jsonify, send_from_directory
import mysql.connector
from mysql.connector import Error
from db_config import DB_CONFIG
import os

app = Flask(__name__, static_url_path='', static_folder='.')

def get_db_connection():
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

# Serve Index Page
@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

# Serve Static Pages
@app.route('/pages/<path:path>')
def serve_pages(path):
    return send_from_directory('pages', path)

# Serve CSS
@app.route('/css/<path:path>')
def serve_css(path):
    return send_from_directory('css', path)

# Serve JS
@app.route('/js/<path:path>')
def serve_js(path):
    return send_from_directory('js', path)

# Serve Images
@app.route('/images/<path:path>')
def serve_images(path):
    return send_from_directory('images', path)

# --- API ENDPOINTS ---

@app.route('/api/contact', methods=['POST'])
def contact():
    data = request.json
    name = data.get('name')
    email = data.get('email')
    message = data.get('message')

    if not all([name, email, message]):
        return jsonify({'error': 'Missing data'}), 400

    conn = get_db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            query = "INSERT INTO messages (name, email, message) VALUES (%s, %s, %s)"
            cursor.execute(query, (name, email, message))
            conn.commit()
            return jsonify({'message': 'Message sent successfully!'}), 201
        except Error as e:
            return jsonify({'error': str(e)}), 500
        finally:
            cursor.close()
            conn.close()
    else:
        return jsonify({'error': 'Database connection failed'}), 500

@app.route('/api/donate', methods=['POST'])
def donate():
    data = request.json
    donor_name = data.get('donor_name')
    email = data.get('email')
    amount = data.get('amount')

    if not all([donor_name, email, amount]):
        return jsonify({'error': 'Missing data'}), 400

    conn = get_db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            query = "INSERT INTO donations (donor_name, email, amount) VALUES (%s, %s, %s)"
            cursor.execute(query, (donor_name, email, amount))
            conn.commit()
            return jsonify({'message': 'Donation recorded successfully!'}), 201
        except Error as e:
            return jsonify({'error': str(e)}), 500
        finally:
            cursor.close()
            conn.close()
    else:
        return jsonify({'error': 'Database connection failed'}), 500

@app.route('/api/volunteer', methods=['POST'])
def volunteer():
    data = request.json
    name = data.get('name')
    email = data.get('email')
    phone = data.get('phone')
    interest = data.get('interest')

    if not all([name, email]):
        return jsonify({'error': 'Missing data'}), 400

    conn = get_db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            query = "INSERT INTO volunteers (name, email, phone, interest) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (name, email, phone, interest))
            conn.commit()
            return jsonify({'message': 'Volunteer application submitted successfully!'}), 201
        except Error as e:
            return jsonify({'error': str(e)}), 500
        finally:
            cursor.close()
            conn.close()
    else:
        return jsonify({'error': 'Database connection failed'}), 500

@app.route('/api/rescue', methods=['POST'])
def rescue():
    data = request.json
    reporter_name = data.get('reporter_name')
    contact_number = data.get('contact_number')
    location = data.get('location')
    description = data.get('description')

    if not all([reporter_name, contact_number, location]):
        return jsonify({'error': 'Missing required fields'}), 400

    conn = get_db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            query = "INSERT INTO rescues (reporter_name, contact_number, location, description) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (reporter_name, contact_number, location, description))
            conn.commit()
            return jsonify({'message': 'Rescue report submitted successfully! Help is on the way.'}), 201
        except Error as e:
            return jsonify({'error': str(e)}), 500
        finally:
            cursor.close()
            conn.close()
    else:
        return jsonify({'error': 'Database connection failed'}), 500

@app.route('/api/adoption', methods=['POST'])
def adoption():
    data = request.json
    applicant_name = data.get('applicant_name')
    email = data.get('email')
    dog_name = data.get('dog_name')

    if not all([applicant_name, email, dog_name]):
        return jsonify({'error': 'Missing required fields'}), 400

    conn = get_db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            query = "INSERT INTO adoptions (applicant_name, email, dog_name) VALUES (%s, %s, %s)"
            cursor.execute(query, (applicant_name, email, dog_name))
            conn.commit()
            return jsonify({'message': 'Adoption application submitted! We will contact you soon.'}), 201
        except Error as e:
            return jsonify({'error': str(e)}), 500
        finally:
            cursor.close()
            conn.close()
    else:
        return jsonify({'error': 'Database connection failed'}), 500

if __name__ == '__main__':
    app.run(debug=True, port=8000)
