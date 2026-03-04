# 🐾 Stray Dogs Welfare - Web Application

<p align="center">
  <b>Full-Stack NGO Platform | Animal Rescue & Care | Community Driven</b><br>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Built%20With-Python%20%7C%20Flask%20%7C%20MySQL-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Frontend-HTML%20%7C%20CSS%20%7C%20JS-orange?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Status-Deployment%20Ready-green?style=for-the-badge" />
</p>

---

![Banner](docs/screenshots/banner.png)

## 📌 Table of Contents
- [📖 About The Project](#-about-the-project)
- [✨ Key Features](#-key-features)
- [🧩 Website Modules](#-website-modules)
- [🛠 Tech Stack](#-tech-stack)
- [💻 Installation & Usage](#-installation--usage)
- [🎨 Design Philosophy](#-design-philosophy)
- [📬 Contact](#-contact)

---

## 📖 About The Project
The **Stray Dogs Welfare** platform is a comprehensive full-stack solution designed to streamline the operations of an animal rescue NGO. It provides a bridge between the community and rescuers, ensuring that every dog in distress receives timely medical care, shelter, and love.

This project goes beyond a simple website by integrating a robust **MySQL database** to manage real-world data like rescue reports, volunteer applications, and donations.

---

## ✨ Key Features
✔ **Emergency Rescue Portal**: Instant reporting system for dogs in distress.

✔ **Volunteer Management**: Streamlined application process for community support.

✔ **Secure Donation Tracking**: Dedicated module for financial contribution logging.

✔ **Adoption & Sterilization**: Information and request tracking for animal welfare.

✔ **Dynamic Notifications**: Interactive UI alerts for form submissions.

✔ **Database Backed**: Full history of all interactions stored securely.

---

## 🧩 Website Modules

### 🏠 Home
A welcoming landing page featuring the mission and a call to action for donations.
![Homepage](docs/screenshots/homepage.png)

### 🏥 Rescue & Medical Care
Details the rescue process and provides a form for emergency reporting.
![Rescue](docs/screenshots/rescue.png)

### 🤝 Volunteer & Community
A dedicated space for dog lovers to join the cause and manage their interests.
![Volunteer](docs/screenshots/volunteer.png)

### 💰 Donation Center
Outlines how funds are utilized and provides a secure contribution interface.
![Donate](docs/screenshots/donate.png)

---

## 🛠 Tech Stack
- **Python (Flask)** – Backend logic and API management.
- **MySQL** – Relational database for data persistence.
- **HTML5 & CSS3** – Structured and aesthetically pleasing UI.
- **JavaScript (ES6)** – Client-side interactions and form validation.
- **MySQL Connector** – Secure bridge between Python and the database.

---

### 📂 Project Structure
- **app.py** – Main server and API routes.
- **db_config.py** – Configuration for database connectivity.
- **setup_db.py** – Automated database initialization script.
- **schema.sql** – Database blueprints and table definitions.
- **pages/** – Multi-page HTML templates.
- **css/ & js/** – Design system and interactive behaviors.
- **docs/screenshots/** – Visual assets for documentation.

---

## 💻 Installation & Usage

### 1. Clone the Repository
```bash
git clone https://github.com/Boomitha-B/StrayDogsWelfare.git
cd StrayDogsWelfare
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Database Initialization
Update your credentials in `db_config.py` and run:
```bash
python setup_db.py
```

### 4. Run the App
```bash
python app.py
```
Visit `http://localhost:8000` to see it in action!

---

## 🎨 Design Philosophy
The UI follows a **warm and professional** aesthetic, using a palette of earthy tones (tans, browns, and whites) to evoke feelings of trust and care. Minimalist components ensure that the focus remains on the animals and the mission.

---

## 📬 Contact
For collaborations or inquiries:
- **GitHub**: [@Boomitha-B](https://github.com/Boomitha-B)
- **LinkedIn**: [Your Profile Link]
- **Email**: [Your Email Address]

---
© 2026 Stray Dogs Welfare – Making a difference, one rescued soul at a time.
