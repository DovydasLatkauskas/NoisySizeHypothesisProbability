h1 = ["apple", "pear", "orange"]
h2 = ["apple", "pear", "orange", "cherry"]
h3 = ["apple", "pear", "orange", "cherry", "banana"]
h4 = ["apple", "pear", "orange", "cherry", "banana", "grapes"]

# add hypotheses here
hypotheses = [h1,h2,h3,h4]

# add data for testing the hypotheses here
data = ["apple", "pear", "apple", "orange", "cherry", "cherry", "orange", "banana"]

def p_d_given_h(h, d): # calculates the probability of hypothesis h given a single data point d
    if h.count(d) > 0:
        output = 0.9/len(h) + 0.01
        #print(f"p of hypothesis given {d} is {str(output)}")
        return output
    else: return 0.01

def summation(data, h): # calculates the sum of probabilities given each data point for a hypothesis h and divides is by the length of data
    output = 0
    for d in data:
        output += p_d_given_h(h, d)
        #print(f"total p of h is {str(output)}")
    #print("\n\n\n")
    return output/len(data)

list_of_probabilities = [] # list containing the probability of each hypothesis to be true given dataset "data"
for h in hypotheses:
    list_of_probabilities.append(summation(data, h))

