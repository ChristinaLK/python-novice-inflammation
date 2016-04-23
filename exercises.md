## Exercises

### Make your own plot

Create a plot showing the standard deviation (`numpy.std`) of 
the inflammation data for each day across all patients.

### Final analysis

Pull all of our analysis so far into a single Juypter notebook cell.  Things 
that need to be included are: 
* The libraries we're using
* Loading the data
* Save the min, max, and mean of the data as variables
* This code generates the outline of a figure: 
~~~
fig = plt.figure(figsize=(10.0,3.0))
axes1 = fig.add_subplot(1,3,1)
axes2 = fig.add_subplot(1,3,2)
axes3 = fig.add_subplot(1,3,3)
~~~
* This code creates the mean graph: 
~~~
axes1.set_ylabel('average')
axes1.plot(avg_inflammation)
~~~
* Duplicate the above code for the max and min graphs.  
* Finally, what command "shows" the plot?  


### Slicing strings

A section of an array is called a [slice](reference.html#slice).
We can take slices of character strings as well:

~~~ {.python}
element = 'oxygen'
print('first three characters:', element[0:3])
print('last three characters:', element[3:6])
~~~

~~~ {.output}
first three characters: oxy
last three characters: gen
~~~

What is the value of `element[:4]`?
What about `element[4:]`?
Or `element[:]`?

What is `element[-1]`?
What is `element[-2]`?
Given those answers,
explain what `element[1:-1]` does.

### Turn a string into a list

Use a for-loop to convert the string "hello" into a list of letters:

~~~ {.python}
["h", "e", "l", "l", "o"]
~~~
Hint: You can create an empty list like this:

~~~ {.python}
my_list = []
~~~

### Combining strings

"Adding" two strings produces their concatenation:
`'a' + 'b'` is `'ab'`.
Write a function called `fence` that takes two parameters called `original` and `wrapper`
and returns a new string that has the wrapper character at the beginning and end of the original.
A call to your function should look like this:

~~~ {.python}
print(fence('name', '*'))
~~~
~~~ {.output}
*name*
~~~

### Selecting characters from strings

If the variable `s` refers to a string,
then `s[0]` is the string's first character
and `s[-1]` is its last.
Write a function called `outer`
that returns a string made up of just the first and last characters of its input.
A call to your function should look like this:

~~~ {.python}
print(outer('helium'))
~~~
~~~ {.output}
hm
~~~

### Name initials

Write a function called `initials`, that takes in a single string with 
someone's name as input, and returns their initials as output.  For example: 

~~~ {.python}
print(initials("Aldo Leopold"))
~~~
~~~ {.output}
AL
~~~

There are different ways to do this, but one way involves using a string method
called `split()`.  What happens if you apply this method to the input string?  

### Close enough

Write some conditions that print `True` if the variable `a` is within 10% of the variable `b`
and `False` otherwise.
Compare your implementation with your partner's:
do you get the same answer for all possible pairs of numbers?

### Scripting

Implement another statistical measure (standard deviation, maximum or minimum)
in our script.  