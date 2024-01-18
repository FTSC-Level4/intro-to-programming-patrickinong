rivers = {
    'Nile river': 'Egypt',
    'Pasig river': 'Phillipines',
    'Amazon river': 'Brazil, Peru, Bolivia, Ecuador, Colombia, Venezuela, Guyana, Suriname',
    'Danube river': 'Austria, Slovakia, Hungary, Croatia, Serbia, Romania, Bulgaria, Moldova, and Ukraine',
    'Mekong river': 'China, Myanmar, Thailand, Lao PDR, Cambodia and Viet Nam',
    }

for river, country in rivers.items():
    print(f"The {river.title()} flows through {country.title()}.")

print("\nThe following rivers are included in this data set:")
for river in rivers.keys():
    print(f"- {river.title()}")

print("\nThe following countries are included in this data set:")
for country in rivers.values():
    print(f"- {country.title()}")