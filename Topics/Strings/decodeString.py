"""
394. Decode String
https://leetcode.com/problems/decode-string/description/

Input: s = "3[a]2[bc]"
Output: "aaabcbc"



"""


def decodeString(s: str) -> str:
    """

    Time Complexity O(N) | N -> Length od input string
    Space Complexity O(N) | Worst case scenarios where nested brackets require stack storage

    """
    current_number = 0
    current_stack = []
    current_string = ""

    print("input :", s)
    for char in s:
        if char.isdigit():
            current_number *= 10
            current_number += int(char)

        elif char == "[":
            current_stack.append((current_string, current_number))
            current_number = 0
            current_string = ""

        elif char == "]":
            last_string, last_num = current_stack.pop()
            current_string = last_string + current_string * last_num

        else:
            current_string += char

        print(
            "char:",
            char,
            "current_string:",
            current_string,
            "current_number:",
            current_number,
            "current_stack:",
            current_stack,
        )
    return current_string


res = decodeString("3[a]2[bc]")
print(res)
