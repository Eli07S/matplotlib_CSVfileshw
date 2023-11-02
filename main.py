#CSV FILE GRAPH HW
#Eli.SK

import matplotlib.pyplot as plt
import csv
x = []
y = []

#Data Graph #1
with open('snakes_count_10.csv') as csvfile:
    csvplots = csv.reader(csvfile, delimiter=',')

    for row in csvplots:
        x.append(row[0])
        y.append(row[1])

plt.bar(x, y)
plt.ylabel("game length")
plt.xlabel("game number")
plt.title("Snakes and ladders")
plt.show()

#Data Graph #2
with open('tally_cab.csv') as csvfile:
    csvplots = csv.reader(csvfile, delimiter=',')

    for row in csvplots:
        x.append(row[0])
        y.append(row[1])

plt.bar(x, y)
plt.ylabel("Fare($)")
plt.xlabel("Distance(Miles)")
plt.title("Cabs in tallahasy")
plt.show()