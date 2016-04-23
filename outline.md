---

layout: page

title: Programming with Python

subtitle: Analyzing Patient Data

minutes: 30

---

> ## Learning Objectives {.objectives}

>

> *   Explain what a library is, and what libraries are used for.

> *   Load a Python library and use the things it contains.

> *   Read tabular data from a file into a program.

> *   Assign values to variables.

> *   Select individual values and subsections from data.

> *   Perform operations on arrays of data.

> *   Display simple graphs.



Words are useful,

but what's more useful are the sentences and stories we build with them.

Similarly,

while a lot of powerful tools are built into languages like Python,

even more live in the [libraries](reference.html#library) they are used to build.



In order to load our inflammation data,

we need to [import](reference.html#import) a library called NumPy.

In general you should use this library if you want to do fancy things with numbers,

especially if you have matrices or arrays.

We can load NumPy using:



~~~ {.python}

import numpy

~~~

~~~ {.python}

numpy.loadtxt(fname='inflammation-01.csv', delimiter=',')

~~~

~~~ {.python}

weight_kg = 55

~~~

~~~ {.python}

print(weight_kg)

~~~

~~~ {.python}

print('weight in pounds:', 2.2 * weight_kg)

~~~

~~~ {.python}

weight_kg = 57.5

print('weight in kilograms is now:', weight_kg)

~~~

~~~ {.python}

weight_lb = 2.2 * weight_kg

print('weight in kilograms:', weight_kg, 'and in pounds:', weight_lb)

~~~

~~~ {.python}

weight_kg = 100.0

print('weight in kilograms is now:', weight_kg, 'and weight in pounds is still:', weight_lb)

~~~

~~~ {.python}

data = numpy.loadtxt(fname='inflammation-01.csv', delimiter=',')

~~~

~~~ {.python}

print(data)

~~~

~~~ {.python}

print(type(data))

~~~

~~~ {.python}

print(data.shape)

~~~

~~~ {.python}

print('first value in data:', data[0, 0])

~~~

~~~ {.python}

print('middle value in data:', data[30, 20])

~~~

~~~ {.python}

print(data[0:4, 0:10])

~~~

~~~ {.python}

print(data[5:10, 0:10])

~~~

~~~ {.python}

small = data[:3, 36:]

print('small is:')

print(small)

~~~

~~~ {.python}

doubledata = data * 2.0

~~~

~~~ {.python}

print('original:')

print(data[:3, 36:])

print('doubledata:')

print(doubledata[:3, 36:])

~~~

~~~ {.python}

tripledata = doubledata + data

~~~

~~~ {.python}

print('tripledata:')

print(tripledata[:3, 36:])

~~~

~~~ {.python}

print(data.mean())

~~~

~~~ {.python}

print('maximum inflammation:', data.max())

print('minimum inflammation:', data.min())

print('standard deviation:', data.std())

~~~

~~~ {.python}

patient_0 = data[0, :] # 0 on the first axis, everything on the second

print('maximum inflammation for patient 0:', patient_0.max())

~~~

~~~ {.python}

print('maximum inflammation for patient 2:', data[2, :].max())

~~~

~~~ {.python}

print(data.mean(axis=0))

~~~

~~~ {.python}

print(data.mean(axis=0).shape)

~~~

~~~ {.python}

print(data.mean(axis=1))

~~~

~~~ {.python}

import matplotlib.pyplot

image  = matplotlib.pyplot.imshow(data)

matplotlib.pyplot.show()

~~~

~~~ {.python}

ave_inflammation = data.mean(axis=0)

ave_plot = matplotlib.pyplot.plot(ave_inflammation)

matplotlib.pyplot.show()

~~~

~~~ {.python}

max_plot = matplotlib.pyplot.plot(data.max(axis=0))

matplotlib.pyplot.show()

~~~

~~~ {.python}

min_plot = matplotlib.pyplot.plot(data.min(axis=0))

matplotlib.pyplot.show()

~~~

~~~ {.python}

import numpy

import matplotlib.pyplot



data = numpy.loadtxt(fname='inflammation-01.csv', delimiter=',')



fig = matplotlib.pyplot.figure(figsize=(10.0, 3.0))



axes1 = fig.add_subplot(1, 3, 1)

axes2 = fig.add_subplot(1, 3, 2)

axes3 = fig.add_subplot(1, 3, 3)



axes1.set_ylabel('average')

axes1.plot(data.mean(axis=0))



axes2.set_ylabel('max')

axes2.plot(data.max(axis=0))



axes3.set_ylabel('min')

axes3.plot(data.min(axis=0))



fig.tight_layout()



matplotlib.pyplot.show()

~~~

---

layout: page

title: Programming with Python

subtitle: Repeating Actions with Loops

minutes: 30

---

> ## Learning Objectives {.objectives}

>

> *   Explain what a for loop does.

> *   Correctly write for loops to repeat simple calculations.

> *   Trace changes to a loop variable as the loop runs.

> *   Trace changes to other variables as they are updated by a for loop.



In the last lesson,

we wrote some code that plots some values of interest from our first inflammation dataset,

and reveals some suspicious features in it, such as from `inflammation-01.csv`



![Analysis of inflammation-01.csv](fig/03-loop_2_0.png)\



We have a dozen data sets right now, though, and more on the way.

We want to create plots for all of our data sets with a single statement.

To do that, we'll have to teach the computer how to repeat things.



An example task that we might want to repeat is printing each character in a

word on a line of its own. One way to do this would be to use a series of `print` statements:



~~~ {.python}

word = 'lead'

print(word[0])

print(word[1])

print(word[2])

print(word[3])



~~~

~~~ {.python}

word = 'tin'

print(word[0])

print(word[1])

print(word[2])

print(word[3])



~~~

~~~ {.python}

word = 'lead'

for char in word:

    print(char)



~~~

~~~ {.python}

word = 'oxygen'

for char in word:

    print(char)

~~~

~~~ {.python}

for variable in collection:

    do things with variable

~~~

~~~ {.python}

length = 0

for vowel in 'aeiou':

    length = length + 1

print('There are', length, 'vowels')

~~~

~~~ {.python}

letter = 'z'

for letter in 'abc':

    print(letter)

print('after the loop, letter is', letter)

~~~

~~~ {.python}

print(len('aeiou'))

~~~

---

layout: page

title: Programming with Python

subtitle: Storing Multiple Values in Lists

minutes: 30

---

> ## Learning Objectives {.objectives}

>

> *   Explain what a list is.

> *   Create and index lists of simple values.



Just as a `for` loop is a way to do operations many times,

a list is a way to store many values.

Unlike NumPy arrays,

lists are built into the language (so we don't have to load a library

to use them).

We create a list by putting values inside square brackets:



~~~ {.python}

odds = [1, 3, 5, 7]

print('odds are:', odds)

~~~

~~~ {.python}

print('first and last:', odds[0], odds[-1])

~~~

~~~ {.python}

for number in odds:

    print(number)

~~~

~~~ {.python}

names = ['Newton', 'Darwing', 'Turing'] # typo in Darwin's name

print('names is originally:', names)

names[1] = 'Darwin' # correct the name

print('final value of names:', names)

~~~

~~~ {.python}

name = 'Bell'

name[0] = 'b'

~~~

~~~ {.python}

odds.append(11)

print('odds after adding a value:', odds)

~~~

~~~ {.python}

del odds[0]

print('odds after removing the first element:', odds)

~~~

~~~ {.python}

odds.reverse()

print('odds after reversing:', odds)

~~~

~~~ {.python}

odds = [1, 3, 5, 7]

primes = odds

primes += [2]

print('primes:', primes)

print('odds:', odds)

~~~

~~~ {.python}

odds = [1, 3, 5, 7]

primes = list(odds)

primes += [2]

print('primes:', primes)

print('odds:', odds)

~~~

---

layout: page

title: Programming with Python

subtitle: Analyzing Data from Multiple Files

minutes: 20

---

> ## Learning Objectives {.objectives}

>

> *   Use a library function to get a list of filenames that match a simple wildcard pattern.

> *   Use a for loop to process multiple files.



We now have almost everything we need to process all our data files.

The only thing that's missing is a library with a rather unpleasant name:



~~~ {.python}

import glob

~~~

~~~ {.python}

print(glob.glob('data/inflammation*.csv'))

~~~

~~~ {.python}

import numpy

import matplotlib.pyplot



filenames = glob.glob('data/inflammation*.csv')

filenames = filenames[0:3]

for f in filenames:

    print(f)



    data = numpy.loadtxt(fname=f, delimiter=',')



    fig = matplotlib.pyplot.figure(figsize=(10.0, 3.0))



    axes1 = fig.add_subplot(1, 3, 1)

    axes2 = fig.add_subplot(1, 3, 2)

    axes3 = fig.add_subplot(1, 3, 3)



    axes1.set_ylabel('average')

    axes1.plot(data.mean(axis=0))



    axes2.set_ylabel('max')

    axes2.plot(data.max(axis=0))



    axes3.set_ylabel('min')

    axes3.plot(data.min(axis=0))



    fig.tight_layout()

    matplotlib.pyplot.show()

~~~

---

layout: page

title: Programming with Python

subtitle: Making Choices

minutes: 30

---

> ## Learning Objectives {.objectives}

>

> *   Explain the similarities and differences between tuples and lists.

> *   Write conditional statements including `if`, `elif`, and `else` branches.

> *   Correctly evaluate expressions containing `and` and `or`.



In our last lesson, we discovered something suspicious was going on

in our inflammation data by drawing some plots.

How can we use Python to automatically recognize the different features we saw,

and take a different action for each? In this lesson, we'll learn how to write code that

runs only when certain conditions are true.



## Conditionals



We can ask Python to take different actions, depending on a condition, with an `if` statement:



~~~ {.python}

num = 37

if num > 100:

    print('greater')

else:

    print('not greater')

print('done')

~~~

~~~ {.python}

num = 53

print('before conditional...')

if num > 100:

    print('53 is greater than 100')

print('...after conditional')

~~~

~~~ {.python}

num = -3



if num > 0:

    print(num, "is positive")

elif num == 0:

    print(num, "is zero")

else:

    print(num, "is negative")

~~~

~~~ {.python}

if (1 > 0) and (-1 > 0):

    print('both parts are true')

else:

    print('at least one part is false')

~~~

~~~ {.python}

if (1 < 0) or (-1 < 0):

    print('at least one test is true')

~~~

~~~ {.python}

if data.max(axis=0)[0] == 0 and data.max(axis=0)[20] == 20:

    print('Suspicious looking maxima!')

~~~

~~~ {.python}

else:

    print('Seems OK!')

~~~

~~~ {.python}

data = numpy.loadtxt(fname='inflammation-01.csv', delimiter=',')

if data.max(axis=0)[0] == 0 and data.max(axis=0)[20] == 20:

    print('Suspicious looking maxima!')

elif data.min(axis=0).sum() == 0:

    print('Minima add up to zero!')

else:

    print('Seems OK!')

~~~

~~~ {.python}

data = numpy.loadtxt(fname='inflammation-03.csv', delimiter=',')

if data.max(axis=0)[0] == 0 and data.max(axis=0)[20] == 20:

    print('Suspicious looking maxima!')

elif data.min(axis=0).sum() == 0:

    print('Minima add up to zero!')

else:

    print('Seems OK!')

~~~

---

layout: page

title: Programming with Python

subtitle: Creating Functions

minutes: 30

---

> ## Learning Objectives {.objectives}

>

> *   Define a function that takes parameters.

> *   Return a value from a function.

> *   Test and debug a function.

> *   Set default values for function parameters.

> *   Explain why we should divide programs into small, single-purpose functions.



At this point,

we've written code to draw some interesting features in our inflammation data,

loop over all our data files to quickly draw these plots for each of them,

and have Python make decisions based on what it sees in our data.

But, our code is getting pretty long and complicated;

what if we had thousands of datasets,

and didn't want to generate a figure for every single one?

Commenting out the figure-drawing code is a nuisance.

Also, what if we want to use that code again,

on a different dataset or at a different point in our program?

Cutting and pasting it is going to make our code get very long and very repetitive,

very quickly.

We'd like a way to package our code so that it is easier to reuse,

and Python provides for this by letting us define things called 'functions' -

a shorthand way of re-executing longer pieces of code.



Let's start by defining a function `fahr_to_kelvin` that converts temperatures from Fahrenheit to Kelvin:



~~~ {.python}

def fahr_to_kelvin(temp):

    return ((temp - 32) * (5/9)) + 273.15

~~~

~~~ {.python}

print('freezing point of water:', fahr_to_kelvin(32))

print('boiling point of water:', fahr_to_kelvin(212))

~~~

~~~ {.python}

def kelvin_to_celsius(temp_k):

    return temp_k - 273.15



print('absolute zero in Celsius:', kelvin_to_celsius(0.0))

~~~

~~~ {.python}

def fahr_to_celsius(temp_f):

    temp_k = fahr_to_kelvin(temp_f)

    result = kelvin_to_celsius(temp_k)

    return result



print('freezing point of water in Celsius:', fahr_to_celsius(32.0))

~~~

~~~ {.python}

def analyze(filename):



    data = numpy.loadtxt(fname=filename, delimiter=',')



    fig = matplotlib.pyplot.figure(figsize=(10.0, 3.0))



    axes1 = fig.add_subplot(1, 3, 1)

    axes2 = fig.add_subplot(1, 3, 2)

    axes3 = fig.add_subplot(1, 3, 3)



    axes1.set_ylabel('average')

    axes1.plot(data.mean(axis=0))



    axes2.set_ylabel('max')

    axes2.plot(data.max(axis=0))



    axes3.set_ylabel('min')

    axes3.plot(data.min(axis=0))



    fig.tight_layout()

    matplotlib.pyplot.show()

~~~

~~~ {.python}

def detect_problems(filename):



    data = numpy.loadtxt(fname=filename, delimiter=',')



    if data.max(axis=0)[0] == 0 and data.max(axis=0)[20] == 20:

        print('Suspicious looking maxima!')

    elif data.min(axis=0).sum() == 0:

        print('Minima add up to zero!')

    else:

        print('Seems OK!')

~~~

~~~ {.python}

for f in filenames[:3]:

    print(f)

    analyze(f)

    detect_problems(f)

~~~

~~~ {.python}

def center(data, desired):

    return (data - data.mean()) + desired

~~~

~~~ {.python}

z = numpy.zeros((2,2))

print(center(z, 3))

~~~

~~~ {.python}

data = numpy.loadtxt(fname='inflammation-01.csv', delimiter=',')

print(center(data, 0))

~~~

~~~ {.python}

print('original min, mean, and max are:', data.min(), data.mean(), data.max())

centered = center(data, 0)

print('min, mean, and and max of centered data are:', centered.min(), centered.mean(), centered.max())

~~~

~~~ {.python}

print('std dev before and after:', data.std(), centered.std())

~~~

~~~ {.python}

print('difference in standard deviations before and after:', data.std() - centered.std())

~~~

~~~ {.python}

# center(data, desired): return a new array containing the original data centered around the desired value.

def center(data, desired):

    return (data - data.mean()) + desired

~~~

~~~ {.python}

def center(data, desired):

    '''Return a new array containing the original data centered around the desired value.'''

    return (data - data.mean()) + desired

~~~

~~~ {.python}

help(center)

~~~

~~~ {.python}

def center(data, desired):

    '''Return a new array containing the original data centered around the desired value.

    Example: center([1, 2, 3], 0) => [-1, 0, 1]'''

    return (data - data.mean()) + desired



help(center)

~~~

~~~ {.python}

numpy.loadtxt('inflammation-01.csv', delimiter=',')

~~~

~~~ {.python}

numpy.loadtxt('inflammation-01.csv', ',')

~~~

~~~ {.python}

def center(data, desired=0.0):

    '''Return a new array containing the original data centered around the desired value (0 by default).

    Example: center([1, 2, 3], 0) => [-1, 0, 1]'''

    return (data - data.mean()) + desired

~~~

~~~ {.python}

test_data = numpy.zeros((2, 2))

print(center(test_data, 3))

~~~

~~~ {.python}

more_data = 5 + numpy.zeros((2, 2))

print('data before centering:')

print(more_data)

print('centered data:')

print(center(more_data))

~~~

~~~ {.python}

def display(a=1, b=2, c=3):

    print('a:', a, 'b:', b, 'c:', c)



print('no parameters:')

display()

print('one parameter:')

display(55)

print('two parameters:')

display(55, 66)

~~~

~~~ {.python}

print('only setting the value of c')

display(c=77)

~~~

~~~ {.python}

help(numpy.loadtxt)

~~~

~~~ {.python}

numpy.loadtxt('inflammation-01.csv', ',')

~~~

---

layout: page

title: Programming with Python

subtitle: Errors and Exceptions

minutes: 30

---

> ## Learning Objectives {.objectives}

>

> *   To be able to read a traceback, and determine the following relevant pieces of information:

>     * The file, function, and line number on which the error occurred

>     * The type of the error

>     * The error message

> *   To be able to describe the types of situations in which the following errors occur:

>     * `SyntaxError` and `IndentationError`

>     * `NameError`

>     * `IndexError`

>     * `FileNotFoundError`



Every programmer encounters errors,

both those who are just beginning,

and those who have been programming for years.

Encountering errors and exceptions can be very frustrating at times,

and can make coding feel like a hopeless endeavour.

However,

understanding what the different types of errors are

and when you are likely to encounter them can help a lot.

Once you know *why* you get certain types of errors,

they become much easier to fix.



Errors in Python have a very specific form,

called a [traceback](reference.html#traceback).

Let's examine one:



~~~ {.python}

import errors_01

errors_01.favorite_ice_cream()

~~~

~~~ {.python}

def some_function()

    msg = "hello, world!"

    print(msg)

     return msg

~~~

~~~ {.python}

def some_function():

    msg = "hello, world!"

    print(msg)

     return msg

~~~

~~~ {.python}

print(a)

~~~

~~~ {.python}

print(hello)

~~~

~~~ {.python}

for number in range(10):

    count = count + number

print("The count is: " + str(count))

~~~

~~~ {.python}

Count = 0

for number in range(10):

    count = count + number

print("The count is: " + str(count))

~~~

~~~ {.python}

letters = ['a', 'b', 'c']

print("Letter #1 is " + letters[0])

print("Letter #2 is " + letters[1])

print("Letter #3 is " + letters[2])

print("Letter #4 is " + letters[3])

~~~

~~~ {.python}

file_handle = open('myfile.txt', 'r')

~~~

~~~ {.python}

file_handle = open('myfile.txt', 'w')

file_handle.read()

~~~

---

layout: page

title: Programming with Python

subtitle: Defensive Programming

minutes: 30

---

> ## Learning Objectives {.objectives}

>

> *   Explain what an assertion is.

> *   Add assertions that check the program's state is correct.

> *   Correctly add precondition and postcondition assertions to functions.

> *   Explain what test-driven development is, and use it when creating new functions.

> *   Explain why variables should be initialized using actual data values rather than arbitrary constants.



Our previous lessons have introduced the basic tools of programming:

variables and lists,

file I/O,

loops,

conditionals,

and functions.

What they *haven't* done is show us how to tell

whether a program is getting the right answer,

and how to tell if it's *still* getting the right answer

as we make changes to it.



To achieve that,

we need to:



*   Write programs that check their own operation.

*   Write and run tests for widely-used functions.

*   Make sure we know what "correct" actually means.



The good news is,

doing these things will speed up our programming,

not slow it down.

As in real carpentry --- the kind done with lumber --- the time saved

by measuring carefully before cutting a piece of wood

is much greater than the time that measuring takes.



## Assertions



The first step toward getting the right answers from our programs

is to assume that mistakes *will* happen

and to guard against them.

This is called [defensive programming](reference.html#defensive-programming),

and the most common way to do it is to add [assertions](reference.html#assertion) to our code

so that it checks itself as it runs.

An assertion is simply a statement that something must be true at a certain point in a program.

When Python sees one,

it evaluates the assertion's condition.

If it's true,

Python does nothing,

but if it's false,

Python halts the program immediately

and prints the error message if one is provided.

For example,

this piece of code halts as soon as the loop encounters a value that isn't positive:



~~~ {.python}

numbers = [1.5, 2.3, 0.7, -0.001, 4.4]

total = 0.0

for n in numbers:

    assert n > 0.0, 'Data should only contain positive values'

    total += n

print('total is:', total)

~~~

~~~ {.python}

def normalize_rectangle(rect):

    '''Normalizes a rectangle so that it is at the origin and 1.0 units long on its longest axis.'''

    assert len(rect) == 4, 'Rectangles must contain 4 coordinates'

    x0, y0, x1, y1 = rect

    assert x0 < x1, 'Invalid X coordinates'

    assert y0 < y1, 'Invalid Y coordinates'



    dx = x1 - x0

    dy = y1 - y0

    if dx > dy:

        scaled = float(dx) / dy

        upper_x, upper_y = 1.0, scaled

    else:

        scaled = float(dx) / dy

        upper_x, upper_y = scaled, 1.0



    assert 0 < upper_x <= 1.0, 'Calculated upper X coordinate invalid'

    assert 0 < upper_y <= 1.0, 'Calculated upper Y coordinate invalid'



    return (0, 0, upper_x, upper_y)

~~~

~~~ {.python}

print(normalize_rectangle( (0.0, 1.0, 2.0) )) # missing the fourth coordinate

~~~

~~~ {.python}

print(normalize_rectangle( (4.0, 2.0, 1.0, 5.0) )) # X axis inverted

~~~

~~~ {.python}

print(normalize_rectangle( (0.0, 0.0, 1.0, 5.0) ))

~~~

~~~ {.python}

print(normalize_rectangle( (0.0, 0.0, 5.0, 1.0) ))

~~~

~~~ {.python}

assert range_overlap([ (0.0, 1.0) ]) == (0.0, 1.0)

assert range_overlap([ (2.0, 3.0), (2.0, 4.0) ]) == (2.0, 3.0)

assert range_overlap([ (0.0, 1.0), (0.0, 2.0), (-1.0, 1.0) ]) == (0.0, 1.0)

~~~

~~~ {.python}

assert range_overlap([ (0.0, 1.0), (5.0, 6.0) ]) == ???

~~~

~~~ {.python}

assert range_overlap([ (0.0, 1.0), (1.0, 2.0) ]) == ???

~~~

~~~ {.python}

assert range_overlap([ (0.0, 1.0), (5.0, 6.0) ]) == None

assert range_overlap([ (0.0, 1.0), (1.0, 2.0) ]) == None

~~~

~~~ {.python}

def range_overlap(ranges):

    '''Return common overlap among a set of [low, high] ranges.'''

    lowest = 0.0

    highest = 1.0

    for (low, high) in ranges:

        lowest = max(lowest, low)

        highest = min(highest, high)

    return (lowest, highest)

~~~

~~~ {.python}

def test_range_overlap():

    assert range_overlap([ (0.0, 1.0), (5.0, 6.0) ]) == None

    assert range_overlap([ (0.0, 1.0), (1.0, 2.0) ]) == None

    assert range_overlap([ (0.0, 1.0) ]) == (0.0, 1.0)

    assert range_overlap([ (2.0, 3.0), (2.0, 4.0) ]) == (2.0, 3.0)

    assert range_overlap([ (0.0, 1.0), (0.0, 2.0), (-1.0, 1.0) ]) == (0.0, 1.0)

~~~

~~~ {.python}

test_range_overlap()

~~~

---

layout: page

title: Programming with Python

subtitle: Debugging

minutes: 30

---

> ## Learning Objectives {.objectives}

>

> *   Debug code containing an error systematically.



Once testing has uncovered problems,

the next step is to fix them.

Many novices do this by making more-or-less random changes to their code

until it seems to produce the right answer,

but that's very inefficient

(and the result is usually only correct for the one case they're testing).

The more experienced a programmer is,

the more systematically they debug,

and most follow some variation on the rules explained below.



## Know What It's Supposed to Do



The first step in debugging something is to

*know what it's supposed to do*.

"My program doesn't work" isn't good enough:

in order to diagnose and fix problems,

we need to be able to tell correct output from incorrect.

If we can write a test case for the failing case --- i.e.,

if we can assert that with *these* inputs,

the function should produce *that* result ---

then we're ready to start debugging.

If we can't,

then we need to figure out how we're going to know when we've fixed things.



But writing test cases for scientific software is frequently harder than

writing test cases for commercial applications,

because if we knew what the output of the scientific code was supposed to be,

we wouldn't be running the software:

we'd be writing up our results and moving on to the next program.

In practice,

scientists tend to do the following:



1.  *Test with simplified data.*

    Before doing statistics on a real data set,

    we should try calculating statistics for a single record,

    for two identical records,

    for two records whose values are one step apart,

    or for some other case where we can calculate the right answer by hand.



2.  *Test a simplified case.*

    If our program is supposed to simulate

    magnetic eddies in rapidly-rotating blobs of supercooled helium,

    our first test should be a blob of helium that isn't rotating,

    and isn't being subjected to any external electromagnetic fields.

    Similarly,

    if we're looking at the effects of climate change on speciation,

    our first test should hold temperature, precipitation, and other factors constant.



3.  *Compare to an oracle.*

    A [test oracle](reference.html#test-oracle) is something whose results are trusted,

    such as experimental data, an older program, or a human expert.

    We use to test oracles to determine if our new program produces the correct results.

    If we have a test oracle,

    we should store its output for particular cases

    so that we can compare it with our new results as often as we like

    without re-running that program.



4.  *Check conservation laws.*

    Mass, energy, and other quantitites are conserved in physical systems,

    so they should be in programs as well.

    Similarly,

    if we are analyzing patient data,

    the number of records should either stay the same or decrease

    as we move from one analysis to the next

    (since we might throw away outliers or records with missing values).

    If "new" patients start appearing out of nowhere as we move through our pipeline,

    it's probably a sign that something is wrong.



5.  *Visualize.*

    Data analysts frequently use simple visualizations to check both

    the science they're doing

    and the correctness of their code

    (just as we did in the [opening lesson](01-numpy.html) of this tutorial).

    This should only be used for debugging as a last resort,

    though,

    since it's very hard to compare two visualizations automatically.



## Make It Fail Every Time



We can only debug something when it fails,

so the second step is always to find a test case that

*makes it fail every time*.

The "every time" part is important because

few things are more frustrating than debugging an intermittent problem:

if we have to call a function a dozen times to get a single failure,

the odds are good that we'll scroll past the failure when it actually occurs.



As part of this,

it's always important to check that our code is "plugged in",

i.e.,

that we're actually exercising the problem that we think we are.

Every programmer has spent hours chasing a bug,

only to realize that they were actually calling their code on the wrong data set

or with the wrong configuration parameters,

or are using the wrong version of the software entirely.

Mistakes like these are particularly likely to happen when we're tired,

frustrated,

and up against a deadline,

which is one of the reasons late-night (or overnight) coding sessions

are almost never worthwhile.



## Make It Fail Fast



If it takes 20 minutes for the bug to surface,

we can only do three experiments an hour.

That doesn't just mean we'll get less data in more time:

we're also more likely to be distracted by other things as we wait for our program to fail,

which means the time we *are* spending on the problem is less focused.

It's therefore critical to *make it fail fast*.



As well as making the program fail fast in time,

we want to make it fail fast in space,

i.e.,

we want to localize the failure to the smallest possible region of code:



1.  The smaller the gap between cause and effect,

    the easier the connection is to find.

    Many programmers therefore use a divide and conquer strategy to find bugs,

    i.e.,

    if the output of a function is wrong,

    they check whether things are OK in the middle,

    then concentrate on either the first or second half,

    and so on.



2.  N things can interact in N<sup>2</sup> different ways,

    so every line of code that *isn't* run as part of a test

    means more than one thing we don't need to worry about.



## Change One Thing at a Time, For a Reason



Replacing random chunks of code is unlikely to do much good.

(After all,

if you got it wrong the first time,

you'll probably get it wrong the second and third as well.)

Good programmers therefore

*change one thing at a time, for a reason*

They are either trying to gather more information

("is the bug still there if we change the order of the loops?")

or test a fix

("can we make the bug go away by sorting our data before processing it?").



Every time we make a change,

however small,

we should re-run our tests immediately,

because the more things we change at once,

the harder it is to know what's responsible for what

(those N<sup>2</sup> interactions again).

And we should re-run *all* of our tests:

more than half of fixes made to code introduce (or re-introduce) bugs,

so re-running all of our tests tells us whether we have regressed.



## Keep Track of What You've Done



Good scientists keep track of what they've done

so that they can reproduce their work,

and so that they don't waste time repeating the same experiments

or running ones whose results won't be interesting.

Similarly,

debugging works best when we

*keep track of what we've done*

and how well it worked.

If we find ourselves asking,

"Did left followed by right with an odd number of lines cause the crash?

Or was it right followed by left?

Or was I using an even number of lines?"

then it's time to step away from the computer,

take a deep breath,

and start working more systematically.



Records are particularly useful when the time comes to ask for help.

People are more likely to listen to us

when we can explain clearly what we did,

and we're better able to give them the information they need to be useful.



> ## Version Control Revisited {.callout}

>

> Version control is often used to reset software to a known state during debugging,

> and to explore recent changes to code that might be responsible for bugs.

> In particular,

> most version control systems have a `blame` command

> that will show who last changed particular lines of code...



## Be Humble



And speaking of help:

if we can't find a bug in 10 minutes,

we should *be humble* and ask for help.

Just explaining the problem aloud is often useful,

since hearing what we're thinking helps us spot inconsistencies and hidden assumptions.



Asking for help also helps alleviate confirmation bias.

If we have just spent an hour writing a complicated program,

we want it to work,

so we're likely to keep telling ourselves why it should,

rather than searching for the reason it doesn't.

People who aren't emotionally invested in the code can be more objective,

which is why they're often able to spot the simple mistakes we have overlooked.



Part of being humble is learning from our mistakes.

Programmers tend to get the same things wrong over and over:

either they don't understand the language and libraries they're working with,

or their model of how things work is wrong.

In either case,

taking note of why the error occurred

and checking for it next time

quickly turns into not making the mistake at all.



And that is what makes us most productive in the long run.

As the saying goes,

*A week of hard work can sometimes save you an hour of thought*.

If we train ourselves to avoid making some kinds of mistakes,

to break our code into modular, testable chunks,

and to turn every assumption (or mistake) into an assertion,

it will actually take us *less* time to produce working programs,

not more.



> ## Debug with a neighbor {.challenge}

>

> Take a function that you have written today, and introduce a tricky bug.

> Your function should still run, but will give the wrong output.

> Switch seats with your neighbor and attempt to debug

> the bug that they introduced into their function.

> Which of the principles discussed above did you find helpful?

---

layout: page

title: Programming with Python

subtitle: Command-Line Programs

minutes: 30

---

> ## Learning Objectives {.objectives}

>

> *   Use the values of command-line arguments in a program.

> *   Handle flags and files separately in a command-line program.

> *   Read data from standard input in a program so that it can be used in a pipeline.



The IPython Notebook and other interactive tools are great for prototyping code and exploring data,

but sooner or later we will want to use our program in a pipeline

or run it in a shell script to process thousands of data files.

In order to do that,

we need to make our programs work like other Unix command-line tools.

For example,

we may want a program that reads a dataset

and prints the average inflammation per patient.



> ## Switching to Shell Commands {.callout}

> In this lesson we are switching from typing commands in a Python interpreter to typing

> commands in a shell terminal window (such as bash). When you see a `$` in front of a

> command that tells you to run that command in the shell rather than the Python interpreter.



This program does exactly what we want - it prints the average inflammation per patient

for a given file.



~~~ {.bash}

$ python readings.py --mean inflammation-01.csv

5.45

5.425

6.1

...

6.4

7.05

5.9

~~~

~~~ {.python}

import sys

print('version is', sys.version)

~~~

~~~ {.python}

import sys

print('sys.argv is', sys.argv)

~~~

~~~ {.python}

import sys

import numpy



def main():

    script = sys.argv[0]

    filename = sys.argv[1]

    data = numpy.loadtxt(filename, delimiter=',')

    for m in data.mean(axis=1):

        print(m)

~~~

~~~ {.python}

import sys

import numpy



def main():

    script = sys.argv[0]

    filename = sys.argv[1]

    data = numpy.loadtxt(filename, delimiter=',')

    for m in data.mean(axis=1):

        print(m)



main()

~~~

~~~ {.python}

import sys

import numpy



def main():

    script = sys.argv[0]

    for filename in sys.argv[1:]:

        data = numpy.loadtxt(filename, delimiter=',')

        for m in data.mean(axis=1):

            print(m)



main()

~~~

~~~ {.python}

import sys

import numpy



def main():

    script = sys.argv[0]

    action = sys.argv[1]

    filenames = sys.argv[2:]



    for f in filenames:

        data = numpy.loadtxt(f, delimiter=',')



        if action == '--min':

            values = data.min(axis=1)

        elif action == '--mean':

            values = data.mean(axis=1)

        elif action == '--max':

            values = data.max(axis=1)



        for m in values:

            print(m)



main()

~~~

~~~ {.python}

import sys

import numpy



def main():

    script = sys.argv[0]

    action = sys.argv[1]

    filenames = sys.argv[2:]

    assert action in ['--min', '--mean', '--max'], \

           'Action is not one of --min, --mean, or --max: ' + action

    for f in filenames:

        process(f, action)



def process(filename, action):

    data = numpy.loadtxt(filename, delimiter=',')



    if action == '--min':

        values = data.min(axis=1)

    elif action == '--mean':

        values = data.mean(axis=1)

    elif action == '--max':

        values = data.max(axis=1)



    for m in values:

        print(m)



main()

~~~

~~~ {.python}

import sys



count = 0

for line in sys.stdin:

    count += 1



print(count, 'lines in standard input')

~~~

~~~ {.python}

import sys

import numpy



def main():

    script = sys.argv[0]

    action = sys.argv[1]

    filenames = sys.argv[2:]

    assert action in ['--min', '--mean', '--max'], \

           'Action is not one of --min, --mean, or --max: ' + action

    if len(filenames) == 0:

        process(sys.stdin, action)

    else:

        for f in filenames:

            process(f, action)



def process(filename, action):

    data = numpy.loadtxt(filename, delimiter=',')



    if action == '--min':

        values = data.min(axis=1)

    elif action == '--mean':

        values = data.mean(axis=1)

    elif action == '--max':

        values = data.max(axis=1)



    for m in values:

        print(m)



main()

~~~

