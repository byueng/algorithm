# -*- coding: utf-8 -*-
# @Time    : 2025-07-15 15:38
# @Author  : jwm
# @File    : 有效单词.py
# @description: For the High King

from typing import List

class Solution:
    def isValid(self, word: str) -> bool:
        word = word.lower()
        have_meta: bool = False
        have_sub: bool = False 
        meta_parameter: List[str] = ['a', 'e', 'i', 'o', 'u']
        if len(word) < 3:
            return False 
        for i in word:
            if not (i >= "a" and i <= "z" or i >= "0" and i <= "9"):
                return False
            else:
                # 是字母
                if i > "9":
                    if i in meta_parameter:
                        have_meta = True
                    else:
                        have_sub = True
                # 是数字
                else:
                    continue
        if not (have_meta and have_sub):
            return False
        return True


def main():
    word = '3pp'
    solution = Solution()
    result = solution.isValid(word)
    print(result)


if __name__ == "__main__":  
    main()