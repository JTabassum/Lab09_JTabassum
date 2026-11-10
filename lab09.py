# Problem-solving practice (LeetCode / ICPC style).
#
# For EACH problem, work out your problem-solving OUTLINE first - restate the problem,
# try a small example by hand, and sketch your approach - BEFORE you write or generate
# any code. You may use an AI assistant to help implement your plan (see the README),
# but do the thinking first.
#
# Do not rename the functions - the tests use these names.


def two_sum(nums, target):
    # Outline (write your plan here first):
    # have a loop to make i the first number
    # have a loop that makes j the second numbers
    # i + j comapre to target
    # TODO: return the indices [i, j] (i < j) of the two numbers in `nums` that add up
    #   to `target`. Assume there is exactly one answer.
    for i in range(len(nums)):
        for j in range (i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


def max_profit(prices):
    # Outline:
    #   has a loop that sests i to first element
    # have a loop that sets j to the second elements
    # comapre i and j to max
    # TODO: `prices[i]` is a stock price on day i. Return the most profit obtainable by
    #   buying on one day and selling on a LATER day. If no profit is possible, return 0.
    max:int = 0
    for i in range (len(prices)):
        for j in range (i + 1, len(prices)):
            profit:int = prices[j] - prices[i]
            if profit > max:
                max = profit
                print(f'the max profit is {profit}')
    return max

def max_subarray(nums):
    # Outline:
    #   have a loop so i can be every elements
    # have a loop so j can be every element
    # set max to teh very first element
    # compare sum of i and j to max
    # TODO: return the largest sum of any contiguous (in-a-row) block of numbers in
    #   `nums`. The list has at least one number.
    max:int = nums[0]
    for i in range (len(nums)):
        sum:int = 0
        for j in range (i, len(nums)):
            sum+=nums[j]
            if sum > max:
                max = sum
                
    return max


def is_balanced(s):   # Part 4 - stretch (optional)
    # Outline:
    #   ...
    # TODO: return True if every bracket in `s` is closed correctly and in the right
    #   order. The brackets are ( ) [ ] { }. (Hint: a list used as a stack works well.)
    pass


def main():
    # Optional scratch space - try your functions here, then run: python lab09.py
    #print(two_sum([2, 7, 11, 15], 9))   # [0, 1]
    pass


if __name__ == "__main__":
    main()
