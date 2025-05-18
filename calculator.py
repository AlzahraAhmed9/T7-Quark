number_1= input("Enter the 1st  number ^-^ : ")
number_2= input("Enter the 1st  number ^-^ : ")
operation=input("Enetr the operation *-* : ")
result = 0 


# The operations :
if operation=="+":
    result= int(number_1) + int(number_2) 

elif operation=="- ":
    result= int(number_1) - int(number_2)

elif operation=="/":
    result= int(number_1) / int(number_2)



# output
print("Result is:", result )