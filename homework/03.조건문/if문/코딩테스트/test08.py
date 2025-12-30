def solution(mystring,pat):
        result = 0
        for i in mystring:
            if pat in mystring:
                result = result + 1
        return result
         
mystring = 'banana'
pat = 'ana'
print(solution(mystring,pat))