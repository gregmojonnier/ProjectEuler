# Project Euler - Problem 2
# Each new term in the Fibonacci sequence is generated by adding the previous two terms.
# By starting with 1 and 2, the first 10 terms will be:
#       1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed four million,
# find the sum of the even-valued terms.

def sumEvenFibonacciTerms(limit):
    sum, nextTerm = 0, 0
    previousTwoTerms = [1, 2]

    # from the starting two terms(1,2)
    # add even terms to the sum and find initial nextTerm
    for term in previousTwoTerms:
        if isEven(term):
            sum = sum + term
        nextTerm = nextTerm + term

    while nextTerm < limit:
        if isEven(nextTerm):
            sum = sum + nextTerm
        previousTwoTerms.pop(0)
        previousTwoTerms.append(nextTerm)
        nextTerm = sumTwoTermList(previousTwoTerms)

    print "The sum of all even Fibonacci terms below {} is: {}".format(limit, sum)

def isEven(term):
    return (term % 2) == 0

def sumTwoTermList(twoTermList):
    sum = 0
    if len(twoTermList) != 2:
        return sum

    for term in twoTermList:
        sum = sum + term

    return sum

if __name__ == "__main__":
    sumEvenFibonacciTerms(10)
    sumEvenFibonacciTerms(4000000)
