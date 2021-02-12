number_test={
    1:"One",
    2:"Two",
    3:"Three",
    4:"Four",
    5:"Five",
    6:"Six",
    7:"Seven",
    8:"Eight",
    9:"Nine",
    0:"Zro"
}
phone_number=input("Enter the phone number : ")
for number in phone_number:

    print(number_test[int(number)]+" ",end='')

