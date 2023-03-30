import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.organization=os.getenv("ORGANIZATION")
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.Model.list()

@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        question = request.form["question"]
        # question=question.format(question.capitalize())
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content":  question},
        #{{variable}} 是flask的语法，用来标记变量
            ]
            )
        
        return redirect(url_for("index", result=response['choices'][0]['message']['content']))

    result = request.args.get("result")
    return render_template("index.html", result=result)

#example prompt
# def generate_prompt(animal):
    
#     return """Suggest three names for an animal that is a superhero.

# Animal: Cat
# Names: Captain Sharpclaw, Agent Fluffball, The Incredible Feline
# Animal: Dog
# Names: Ruff the Protector, Wonder Canine, Sir Barks-a-Lot
# Animal: {}
# Names:""".format(
#         animal.capitalize()
#     )
