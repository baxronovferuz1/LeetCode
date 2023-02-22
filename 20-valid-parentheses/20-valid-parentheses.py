class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        types = True
        for i in s:
            if i in '([{':
                stack.append(i)
            elif i in ')]}':
                try:
                    popped_element = stack.pop()
                except:
                    types=False
                    break
                if popped_element=='(' and i==')':
                    pass
                elif popped_element=='{' and i=='}':
                    pass
                elif popped_element=='[' and i==']':
                    pass
                else:
                    types=False
                    break
        if len(stack)==0:
            return (types)
        else:
            return (False)
                
        
        return True 