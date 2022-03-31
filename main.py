from bs4 import BeautifulSoup
import requests

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

print(result)
