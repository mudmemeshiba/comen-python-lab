t  = 1
dp = 0
dc = 100
while dp < dc:
    dp += int(input("Input distance: "))
    print(f"Police distance: {dp}")
    dc = dc + 2**t
    print(f"Criminal distance: {dc}")
    t += 1
print("Caught him!")

# s = 0
# d = int(input("Input distance: "))
# print(f"Police distance: {d}")
# print("Criminal distance: 102") 
# while True:
    
#     distance = int(input("Input distance: "))
#     print(f"Police distance: {}")
#     print(f"Criminal distance: {}")                 

# #    v = s/t
# # 2**n = s/t
