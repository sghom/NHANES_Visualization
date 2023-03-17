import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

r = 1
mean = [15, 5]
cov = [[1, r], [r, 1]]
x, y = x, y = np.random.multivariate_normal(mean, cov, 400).T

plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.hist(x = x, bins= 15)
plt.title("X")

plt.subplot(1,2,2)
plt.hist(x = y, bins= 15)
plt.title("Y")

plt.show()

# Plot the data
plt.figure(figsize=(10,10))
plt.subplot(2,2,2)
plt.scatter(x = x, y = y)
plt.title("Joint Distribution of X and Y")

# Plot the Marginal X Distribution
plt.subplot(2,2,4)
plt.hist(x = x, bins = 15)
plt.title("Marginal Distribution of X")


# Plot the Marginal Y Distribution
plt.subplot(2,2,1)
plt.hist(x = y, orientation = "horizontal", bins = 15)
plt.title("Marginal Distribution of Y")

# Show the plots
plt.show()