import time
def choice(Operator,num1,num2):
    if(Operator == "+"):
        answer = num1+num2
        return answer
    elif(Operator == "-"):
        answer = num1-num2
        return answer
    elif(Operator == "*"):
        answer = num1*num2
        return answer
    elif(Operator == "/"):
        answer = num1/num2
        return answer
    elif(Operator == "^"):
        answer = num1**num2
        return answer

print("""Welcome to the simple calulator!
         You can do calulations with only one digit in them!
         For example: 5+4.   This wouldn't work:15+10""")
time.sleep(2)
calculation=input("Enter the calulation!(Only single digits accepted) V1.00:")
Operator=calculation[1]
num1=int(calculation[0])
num2=int(calculation[2])


answer = choice(Operator,num1,num2)
print(answer)

