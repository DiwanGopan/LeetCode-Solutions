class Solution:
    def secondHighest(self, s: str) -> int:
        highest = -1
        second_highest = -1

        for i in s:
            if not i.isdigit():
                continue

            num = int(i)

            if num > highest:
                second_highest = highest
                highest = num
            elif highest > num > second_highest:
                second_highest = num

        if second_highest == -1:
            return -1
        else:
            return second_highest