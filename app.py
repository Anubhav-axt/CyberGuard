from flask import Flask, render_template, request, jsonify
from modules.password_checker import check_password
from modules.password_generator import generate_password, generate_passphrase
from modules.hash_generator import generate_hash, generate_all_hashes
from modules.port_scanner import scan_ports
from modules.phishing_detector import analyze_url

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@app.route("/password")
def password():
    return render_template("password.html")


@app.route("/password/check", methods=["POST"])
def password_check():
    password_str = request.form.get("password", "")
    result = check_password(password_str)
    return jsonify(result)


@app.route("/generator")
def generator():
    return render_template("generator.html")


@app.route("/password/generate", methods=["POST"])
def password_generate():
    length = int(request.form.get("length", 16))
    use_uppercase = request.form.get("uppercase") == "on"
    use_lowercase = request.form.get("lowercase") == "on"
    use_numbers = request.form.get("numbers") == "on"
    use_special = request.form.get("symbols") == "on"

    if request.form.get("type") == "passphrase":
        word_count = int(request.form.get("word_count", 4))
        result = generate_passphrase(word_count)
        return jsonify({"password": result})
    else:
        result = generate_password(length, use_uppercase, use_lowercase, use_numbers, use_special)
        return jsonify({"password": result})


@app.route("/hash")
def hash_page():
    return render_template("hash.html")


@app.route("/hash/generate", methods=["POST"])
def hash_generate():
    text = request.form.get("text", "")
    algorithm = request.form.get("algorithm", "sha256")
    result = generate_hash(text, algorithm)
    return jsonify(result)


@app.route("/scanner")
def scanner():
    return render_template("scanner.html")


@app.route("/scanner/scan", methods=["POST"])
def scanner_scan():
    target = request.form.get("target", "")
    start_port = int(request.form.get("start_port", 1))
    end_port = int(request.form.get("end_port", 1024))
    result = scan_ports(target, start_port, end_port)
    return jsonify(result)


@app.route("/phishing")
def phishing():
    return render_template("phishing.html")


@app.route("/phishing/check", methods=["POST"])
def phishing_check():
    url = request.form.get("url", "")
    result = analyze_url(url)
    return jsonify(result)


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)
