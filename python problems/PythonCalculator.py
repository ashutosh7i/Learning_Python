#This is a calculator made in Python
number_1 = int(input("Enter the first Number- "));
number_2 = int(input("Enter the second Number- "));

Operation = input("Enter the Operation to perform(+,-,*,/)- ");
print("The operation is- ");
if Operation == '+':
    print(number_1+number_2);
elif Operation == '-':
    print(number_1-number_2);
elif Operation == '*':
    print(number_1*number_2);
elif Operation == '/':
    print(number_1/number_2);
else:
    print("INVALID OPERATION!");