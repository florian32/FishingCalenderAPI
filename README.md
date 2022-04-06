# FishingCalenderAPI

A project that scrapes the web for data and returns a JSON with the informations about fishing bites during a chosen day.
## How does it work?

The project uses Beautiful Soup 4 to get the data from the site https://wedkuje.pl/kalendarz-wedkarski-bran-ryb.html. Then the data is being converted into a JSON and returned using Flask.

## How to access the data?

in order to access the data you need to go to the /search path and give as an argument day=your_chosen_day

For example:
http://127.0.0.1:5000/search?day=6 
will return the data from the sixth of the current month.
