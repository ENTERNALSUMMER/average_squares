"""Computation of weighted average of squares."""
import argparse
# import readline
import numpy as np
import csv
def average_of_squares(list_of_numbers, list_of_weights=None):
    """ Return the weighted average of a list of values.
    
    By default, all values are equally weighted, but this can be changed
    by the list_of_weights argument.
    
    Example:
    --------
    >>> average_of_squares([1, 2, 4])
    21.0
    >>> average_of_squares([2, 4], [1, 0.5])
    12.0
    >>> average_of_squares([1, 2, 4], [1, 0.5])
    Traceback (most recent call last):
    AssertionError: weights and numbers must have same length

    """
    if list_of_weights is not None:
        assert len(list_of_weights) == len(list_of_numbers), \
            "weights and numbers must have same length"
        effective_weights = list_of_weights
    else:
        effective_weights = [1] * len(list_of_numbers)
    squares = [
        float(weight * number * number)
        for number, weight
        in zip(list_of_numbers, effective_weights)
    ]
    return sum(squares)


def convert_numbers(list_of_strings):
    """Convert a list of strings into numbers, ignoring whitespace.
    
    Example:
    --------
    >>> convert_numbers(["4", " 8 ", "15 16", " 23    42 "])
    [4, 8, 15, 16, 23, 42]

    """
    all_numbers = []
    if list_of_strings is None:
        all_numbers = None
    else:
        for s in list_of_strings.split(','):
            for token in s.split('"'):
                for t in token.split():
                    try:
                        all_numbers.append(float(t))
                    except ValueError:
                        pass
            # all_numbers.extend([token.strip() for token in s.split()])
        # Take each string in the list, split it into substrings separated by
        # whitespace, and collect them into a single list...
    return all_numbers

def parse_args():
    parse = argparse.ArgumentParser(description='calculate square')
    parse.add_argument('numbers',type=open, nargs='*',help='a list of number strings')
    parse.add_argument('-w','--weights',type=open, nargs='?',default=None,help='a list of weight strings')
    args = parse.parse_args() 
    with open('numbers.txt','r') as myfile:
        args.numbers = myfile.read()
    with open('weights.txt','r') as myfile:
        args.weights = myfile.read()
    return args


if __name__ == "__main__":

    args = parse_args()
    # weight_strings = ["1"]
    # input as "1 2 4" "1 1 1" 
    numbers = convert_numbers(args.numbers)
    # print(open(args.numbers).read())
    weights = convert_numbers(args.weights)
    # print(weights)
    result = average_of_squares(numbers, weights)
    print(result)