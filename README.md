Employee Management System

A modern Employee Management System built using FastAPI, SQLAlchemy, MySQL, Jinja2, HTML, and CSS. The application provides a simple interface for managing employee records with authentication and CRUD operations.

🚀 Features

- 🔐 User Registration
- 🔑 User Login
- 🏠 Dashboard
- ➕ Add Employee
- 👀 View All Employees
- ✏️ Update Employee Details
- 🗑️ Delete Employee
- 🎨 Responsive and modern UI
- 💾 MySQL database integration using SQLAlchemy
- ⚡ FastAPI backend for high performance

🛠️ Tech Stack

- Backend: FastAPI
- Database: MySQL
- ORM: SQLAlchemy
- Frontend: HTML, CSS, Jinja2 Templates
- Language: Python

📂 Project Structure

Employee_Management_System/
│
├── routers/
│   ├── users.py
│   └── employees.py
│
├── templates/
│   ├── register.html
│   ├── login.html
│   ├── dashboard.html
│   ├── add_employee.html
│   ├── update_employee.html
│   └── view_employee.html
│
├── static/
│   └── style.css
│
├── uploads/
│
├── auth.py
├── crud.py
├── database.py
├── models.py
├── schemas.py
├── main.py
└── README.md

⚙️ Installation

1. Clone the repository

git clone https://github.com/swaroopmore/Employee_Management_System.git

2. Navigate to the project folder

cd Employee_Management_System

3. Install dependencies

pip install -r requirements.txt

4. Configure your MySQL database credentials in "database.py".

5. Start the FastAPI server

uvicorn main:app --reload

6. Open your browser and visit:

http://127.0.0.1:8000

📸 Functionalities

- Register a new user
- Login with credentials
- Add employee records
- View all employees
- Edit employee information
- Delete employee records
- Navigate through a clean dashboard interface

🔮 Future Improvements

- JWT Authentication
- Password Reset
- Employee Search and Filters
- Pagination
- Profile Picture Upload
- Role-Based Access Control (Admin/User)
- REST API Documentation
- Docker Deployment

👨‍💻 Author

Swaroop More

GitHub: https://github.com/swaroopmore

---

⭐ If you found this project useful, consider giving it a star on GitHub!
