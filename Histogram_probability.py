#Numeric Python library
import numpy as np


#Plotting library
from matplotlib import pyplot as plt



#Provide an estimate of the mean and standard deviation for a
#standard normal distribution.
mu, sigma = 0, 1



#Generate 1000 samples from the distribution.
s = np.random.normal(mu, sigma, 1000)



#Create a histogram containing the bins for the sample values (bins), the number of
#counts that fall into in each bin (n) and the shape and size of the rectangles
#of the histogram (patches).  Bins are really the x axis of the histogram and
#they actually represent ranges of the sample values taken from the distribution.
n, bins, patches = plt.hist(s,30, normed=True)



#Create a x-axis for the predicted probability density function.
x = np.linspace(min(bins), max(bins),1000)



#Add the predicted probability density function to the plot based on the values of the bins.
#This is for a standard normal distribution.
plt.plot(x, 1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (x - mu)**2 / (2 * sigma**2)),linewidth=2, color='r')



#Set the x boundaries based on the upper and lower limits of the bin values.  The y limit was set to the maximum
#value of the normalized bin count, n.  However, y could go up to a maximum probability value of 1 if needed.
#The minimum y axis limit is of course zero probability.
plt.xlim(min(bins), max(bins))
plt.ylim(0,max(n))



#X and Y axis labels.
plt.xlabel('Sample bin values')
plt.ylabel('Probability')



#Show both the normalized histogram of the data overlaid with the predicted probability density function.
plt.show()






