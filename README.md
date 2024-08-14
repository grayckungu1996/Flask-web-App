


# Flask Web Application

This is a simple web application built using Flask, a lightweight WSGI web application framework in Python. The application includes basic user authentication, note management, and a well-structured backend.

## Features

- User registration and login
- Note creation, deletion, and viewing
- User authentication with Flask-Login
- Database management with SQLAlchemy

## Technologies Used

- **Flask**: A lightweight Python web framework
- **SQLAlchemy**: An ORM for database management
- **SQLite**: Database system
- **Flask-Login**: User session management
- **Werkzeug**: Security for password hashing

## Setup Instructions

### Prerequisites

- Python 3
- Virtual environment (optional but recommended)

### Installation

1. **Clone the Repository**

   git clone https://github.com/your-username/Flask-web-App.git
   cd Flask-web-App


2. **Create and Activate a Virtual Environment**

   python3 -m venv venv
   

3. **Install Dependencies**

   ```sh
   pip install -r requirements.txt
   ```

4. **Set Up the Database**

   ```sh
   python
   >>> from your_module import create_database
   >>> create_database()
   ```

   Replace `your_module` with the name of the Python file where `create_database` is defined (e.g., `__init__.py`).

5. **Run the Application**

   ```sh
   python your_module.py
   ```


### Usage

- **Visit the Application**: Open your browser and go to `http://127.0.0.1:5000/`.
- **Register**: Go to `/sign-up` to create a new account.
- **Login**: Use the `/login` route to sign in.
- **Manage Notes**: After logging in, you can create, view, and delete notes.

## File Structure

- `app/` – Contains Flask application code.
  - `__init__.py` – Initializes the Flask app, database, and login manager.
  - `auth.py` – Handles user authentication routes.
  - `views.py` – Contains routes for viewing and managing notes.
  - `models.py` – Defines the database models.
- `templates/` – Contains HTML templates for rendering views.
- `static/` – Contains static files such as CSS and JavaScript.
- `requirements.txt` – Lists the required Python packages.

## Contributing

Feel free to open issues or submit pull requests if you'd like to contribute to this project. Your contributions are welcome!

## License

This project is licensed under the MIT License. 
## Contact

For any questions or feedback, you can reach me at [grayckungu1996@gmail.com]
