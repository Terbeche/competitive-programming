class Solution:
    def interpret(self, command: str) -> str:
        n = len(command)
        answer = ""
        i = 0

        while i < n:
            if command[i] == "G":
                answer += "G"
                i += 1
            elif command[i] == "(":
                if command[i+1] == ")":
                    answer += "o"
                    i += 2
                else:
                    answer += "al"
                    i += 4

        return answer