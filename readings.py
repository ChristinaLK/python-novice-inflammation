import sys
import numpy

script = sys.argv[0]
action = sys.argv[1]
filename = sys.argv[2]

def reading(action, filename):
    data = numpy.loadtxt(filename, delimiter=",")
    if action == '--mean':
        value = data.mean(axis = 1)
    elif action == '--std':
        value = data.std(axis = 1)
    else: 
        value = "Option not supported"
    print(value)

reading(action, filename)
