#Python: Create a list by concatenating a given list which range goes from 1 to n
"""
Sample list : ['p', 'q']
n =5
Sample Output : ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']
"""

alpha_strings =  ['p', 'q']
numeric = 5
def concat(alpha_strings,numeric):
    result = ['{}{}'.format(x,y) for y in range(numeric) for x in alpha_strings]
    return result

print(concat(alpha_strings,numeric))