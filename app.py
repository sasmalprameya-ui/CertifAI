from flask import Flask, render_template, request
import random
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/generate", methods=["GET", "POST"])
def generate():

    if request.method == "POST":

        name = request.form["name"]
        course = request.form["course"]
        organization = request.form["organization"]
        date = request.form["date"]
        certificate_id = "CERT-2026-" + str(random.randint(100000,999999))
        return render_template(
            "certificate.html",
            name=name,
            course=course,
            organization=organization,
            date=date,
            certificate_id=certificate_id
        )

    return render_template("generate.html")


if __name__ == "__main__":
    app.run(debug=True)