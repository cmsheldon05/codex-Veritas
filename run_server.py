from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("sandbox.html")

@app.route("/sandbox")
def sandbox():
    return render_template("sandbox.html")

if __name__ == "__main__":
    # bind to all interfaces so your PHONE can reach it over Wi-Fi/LAN
    app.run(host="0.0.0.0", port=5050, debug=False)
