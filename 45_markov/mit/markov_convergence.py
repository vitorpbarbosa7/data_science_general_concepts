# https://www.youtube.com/watch?v=IkbkEtOOC1Y&t=1842s
import matplotlib.pyplot as plt


def markov_simple_example(p11,p12,p21,p22,max_transitions=30):
	
	r11_nlast = p11
	r12_nlast = p12
	r21_nlast = p21
	r22_nlast = p22
	
	transitions = list(range(0,max_transitions))
	
	r11 = [1,p11]
	r12 = [0,p12]
	r21 = [0,p21]
	r22 = [1,p22]
	for n in transitions[2:]:
		r11n = r11_nlast*p11 + r12_nlast*p21
		r12n = r11_nlast*p12 + r12_nlast*p22
		r21n = r21_nlast*p11 + r22_nlast*p21
		r22n = r21_nlast*p12 + r22_nlast*p22
		
		# store the probability for each step
		r11.append(r11n)
		r12.append(r12n)
		r21.append(r21n)
		r22.append(r22n)
	
		# update, the last will now be this one calculated for this step
		# so we can go to next step and use this one as the last one
		r11_nlast = r11n
		r12_nlast = r12n
		r21_nlast = r21n
		r22_nlast = r22n
		
	# initial state is irrelevant, the probabilites will converge
	# Markov chain enters steady-state
	fig, ax = plt.subplots(4)
	ax[0].scatter(x = transitions, y = r11, s=0.2)
	ax[1].scatter(x = transitions, y = r12, s=0.2)
	ax[2].scatter(x = transitions, y = r21, s=0.2)
	ax[3].scatter(x = transitions, y = r22, s=0.2)
	fig.set_size_inches(12,8)
	plt.show()

#markov_simple_example(.5,.5,.2,.8)
markov_simple_example(.999,.001,.002,.998,max_transitions=10000)

