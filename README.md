# Enterprise-User-Authentication-System
A modern and secure Flask-based authentication system designed for enterprise applications. Features include:  User registration and login with secure password hashing  JWT-based protected API routes  Session management  Admin panel to manage users  Delete non-admin users  Responsive and modern HTML templates  ,a small Application

enterprise_auth/
│
├─ app.py                # Main Flask app
├─ config.py             # Configuration settings
├─ requirements.txt      # Python dependencies
├─ users.db              # SQLite database (auto-created)
│
├─ templates/            # HTML templates
│   ├─ base.html
│   ├─ login.html
│   ├─ register.html
│   ├─ dashboard.html
│   └─ admin.html
│
└─ static/               # Static assets
    ├─ style.css
    └─ script.js

⚡ Installation & Setup

   Clone the repository or download the files:

      git clone <your-repo-link>
      cd enterprise_auth


Install dependencies:

pip install -r requirements.txt


Run the Flask app:

    python app.py


Open in browser:

    http://127.0.0.1:5000/login

👤 Default Admin Credentials

    Email: ganeshdandiboyina@gmail.com

    Password: Ganesh@.123

    Admin can access /admin to view all users and delete non-admin accounts.

📝 Usage

    Register new user: /register

    Login: /login

    Dashboard: /dashboard (after login)

    Admin panel: /admin (admin-only)

    Logout: /logout

Protected API: /api/protected (JWT required)

🔒 Security Notes

    Passwords are hashed using Werkzeug

    JWT secures protected API routes

    Change SECRET_KEY and JWT_SECRET_KEY in config.py for production

    For production, consider PostgreSQL/MySQL instead of SQLite

🎨 Frontend

    Modern and responsive layout

    Navbar, buttons, tables, and alerts

    Static files: style.css and script.js

⚙️ Technologies Used

    Python 3

    Flask Framework

    Flask-SQLAlchemy

    Flask-JWT-Extended

    Werkzeug Security

    HTML5, CSS3, JavaScript

📈 Future Improvements

    Email verification during registration

    Password reset functionality

    Role-based access control beyond admin/user

    Integration with cloud databases
 
    Enhanced UI/UX with frameworks like Bootstrap or Tailwind


💻 Author

   .Ganesh Dandiboyina – Full-stack enthusiast & developer
