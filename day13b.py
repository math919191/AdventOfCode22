
# mostly copied code from my first try "day13.py"

def readInput():
    f = open("input.txt", "r")

    pairs = []

    for line in f:
        if (line != '\n'):
            pairs.append(line.strip())

    return pairs


def convertToListIfNecessary(el1, el2):
    if type(el1) is int:
        el1 = [el1]
    if type(el2) is int:
        el2 = [el2]
    return el1, el2


def comp(el1, el2):

    # check if there is a valid comparison
    if type(el1) is int and type(el2) is int:
        if (el1 < el2):
            return True
        elif el1 > el2:
            return False
        else:
            return "same"

    el1, el2 = convertToListIfNecessary(el1, el2)

    if len(el1) == 0 and len(el2) == 0:
        return "same"

    if len(el1) == 0:  # left side ran out
        return True
    if len(el2) == 0:  # right side ran out
        return False

    for i in range(len(el1)):
        if len(el1) > 0 and len(el2) == 0:
            return False
        pop1 = el1.pop(0)
        pop2 = el2.pop(0)
        compResult = comp(pop1, pop2)
        if (compResult == "same"):
            pass
        else:
            return compResult
    if len(el1) == 0 and len(el2) > 0:
        return True

    return "same"


def bubbleSort(arr):  # straight from geeks for geeks
    n = len(arr)
    # optimize code, so if the array is already sorted, it doesn't need
    # to go through the entire process
    swapped = False
    # Traverse through all array elements
    for i in range(n-1):
        # range(n) also work but outer loop will
        # repeat one time more than needed.
        # Last i elements are already in place
        for j in range(0, n-i-1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            e1 = eval(arr[j])
            e2 = eval(arr[j + 1])
            # if arr[j] > arr[j + 1]:
            if comp(e1, e2) == False:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

        if not swapped:
            # if we haven't needed to make a single swap, we
            # can just exit the main loop.
            return


pairs = readInput()
pairs.append("[[6]]")
pairs.append("[[2]]")

bubbleSort(pairs)

a = 1
for i, pair in enumerate(pairs):
    if pair == "[[6]]" or pair == "[[2]]":
        a *= (i+1)
print(a)
