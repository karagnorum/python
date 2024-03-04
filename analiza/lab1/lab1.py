import csv


def replace_blanks(input_file, output_file):
    """Replaces each blank space in text from input_file with a colon and writes it to output_file."""

    with open(input_file, 'r') as file:
        content = file.read()

    import re
    modified_content = re.sub(r'(\t)+|  +', ';', content)

    with open(output_file, 'w') as file:
        file.write(modified_content)


replace_blanks("kraje0.csv", "kraje.csv")


# we will store names of all existing countries here
existing_countries = [None] * 195
# file containing all existing countries. utf-8-sig used to handle UTF-8 BOM character
with open("kraje.csv", encoding='utf-8-sig') as file:
    data = csv.DictReader(file, delimiter=';')
    j = 0
    for row in data:
        # column with country name is called "b"
        existing_countries[j] = row["b"]
        j = j + 1


regions = []  # we will store column "Country name" here
# file containing population of different countries in different years
with open("dane.csv", encoding='utf-8-sig') as file:

    data = csv.DictReader(file)
    for row in data:
        regions.append(row["Country Name"])

# countries named differently in "kraje.csv" and "dane.csv", eg. 'Syria' vs 'Syrian Arab Republic'
problematic_countries = {'Syrian Arab Republic', 'Congo, Rep.', 'Slovak Republic', 'West Bank and Gaza', 'Gambia, The', 'Turkiye', 'Bahamas, The', 'Iran, Islamic Rep.', 'Russian Federation', 'Eswatini', "Cote d'Ivoire", 'Lao PDR', 'Congo, Dem. Rep.',
                         'St. Vincent and the Grenadines', 'St. Kitts and Nevis', 'United States', 'Venezuela, RB', 'Micronesia, Fed. Sts.', 'Korea, Rep.', 'Kyrgyz Republic', 'Yemen, Rep.', 'Czechia', 'St. Lucia', 'Egypt, Arab Rep.', 'Myanmar', 'Viet Nam', 'Brunei Darussalam', 'Korea, Dem. People\'s Rep.'}

assert (len(problematic_countries) == len(
    set(existing_countries) - set(regions)) - 1)  # There is exactly one country, Holy See, not included in "dane.csv"
non_problematic_countries = set(
    existing_countries).intersection(set(regions))  # countries named the same in "kraje.csv" and "dane.csv"
assert (len(non_problematic_countries.intersection(problematic_countries)) == 0)
countries = list(non_problematic_countries.union(problematic_countries))

for i in range(1960, 2023):
    year = str(i)

    with open("dane.csv", encoding='utf-8-sig') as file:

        # dictionary, which binds population to set of countries with this population
        countries_population = dict()
        data = csv.DictReader(file)

        for row in data:
            if row[year] == "":
                continue
            region = row["Country Name"]
            population = int(row[year])  # population in region in year i
            if region in countries:
                # add region to list of those with the population
                if population not in countries_population.keys():
                    countries_population[population] = set()
                countries_population[population].add(region)

        populations = list(countries_population.keys())
        populations.sort()

        most_populated_countries = []
        greatest_populations = []
        for j in range(-5, 0):
            for country in countries_population[populations[j]]:
                greatest_populations.append(populations[j])
                most_populated_countries.append(country)

        assert (len(most_populated_countries) == len(greatest_populations))
        for j in range(len(greatest_populations)):
            assert (type(greatest_populations[j]) is int)
            assert (
                most_populated_countries[j] in countries_population[greatest_populations[j]])

        print(i)
        print(most_populated_countries)
        print(greatest_populations)

        import matplotlib.pyplot as plt
        import numpy as np
        plt.clf()  # clear the plot
        plt.bar(most_populated_countries,
                greatest_populations, color='blue')
        # Rotate labels for better visibility
        plt.xticks(rotation=45, ha='left')
        plt.ylim(0, 2*10**9)
        plt.tight_layout()  # Adjust layout to prevent clipping of labels
        plt.savefig('plot' + year + '.png')
