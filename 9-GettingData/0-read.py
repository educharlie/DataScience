import csv
import collections

names = collections.Counter()
with open('data.csv') as csvfile:
	for row in csv.reader(csvfile, delimiter=','):
		names[row[1]] += 1

print 'Number of Lee names: %s' % names['Lee']
#print grades.most_common()