pets = []

pet = {
    'animal type': 'Dog',
    'name': 'Milo',
    'owner': 'Patrick',
    'weight': '32kg',
    'eats': 'Dog Food',
}
pets.append(pet)

pet = {
    'animal type': 'Cat',
    'name': 'Sugar',
    'owner': 'Zoe',
    'weight': '4kg',
    'eats': 'Cat Food',
}
pets.append(pet)

pet = {
    'animal type': 'Parrot',
    'name': 'Wreck',
    'owner': 'Taylor',
    'weight': '3kg',
    'eats': 'shoes',
}
pets.append(pet)


for pet in pets:
    print(f"\nHere's what I know about {pet['name'].title()}:")
    for key, value in pet.items():
        print(f"\t{key}: {value}")