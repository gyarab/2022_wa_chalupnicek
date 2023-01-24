import httpx
from pprint import pprint

url = "https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/denni_kurz.txt"
res = httpx.get(url)
rows = res.text.split("\n")

rows = rows[2:-1]

"""
result = amount / data["USD"]

data = {
    "EUR": 23.880,
    "USD": 21.971,
    ...
}
"""

data = {}

for r in rows:
    cols = r.split("|")
    curr = cols[-2]
    rate = cols[-1]
    rate = rate.replace(",", ".")
    rate = float(rate)
    data[curr] = rate
pprint(data)

user_amount = input("Zadej částku v CZK: ")
user_amount = float(user_amount)
user_curr = input("Zadej cílovou měnu: ")

result = user_amount / data[user_curr]
result = round(result, 2)

print(f"Vysledna castka je {result} {user_curr}")
