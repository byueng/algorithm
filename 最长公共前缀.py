# -*- coding: utf-8 -*-
# @Time    : 2025-07-08 20:26
# @Author  : jwm
# @File    : longestCommonPrefix.py
# @description: For the High King

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        commonprefix: str = ""
        current_char: str = ""
        strs_length: int = len(strs)
        epoch_num: int = 0
        flag: bool = True
        # singal char 
        if strs_length == 1 :
            commonprefix = strs[0]
            flag = False
        while flag: 
            for i in range(strs_length - 1):
                try:
                    left_char = strs[i][epoch_num] if strs[i] != "" else ""
                    right_char = strs[i+1][epoch_num] if strs[i+1] != "" else ""
                    current_char = left_char
                except IndexError:
                    return commonprefix
                # null char 
                if left_char == "" or right_char == "":
                    return ""
                if left_char != right_char:
                    flag = False
                    break
            if flag: 
                commonprefix += current_char
                epoch_num += 1    
        return commonprefix      

def main():
    strs = ["dog","racecar","car"]
    solution = Solution()
    result = solution.longestCommonPrefix(strs)
    print(result)

if __name__ == "__main__":
    main()