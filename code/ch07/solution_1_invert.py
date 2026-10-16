capitals = {"France": "Paris", "Japan": "Tokyo", "Kenya": "Nairobi"}
countries = {}
for country, capital in capitals.items():
    countries[capital] = country
print(countries)
print(countries["Tokyo"])
