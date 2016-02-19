from matplotlib import pyplot as plt
import collections

friends = [70,65,72,63,71,64,60,64,67]
minutes = [175,170,205,120,220,130,105,145,190]
labels = ['a','b','c','d','e','f','g','h','i']

plt.scatter(friends,minutes)

#label each point
for label, friendCount, minuteCount in zip(labels, friends, minutes):
	plt.annotate(label,
		xy = (friendCount, minuteCount), #put the label with its point
		xytext = (5,-5), #but slightly offset
		textcoords = 'offset points')

plt.title("Daily Minutes vs Number of Friends")
plt.xlabel("# of friends")
plt.ylabel("Daily minutes spent on the site")
plt.show()