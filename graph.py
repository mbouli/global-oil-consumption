# Mason Boulier
# This code outputs a graph of our growing oil consumption.
# Oil is a finite resource and the world needs to pivot to using more renewable resources.

# Import plot library
import matplotlib.pyplot as plt
# Import data management library
import pandas as pd;

# Read CSV data file
cdf = pd.read_csv("oil_consumption.csv")

# Create range of years that we will use
years = range(1965, 2018)
# Create empty array 
consumption = []

# For each year in years array, append global consumption for that year.
for year in years:
    # Global usage in TWh (One trillion watt-hours)
    consumption.append(cdf.iloc[-1][str(year)])

fig, ax1 = plt.subplots()

# Plot consumption data
ax1.plot(years, consumption)
ax1.set_ylabel("Consumption (TWh)")

# Create title and labels
plt.title("Oil Consumption")
plt.xlabel('Year')
plt.grid(True)

# Show the plot
plt.show()