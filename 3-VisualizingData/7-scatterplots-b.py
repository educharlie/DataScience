from matplotlib import pyplot as plt
import collections

testGrades1 = [99,90,85,97,80]
testGrades2 = [100,85,60,90,70]

plt.scatter(testGrades1, testGrades2)
plt.title("Axes aren't comparable")
plt.xlabel("test grades 1")
plt.ylabel("test grades 2")
plt.axis("equal") #to make it comparable
plt.show()