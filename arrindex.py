def arrGet(arr, index):
    length = len(arr)
    ind = int(index)

    while True:
        index = input("Please Enter an integer that is within the array: ")
        try:
            index = int(index)
            if 0 <= index < length:
                break
            else:
                print("Index is out of range. Try again")
        except ValueError:
            print("Invalid input. Please enter an integer")

given = [1, 2, 3, 4]
x = arrGet(given, 5)
print(x)
print(len(given))
