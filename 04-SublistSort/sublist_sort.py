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


def sort_sublists(list, start, mid, end):
    '''Sorts the two adjacent sublists in place:<br />
    first sublist  = list[start .. mid]<br />
    second sublist = list[mid + 1 .. end]'''
    # Take each element of the second sublist and move it left
    # until it sits in the correct position among the elements before it
    for i in range(mid + 1, end + 1):
        j = i
        while j > start and list[j - 1] > list[j]:
            list[j - 1], list[j] = list[j], list[j-1]
            j -= 1


def sort_pass(array):
    '''Does one full pass across the array, handling two sublists at a time.'''
    start = 0
    done = False

    while not done:
        first_end = get_sublist_index(array, start)

        if first_end == len(array) - 1:
            done = True

        else:
            second_end = get_sublist_index(array, first_end + 1)

            sort_sublists(array, start, first_end, second_end)

            start = second_end + 1
        
            done = not (start < len(array))


def main(array: list[int]) -> list[int]:
    '''Main function loop. Takes in a list and returns that list sorted.'''
    # Repeat until one sorted run covers the whole array
    while get_sublist_index(array, 0) < len(array) - 1:
        sort_pass(array)

    return array


if __name__ == "__main__":
    data = [random.randint(0, 99) for _ in range(20)]
    print(f"List before sort: {data}")
    data = main(data)
    print(f"List after sort: {data}")
