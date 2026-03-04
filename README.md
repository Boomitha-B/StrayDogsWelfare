# Stray Dogs Welfare - Web Application

This is a full-stack Flask application for the Stray Dogs Welfare NGO.

## 📂 Project Structure
- **app.py**: Main Flask application file.
- **db_config.py**: Database configuration (Update credentials here).
- **schema.sql**: Database schema definition.
- **setup_db.py**: Script to automatically create the database and tables.
- **pages/**: HTML templates.
- **static/**: CSS, JS, and Images.

## 🚀 Setup Instructions

### 1. Prerequisites
- Python installed.
- MySQL Server installed and running.

### 2. Install Dependencies
Open your terminal in this folder and run:
```bash
pip install -r requirements.txt
```

### 3. Configure Database
1. Open `db_config.py`.
2. Update the `DB_CONFIG` dictionary with your MySQL **username** and **password**.

### 4. Initialize Database
Run this script once to create the database and tables:
```bash
python setup_db.py
```

### 5. Run the Application
Start the server:
```bash
python app.py
```
Access the website at: **http://localhost:8000**

## ✨ Features
- **Dynamic Forms**: Donate, Volunteer, Rescue, Contact.
- **Database Integration**: All submissions are saved to MySQL.
- **Validation**: Strict input validation for Phone/Names.
- **Toast Notifications**: Interactive success/error messages.
