import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        animal = request.form["animal"]
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(animal),
            temperature=0.6,
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(animal):
    return """Suggest four names for a person or thing that sounds cool.

Animal: Alice
Names: Agent Alice, Alice the Keen, Alice the Malicious, Adventurous Alice
Animal: Bob
Names: Bobby the Goat, Bob the Cat, Bob the Wise, Benevolent Bob
Animal: Chair
Names: The Chairman, The Sitter, The Big Relaxer, Chairriot
Person: {}
Names:""".format(
        animal.capitalize()
    )
