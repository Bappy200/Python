try:
    age=int(input("Enter your age : "))
    income=2000
    rick=income/age
    print(rick)

except ValueError:
    print("Invalid Age")

except ZeroDivisionError:
    print("Age not be 0 !")

