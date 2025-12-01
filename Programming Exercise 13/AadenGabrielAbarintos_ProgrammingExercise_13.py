# AadenGabrielAbarintos_ProgrammingExercise_13.py
# This program creates a database called population_AA
# then creates a table within that database with the fields
# city, year, and population. The data is composed of
# ten cities within the state of Florida from the year 2023. 
# The program then simulates population growth and decline 
# for the next 20 years. Then the program shows the 
# population growth for a city. The user then is prompted
# to select a city to display the data.


# Import the SQLite module.
import sqlite3


# Import the random module.
import random


# Import the matplotlib module.
import matplotlib.pyplot as plt


# Define the create_db function.
def create_db():

    # Connect/Create the database.
    conn = sqlite3.connect("population_AA.db")
    c = conn.cursor()

    # Create the table if it does not already exist.
    c.execute(
        "CREATE TABLE IF NOT EXISTS "
        "population(city TEXT, "
        "year INTEGER, population INTEGER)"
        )

    conn.commit()
    conn.close()


# Define the simulate function.
def simulate():

    # Connect to the database.
    conn = sqlite3.connect("population_AA.db")
    c = conn.cursor()

    # Clear old data so the simulation is fresh.
    c.execute("DELETE FROM population")

    # Add the starting populations from 2023.
    cities = {
        "Miami": 470677,
        "Orlando": 327390,
        "Tampa": 409742,
        "Jacksonville": 993468,
        "Tallahassee": 203665,
        "St. Petersburg": 265083,
        "Fort Lauderdale": 187872,
        "Gainesville": 147524,
        "Sarasota": 58061,
        "Venice": 28325
    }

    # Add the values.
    for city, pop in cities.items():
            c.execute(
                "INSERT INTO population VALUES (?, ?, ?)", 
                (city, 2023, pop)
                )


    # Simulate the population growth/decline
    # from 2024 to 2043.
    for city, pop_2023 in cities.items():
        last_pop = pop_2023

        for year in range(2024, 2044):
            rate = random.uniform(-0.02, 0.03)

            # Calculate the new population.
            new_pop = int(last_pop * (1 + rate))

            # Insert the data.
            c.execute(
                "INSERT INTO population VALUES (?, ?, ?)", 
                (city, year, new_pop)
                )
            last_pop = new_pop

    # Commit the changes.
    conn.commit()

    # Close the file.
    conn.close()


# Define the plot_population function.
def plot_city_population():

    conn = sqlite3.connect("population_AA.db")
    c = conn.cursor()

    # Display the city options
    c.execute("SELECT DISTINCT city FROM population")
    results = c.fetchall()
    cities = [r[0] for r in results]

    # Ask the user to pick a city to display simulation.
    print("\nAvailable Florida cities:")
    for i, city in enumerate(cities, 1):
        print(f"{i}. {city}")

    choice = int(input("\nChoose a city by number: "))
    selected_city = cities[choice - 1]


    # Get the population data.
    c.execute(
        "SELECT year, "
        "population FROM population WHERE city = ? ORDER BY year", 
        (selected_city,)
        )
    data = c.fetchall()

    # Format the table.
    years = [row[0] for row in data]
    pops = [row[1] for row in data]

    conn.close()

    # Display the data.
    plt.figure(figsize=(10, 5))
    plt.plot(years, pops, marker='o')
    plt.title(f"Population Growth for {selected_city}")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.grid(True)
    plt.show()



# Define the main function.
def main():
    create_db()
    simulate()
    plot_city_population()


# Run the main function.
main()