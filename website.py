from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "shefix_secret"  # Required for flash

users = []

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login")
def login_page():
    return render_template("login.html")

@app.route("/register")
def register_page():
    return render_template("register.html")
@app.route("/dashboard")
def dashboard_page():
    return render_template("dashboard.html")

@app.route("/solutions")
def solutions():
    return render_template("solutions.html")

@app.route("/community")
def community():
    return render_template("community.html")

@app.route("/services")
def services():
    return render_template("services.html")


@app.route("/solutions/tyre")
def tyre_fix():
    return render_template("tyre.html")

@app.route("/solutions/fuse")
def fuse_fix():
    return render_template("fuse.html")

@app.route("/solutions/hostel")
def hostel_hacks():
    return render_template("hostel.html")

# REGISTER
@app.route("/register", methods=["POST"])
def register_user():
    email = request.form.get("email")
    password = request.form.get("password")
    confirm_password = request.form.get("confirm_password")

    if password != confirm_password:
        flash("Passwords do not match!")
        return redirect(url_for("register_page"))

    for user in users:
        if user["email"] == email:
            flash("User already exists!")
            return redirect(url_for("register_page"))

    users.append({
        "email": email,
        "password": password
    })

    flash("Registration successful! Please login.")
    return redirect(url_for("login_page"))


# LOGIN
@app.route("/login", methods=["POST"])
def login_user():
    email = request.form.get("email")
    password = request.form.get("password")

    for user in users:
        if user["email"] == email and user["password"] == password:
            flash("Login successful!")
            return redirect(url_for("dashboard_page"))

    flash("Account not found. Please register.")
    return redirect(url_for("login_page"))

@app.route("/search", methods=["POST"])
def search():
    # Get the text from the search bar
    query = request.form.get("search_query", "").lower().strip()

    # Logic to redirect based on keywords
    if "tyre" in query:
        return redirect(url_for("tyre_page"))
    elif "fuse" in query:
        return redirect(url_for("fuse_page"))
    elif "hostel" in query:
        return redirect(url_for("hostel_page"))
    elif "solution" in query:
        return redirect(url_for("solutions_page"))
    # Added this so the search bar finds your new safety page!
    elif "safety" in query or "security" in query or "service" in query:
        return redirect(url_for("safety_page"))
    
    # If nothing matches, go back to the dashboard
    return redirect(url_for("dashboard"))


if __name__ == "__main__":
    app.run(debug=True, port=8000)
