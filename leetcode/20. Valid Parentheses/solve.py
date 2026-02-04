class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()

        opens_brackets = {
                          '(' : 0,
                          '[' : 0, 
                          '{' : 0,
                         }

        closes_brackets = {
                          ')' : 0,
                          ']' : 0, 
                          '}' : 0,
                         }
        for i in s:
            if i in opens_brackets:
                opens_brackets[i] += 1
            elif i in closes_brackets:
                closes_brackets[i] += 1

        if opens_brackets["("] != closes_brackets[")"]:
            return False
        elif opens_brackets["["] != closes_brackets["]"]:
            return False
        elif opens_brackets["{"] != closes_brackets["}"]:
            return False

        for i in s:
            if i in opens_brackets:
                stack.append(i)
            elif i in closes_brackets and len(stack) > 0:
                if stack[-1] == "(" and i != ")":
                    return False
                elif stack[-1] == "[" and i != "]":
                    return False
                elif stack[-1] == "{" and i != "}":
                    return False
                else:
                    stack.pop()

        if len(stack) > 0:
            return False    
            
        return True
  
