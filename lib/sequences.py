#!/usr/bin/env python3

def print_fibonacci(length):
    '''Prints the Fibonacci sequence up to the specified length.'''
    if length <= 0:
        print('[]')
        return
    
    #case for length = 1
    if length == 1:
        print('[0]')
        return
    
    # Initialize the first 2 Fibonacci numbers
    fib_sequence = [0, 1]
    
    # Generate the Fibonacci sequence to the desired length
    while len(fib_sequence) < length:
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_fib)
    
    # Print the list 
    print(fib_sequence)