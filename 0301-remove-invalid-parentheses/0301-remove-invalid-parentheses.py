class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        def isValid(string):
            count = 0

            for ch in string:
                if ch == '(':
                    count += 1
                elif ch == ')':
                    count -= 1

                if count < 0:
                    return False

            return count == 0

        level = {s}

        while level:
            result = []

            for string in level:
                if isValid(string):
                    result.append(string)

            if result:
                return result

            next_level = set()

            for string in level:
                for i in range(len(string)):
                    if string[i] not in '()':
                        continue

                    new_string = string[:i] + string[i+1:]
                    next_level.add(new_string)

            level = next_level

        return [""]
