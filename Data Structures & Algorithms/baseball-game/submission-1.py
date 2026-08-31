class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = []

        for operation in operations:
            match operation:
                case '+':
                    a = scores.pop()
                    b = scores.pop()
                    c = a + b
                    scores += [b, a, c]
                case 'C':
                    scores.pop()
                case 'D':
                    a = scores.pop()
                    scores += [a , a * 2]
                case _:
                    scores.append(int(operation))

        return sum(scores)
