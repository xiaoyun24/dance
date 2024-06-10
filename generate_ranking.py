import numpy as np
import csv

# Set the means and standard deviations for the lists
means = [70]*15
std_devs = [0.5 ]*15
ranges = [(0,100)]*15




length = len(means)




# Define the correlation coefficient
correlation = 0.7

# Create the covariance matrix for 5 lists
cov_matrix = np.full((length, length), correlation * std_devs[0] * std_devs[1])
for i in range(length):
    for j in range(length):
        cov_matrix[i, j] = correlation * std_devs[i] * std_devs[j] if i != j else std_devs[i]**2

# Generate 100 samples from a multivariate normal distribution
samples = np.random.multivariate_normal(means, cov_matrix, 100)

# Split the samples into five lists and clip them to the specified ranges
lists = [np.clip(np.round(samples[:, i]), ranges[i][0], ranges[i][1]) for i in range(length)]








print(lists)





# score_list = [jbg_score, ztq_score, gj_score, tj_score, sz_score, total_score]

# # Plot the distributions
# plt.figure(figsize=(18, 10))

# for i, lst in enumerate(score_list, 1):
#     plt.subplot(2, 3, i)
#     plt.hist(lst, bins=20, edgecolor='black')
#     plt.title(f'Histogram of List {i}')
#     plt.xlabel('Number')
#     plt.ylabel('Frequency')

# plt.tight_layout()
# plt.show()

# # Print the generated lists
# for i, lst in enumerate(score_list, 1):
#     print(f"List {i}: {lst}")
