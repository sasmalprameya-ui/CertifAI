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
        certificate_type = request.form["certificateType"]
        activity = ""
        certificate_title = ""
        certificate_text = ""
        if certificate_type == "Internship":

           certificate_title = "INTERNSHIP"

           certificate_text = "for successfully completing the internship in"

           activity = request.form["domain"]
        elif certificate_type == "Workshop":
           certificate_title = "WORKSHOP"
           certificate_text = "for successfully attending"

           activity = request.form["workshop"]
           instructor = request.form["instructor"]
           duration = request.form["duration"]
        elif certificate_type == "Hackathon":
           certificate_title = "HACKATHON"
           certificate_text = "for participating in"

           activity = request.form["hackathon"]
           team = request.form["team"]
           position = request.form["position"]
        elif certificate_type == "Competition":
           certificate_title = "COMPETITION"
           certificate_text = "for participating in"

           activity = request.form["competition"]
           rank = request.form["rank"]
        elif certificate_type == "Participation":
            certificate_title = "PARTICIPATION"
            certificate_text = "for active participation in"

            activity = request.form["event"]
            organizer = request.form["organizer"]
        elif certificate_type == "Completion":
            certificate_title = "COMPLETION"
            certificate_text = "for successfully completing"

            activity = request.form["Course"]
            duration = request.form["duration"]   
        elif certificate_type == "Appreciation":
            certificate_title = "APPRECIATION"
            certificate_text = "in appreciation for"

            activity = request.form["reason"]
        elif certificate_type == "Excellence":
            certificate_title = "EXCELLENCE"
            certificate_text = "for excellence in"

            activity = request.form["achievement"]
        elif certificate_type == "Volunteer":
            certificate_title = "VOLUNTEER"
            certificate_text = "for dedicated volunteer service as"

            activity = request.form["role"]
            department = request.form["department"]   
        elif certificate_type == "Winner":
            certificate_title = "WINNER"
            certificate_text = "for securing first position in"

            activity = request.form["competition"]
            position = request.form["position"]
        elif certificate_type == "Runner-Up":
            certificate_title = "RUNNER-UP"
            certificate_text = "for securing runner-up position in"

            activity = request.form["competition"]
        elif certificate_type == "Seminar":
            certificate_title = "SEMINAR"
            certificate_text = "for successfully attending"

            activity = request.form["seminar"]
            speaker = request.form["speaker"]              

        organization = request.form["organization"]
        date = request.form["date"]
        certificate_id = "CERT-2026-" + str(random.randint(100000,999999))
        return render_template(
            "certificate.html",
            name=name,
            certificate_title=certificate_title,
            certificate_text=certificate_text,
            activity=activity,
            organization=organization,
            date=date,
            certificate_id=certificate_id
        )

    return render_template("generate.html")


if __name__ == "__main__":
    app.run(debug=True)