string = input("Enter a string: ")
size   = int(input("Enter arrow's size (greater than 0): "))
space  = 0
store  = 1

if size <= 0:
    print("Size must be greater than 0.")
if size == 2:
    print(string)
    print(string)

if size % 2 == 0 and size != 2:
    for i in range(size):
        if size % 2 == 0 and space <= (size//2)-1:
            print(f"{' '*space}{string}")
            space += 1
    for i in range(size//2):
        print(f"{' '*(space-1)}{string}")
        space -= 1

if size % 2 != 0:
    for i in range(size):
        if space <= size//2:
            print(f"{' '*space}{string}")
            space += 1
    for i in range(size//2):
        print(f"{' '*(space-2)}{string}")
        space -= 1