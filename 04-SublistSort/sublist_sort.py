# 1. Name:
#      Tristan Zatylny
# 2. Assignment Name:
#      Lab 09 : Sub-List Sort Program
# 3. Assignment Description:
#      This program takes in a list of unsorted integers and sorts them
#      by sorting two sublists at a time.
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part of this assignment was writing the json file
#      for the test driver. It was easy other than that because of the
#      pseudocode.
# 5. How long did it take for you to complete the assignment?
#      1 hour

import random

def get_sublist_index(array, start):
    '''Returns the index where the sorted run beginning at `start` ends.
    Returns `start` itself if there is no sorted run.'''
    end = start
    while end + 1 < len(array) and array[end] <= array[end + 1]:
        end += 1
    return end


def sort_sublists(source, destination, start, mid, end):
    '''Sorts the two adjacent sublists using a destination array:<br />
    first sublist  = list[start .. mid]<br />
    second sublist = list[mid + 1 .. end]'''
    sub_one = start
    sub_two = mid + 1
    for i in range(start, end + 1):
        if sub_one > mid:
            destination[i] = source[sub_two]
            sub_two += 1
        elif sub_two > end or source[sub_one] <= source[sub_two]:
            destination[i] = source[sub_one]
            sub_one += 1
        else:
            destination[i] = source[sub_two]
            sub_two += 1
    return destination


def sort_pass(source, destination):
    '''Does one full pass across the list, handling two sublists at a time.'''
    start = 0
    done = False

    while not done:
        first_end = get_sublist_index(source, start)

        if first_end == len(source) - 1:
            # Copy any leftover element if necessary
            destination[start:] = source[start:]
            done = True

        else:
            second_end = get_sublist_index(source, first_end + 1)

            destination = sort_sublists(source, destination, start, first_end, second_end)

            start = second_end + 1
        
            done = not (start < len(source))


def main(source: list[int]) -> list[int]:
    '''Main function loop. Takes in a list and returns that list sorted.'''
    destination = [0] * len(source)
    # Repeat until one sorted run covers the whole list
    while get_sublist_index(source, 0) < len(source) - 1:
        sort_pass(source, destination)
        # Swap lists because apparently setting one equal to the other
        # makes them reference the same list in memory.
        source, destination = destination, source

    return source


if __name__ == "__main__":
    data = [random.randint(0, 99) for _ in range(20)]
    print(f"List before sort: {data}")
    data = main(data)
    print(f"List after sort: {data}")
