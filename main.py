h1 = ["apple", "pear", "orange"]
h2 = ["apple", "pear", "orange", "cherry"]
h3 = ["apple", "pear", "orange", "cherry", "banana"]
h4 = ["apple", "pear", "orange", "cherry", "banana", "grapes"]

data = ["apple", "pear", "apple", "orange", "cherry", "cherry", "orange", "banana"]

def p_d_given_h(h, d):
    if h.count(d) > 0:
        output = 0.9/len(h) + 0.01
        print(f"p of hypothesis given {d} is {str(output)}")
        return output
    else: return 0.01

def summation(data, h):
    output = 0
    for d in data:
        output += p_d_given_h(h, d)
        print(f"total p of h is {str(output)}")
    print("\n\n\n")
    return output/len(data)

prob_h1 = summation(data, h1)
prob_h2 = summation(data, h2)
prob_h3 = summation(data, h3)
prob_h4 = summation(data, h4)

print(f"h1 = {str(prob_h1)}")
print(f"h2 = {str(prob_h2)}")
print(f"h3 = {str(prob_h3)}")
print(f"h4 = {str(prob_h4)}")