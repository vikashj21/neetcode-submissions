class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for op in s:
            if op == "]" and bool(stack):
                if stack.pop() != "[":
                    return False
            elif op == "}" and bool(stack):
                if stack.pop() != "{":
                    return False   
            elif op == ")"and bool(stack):
                if stack.pop() != "(":
                    return False   
            else:
                stack.append(op)
        
        return not bool(stack)