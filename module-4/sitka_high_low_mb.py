
import csv
from datetime import datetime

from matplotlib import pyplot as plt

# Identify the CSV weather data file.
filename = 'sitka_weather_2018_simple.csv'

# Read dates, high temperatures, and low temperatures from the file.
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []

    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(current_date)

        high = int(row[5])
        highs.append(high)

        low = int(row[6])
        lows.append(low)

# Display menu instructions and available options.
print("Welcome to the Sitka Weather Temperature Program!")
print("Select an option to view the temperature data.")

# Continue displaying the menu until the user chooses Exit.
while True:
    print("\n1. Highs")
    print("2. Lows")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == '1':
        # Display the high temperature graph in red.
        print("Displaying high temperatures...")
        fig, ax = plt.subplots()
        ax.plot(dates, highs, c='red')
        plt.title("Daily high temperatures - 2018", fontsize=24)

    elif choice == '2':
        # Display the low temperature graph in blue.
        print("Displaying low temperatures...")
        fig, ax = plt.subplots()
        ax.plot(dates, lows, c='blue')
        plt.title("Daily low temperatures - 2018", fontsize=24)

    elif choice == '3':
        # Display exit message and end the program.
        print("Thank you for using the Sitka Weather Program!")
        break

    else:
        # Handle invalid menu selections.
        print("Invalid selection. Please choose 1, 2, or 3.")

    if choice == '1' or choice == '2':
        # Format and display the selected temperature graph.
        plt.xlabel('', fontsize=16)
        fig.autofmt_xdate()
        plt.ylabel("Temperature (F)", fontsize=16)
        plt.tick_params(axis='both', which='major', labelsize=16)
        plt.show()