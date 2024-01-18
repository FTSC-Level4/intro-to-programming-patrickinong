def describe_city(city, country='Philippines'):
    """Describe a city."""
    msg = f"{city.title()} is in {country.title()}."
    print(msg)

describe_city('Manila')
describe_city('Abu Dhabi', 'United Arab Emirates')
describe_city('Rizal')