import numpy as np
from math import log, exp
import matplotlib.pyplot as plt

total_error_for_all_samples_single_stump = np.arange(0.01,1,0.01)
print(total_error_for_all_samples_single_stump)

def amount_of_say(error):

	# according to the error made by each stump, they will receive a weight of amount of say, 
	# which will be used in the final classification task, to weight their decisions	
	vote = (1/2)*log((1-error)/error)

	return vote

votes = [amount_of_say(error) for error in total_error_for_all_samples_single_stump]

#plt.scatter(x = total_error_for_all_samples_single_stump, y = votes)
#plt.xlabel('error')
#plt.ylabel('amount of say')
#plt.show()


def new_sample_weight(sample_weight, amount_of_say,sign:int):

	# if sign is positive, +1, then we are talking about the incorrectly classified sample, which will have their weight increased
	# if sign is negative, -1, then the weight will be decreased, since this was a correctly classified sample
	
	new_sample_weight = sample_weight*exp((sign)*amount_of_say)

	return new_sample_weight

new_sample_weights = [new_sample_weight(1/8,vote,-1) for vote in votes]

plt.scatter(x = votes, y = new_sample_weights)
plt.xlabel('amount of say')
plt.ylabel('new sample weight')
plt.show()
