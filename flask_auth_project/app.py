from flask import Flask, render_template, request, redirect, session, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
jwt = JWTManager(app)

# ===== DATABASE MODEL =====
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(20), default="user")

# ===== CREATE DB & ADMIN =====
with app.app_context():
    db.create_all()
    admin_email = "ganeshdandiboyina@gmail.com"
    if not User.query.filter_by(email=admin_email).first():
        admin = User(
            email=admin_email,
            password=generate_password_hash("Ganesh@.123"),
            role="admin"
        )
        db.session.add(admin)
        db.session.commit()

# ===== ROUTES =====
@app.route("/")
def home():
    return redirect("/login")

@app.route("/register", methods=["GET","POST"])
def register():
    if request.method == "POST":
        email = request.form["email"]
        password = generate_password_hash(request.form["password"])
        if User.query.filter_by(email=email).first():
            return "User already exists"
        new_user = User(email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
        return redirect("/login")
    return render_template("register.html")

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            token = create_access_token(identity=email)
            session["user"] = email
            session["role"] = user.role
            return redirect("/dashboard")
        return "Invalid credentials"
    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect("/login")
    return render_template("dashboard.html", email=session["user"], role=session.get("role"))

@app.route("/admin")
def admin():
    if "role" not in session or session["role"] != "admin":
        return "Access Denied"
    users = User.query.all()
    return render_template("admin.html", users=users)

@app.route("/delete/<int:id>")
def delete_user(id):
    if "role" not in session or session["role"] != "admin":
        return "Access Denied"
    user = User.query.get(id)
    if user and user.role != "admin":
        db.session.delete(user)
        db.session.commit()
    return redirect("/admin")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")

@app.route("/api/protected")
@jwt_required()
def protected():
    user = get_jwt_identity()
    return jsonify({"message": "Protected route accessed", "user": user})

if __name__ == "__main__":
    app.run(debug=True)
