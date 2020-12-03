# ----------- Day 1 Task ----------------

# Before you leave, the Elves in accounting just need you to fix your expense report (your puzzle input); apparently, something isn't quite adding up.
#
# Specifically, they need you to find the two entries that sum to 2020 and then multiply those two numbers together.
#
# For example, suppose your expense report contained the following:
#
# 1721
# 979
# 366
# 299
# 675
# 1456
#
# In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying them together produces 1721 * 299 = 514579, so the correct answer is 514579.
#
# Of course, your expense report is much larger. Find the two entries that sum to 2020; what do you get if you multiply them together?
#
#
# --- Part Two ---
# The Elves in accounting are thankful for your help; one of them even offers you a starfish coin they had left over from a past vacation. They offer you a second one if you can find three numbers in your expense report that meet the same criteria.
#
# Using the above example again, the three entries that sum to 2020 are 979, 366, and 675. Multiplying them together produces the answer, 241861950.
#
# In your expense report, what is the product of the three entries that sum to 2020?


# ----------- Solution ----------------


def elvish_accounting(num_ints: list, num_to_sum_to: int):

    for num in num_ints:
        if num_to_sum_to-num in num_ints:
             return num * (num_to_sum_to - num)
        else:
            continue
    return 0


def elvish_accounting_2(num_ints: list, num_to_sum_to: int):

    for num in num_ints:
        new_num_ints = []
        new_num_ints.extend(num_ints)

        new_num_to_sum_to = num_to_sum_to-num
        new_num_ints.remove(num)
        product = num * elvish_accounting(new_num_ints, new_num_to_sum_to)
        if product == 0:
            continue
        else:
            return product

if __name__ == '__main__':

    file = open("Day1.txt", "r")
    num_ints = [int(num_str.strip()) for num_str in file]

    elvish_accounting(num_ints, 2020) # 960075
    elvish_accounting_2(num_ints, 2020) # 212900130
