# Reading 6.2 Customizing Iteration

# A generator is any function that uses the yield statement.
# yield produces a value, but suspends the function execution.
# The function resumes on next call to __next__().

def countdown(n):
    print('Counting down from', n)
    while n > 0:
        yield n
        n -= 1

x = countdown(10)
print(x)
next(x)