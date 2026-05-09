class Solution:

    def encode(self, strs: List[str]) -> str:
        output =""
        for s in strs:
            output += str(len(s)) + "#" + s
        print(output)
        return output

    def decode(self, s: str) -> List[str]:
        output = []
        next_string_length = 0
        current_index = 0

        while current_index < len(s):
                curr = current_index
                while s[curr] !=  "#":
                    curr +=1
                next_string_length = int(s[current_index:curr])
                current_index = curr+1
                output.append(s[current_index:current_index+next_string_length])
                current_index = current_index+next_string_length

        return output
            
            



