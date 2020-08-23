class Solution:
    def countBits(self, num: int) -> List[int]:

        def recursion(num: int, power: int, currentSet: List[int], result: List[int]) -> List[int]:

            # array length reach to num + 1 represent can return now
            if len(result) == num + 1:
                return result

            element_to_push = 2**power

            for i in range(element_to_push):
                # when only 1 element
                if i < len(currentSet) and currentSet[i] == 0:
                    result.append(1)
                    continue

                if i < len(currentSet):
                    result.append(currentSet[i])
                else:
                    result.append(currentSet[i - len(currentSet)] + 1)

                # when reached the num
                if len(result) == num + 1:
                    return result

            # update current set
            currentSet = result[len(result) - element_to_push:len(result)]

            recursion(num, power + 1, currentSet, result)

            return result

        return recursion(num, 0, [0], [0])