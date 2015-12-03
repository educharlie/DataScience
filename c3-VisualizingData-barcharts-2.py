
from matplotlib import pyplot as plt

movies = ["Saw 1", "Spiderman", "Ironman", "Alicia en el pais de las maravillas", "Gandhi"]
numberOfOscars = [2,4,6,3,2]

# bars are by default width 0.8, so we'll add 0.1 to the left coordinates so that each bar is centered
xs = [i + 0.1 for i, _ in enumerate(movies)]

# plot bars with left x-coordinates [xs], heights [num_oscars]
plt.bar(xs, numberOfOscars)

plt.xlabel("Movies")
plt.ylabel("Number of Oscars")
plt.title("My favorite movies")

# label x-axis with movie names at bar centers
plt.xticks([i + 0.5 for i, _ in enumerate(movies)], movies)

plt.show()