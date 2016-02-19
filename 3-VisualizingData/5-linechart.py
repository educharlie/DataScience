from matplotlib import pyplot as plt
import collections

variance = [1,2,4,8,16,32,64,128,256]
biasSquared = [256,128,64,32,16,8,4,2,1]
totalError = [x + y for x, y in zip(variance, biasSquared)]
xs = [i for i, _ in enumerate(variance)]

#we can make multiple calls to plt.plot to show multiple series on hte same chart
plt.plot(xs, variance, 'g-', label='variance') #green solid line
plt.plot(xs, biasSquared, 'r-.', label='bias^2') #red dot-dashed line
plt.plot(xs, totalError, 'b:.', label='total error') #blue dotted line

#because we've assigend labels to each series we can get a legend for free loc = 9 means "top center"
plt.legend(loc=9)
plt.xlabel("model complexity")
plt.title("The Bias-Variance Tradeoff")
plt.show()

