from flask import Flask, request, render_template
import requests

app = Flask(__name__)

API_URL = "http://127.0.0.1:8000/humanize/"

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        text = request.form["text"]
        response = requests.post(API_URL, json={"text": text})
        humanized_text = response.json().get("humanized_text", "")
        return render_template("index.html", input_text=text, output_text=humanized_text)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, port=5000)

