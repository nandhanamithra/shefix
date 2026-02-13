from flask import Flask, render_template, request, jsonify, redirect, url_for

app = Flask(__name__)

users = []

# ======================
# FRONTEND ROUTES
# ======================

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login")
def login_page():
    return render_template("login.html")

@app.route("/register")
def register_page():
    return render_template("register.html")

# ======================
# API ROUTES
# ======================

@app.route("/api/register", methods=["POST"])
def register():
    data = request.json
    users.append(data)
    return jsonify({"message": "User registered successfully!"})

@app.route("/api/login", methods=["POST"])
def login():
    data = request.json
    for user in users:
        if user["email"] == data["email"] and user["password"] == data["password"]:
            return jsonify({"message": "Login successful!"})
    return jsonify({"message": "Invalid credentials"}), 401


if __name__ == "__main__":
    print("hello")
    app.run(debug=True, port=8000)


