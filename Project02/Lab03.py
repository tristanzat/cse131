# 1. Name:
#      Tristan Zatylny
# 2. Assignment Name:
#      Lab 03 : Calendar Program
# 3. Assignment Description:
#      This displays a calendar for a month given an input month and year.
# 4. What was the hardest part? Be as specific as possible.
#      The most difficult part was figuring out how to do the compute_offset function.
#      Having the pseudocode done for the function helped a lot, though.
# 5. How long did it take for you to complete the assignment?
#      1.5 hours


# Test cases:
# January 1753 - normal
# February 1753 - non-leap year
# January 1754 - normal
# February 1756 - leap year
# February 1800 - non-leap year
# February 2000 - leap year
# Month: "error", 0, 13, 11 - error handling to eventual success
# Year: "error", -1, 1752, 2019 - error handling to eventual success


def display_table(month: int, year: int):
    '''Display a calendar table for a given month and year'''
    assert(type(month) == type(year) == type(0))
    assert(1 <= month <= 12)
    assert(year > 1752)
    
    dow = compute_offset(month, year)
    # Logic below expects that 0 represents Sunday; compute_offset has 0 representing Monday.
    # Add 1 to passed-in parameter and handle input being 6 (Sunday)
    dow = 0 if dow + 1 > 6 else dow + 1

    num_days = number_days_in_month(month, year)

    assert(type(num_days) == type(dow) == type(0))
    assert(0 <= dow <= 6)
    assert(28 <= num_days <= 31)

    # Display a nice table header
    print("  Su  Mo  Tu  We  Th  Fr  Sa")

    # Indent for the first day of the week
    for indent in range(dow):
        print("    ", end='')

    # Display the days of the month
    for dom in range(1, num_days + 1):
        print(repr(dom).rjust(4), end='')
        dow += 1
        # Newline after Saturdays
        if dow % 7 == 0:
            print("") # newline

    # We must end with a newline
    if dow % 7 != 0:
        print("") # newline


def compute_offset(month: int, year: int) -> int:
    '''Get which day is the starting day of the week given a month and year. Returns 0 (Monday) - 6 (Sunday)'''
    assert(type(month) == type(year) == type(0))
    assert(1 <= month <= 12)
    assert(year > 1752)
    # Root day is January 1, 1753 (Monday), calculate based on that
    total_days = 0

    # Add days for all past years
    for y in range(1753, year):
        total_days = total_days + 366 if is_leap_year(y) else total_days + 365

    # Add days for months
    for m in range(1, month):
        total_days += number_days_in_month(m, year)

    # Return 0-6 (0 = Monday, 6 = Saturday)
    return total_days % 7


def number_days_in_month(month: int, year: int) -> int:
    '''Returns the number of days in a month'''
    assert(type(month) == type(year) == type(0))
    assert(1 <= month <= 12)
    assert(year > 1752)

    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # Handle leap year
    if month == 2 and is_leap_year(year):
        return 29
    return days[month - 1]


def is_leap_year(year: int) -> bool:
    '''Returns true if a given year is a leap year.'''
    assert(type(year) == type(0))
    assert(year > 1752)

    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def main():
    # Get user input for month
    valid_input = False
    while not valid_input:
        try:
            month = int(input("Enter the month number: "))
            assert(1 <= month <= 12)
            valid_input = True
        except:
            print("Invalid input. Must input a number 1-12.")

    # Get user input for year
    valid_input = False
    while not valid_input:
        try:
            year = int(input("Enter year: "))
            assert(year > 1752)
            valid_input = True
        except:
            print("Invalid input. Year must be 1753 or later.")

    display_table(month, year)


if __name__ == "__main__":
    main()