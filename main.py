from bs4 import BeautifulSoup
import requests
from flask import Flask, jsonify, render_template, request, session

app = Flask(__name__)

response = requests.get("https://wedkuje.pl/kalendarz-wedkarski-bran-ryb.html")
website = response.text
soup = BeautifulSoup(website, "html.parser")

days = soup.find_all(name="span", class_="dzien")
days = [day.getText() for day in days]

moon_phases = soup.find_all(name="div", class_="KontenerFazy")
moon_phases = [moon_phase.getText().replace("\n", "") for moon_phase in moon_phases]

bites = soup.find_all(name="div", class_="KontenerRyby")
bites = [bite.getText().replace("\n", "") for bite in bites]

result = {}

for i in range(len(days)):
    result[days[i]] = [moon_phases[i], bites[i]]


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/search")
def get_day():
    day = request.args.get("day")

    return jsonify(day=day,
                   moon_phase=result[day][0],
                   bites=result[day][1],
                   )


if __name__ == '__main__':
    app.run(debug=True)
