# i = 0 

# while i <10:
#     if i == 5:
        
#         continue
#     print(i)
#     i += 1


# a=[1, 2, 3, 4, 5]
# val=4   

# for i in a:
#     if i == val:
#         print(f"found the value {i}")
#         break
#  else:
#         print("not found the value ")

# a = [1, 3, 5, 7, 9, 11]
# val = 7

# for i in a:
#     if i == val:
#         print(f"Found at {i}!")
#         break
# else:
#     print(f"not found")


# cnt=5

# while True:
#     print(cnt)
#     cnt -= 1
#     if cnt ==0 :
#         print("countdown ended")
#         break


# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# val = 5
# found = False

# for r in matrix:
#     for n in r:
#         if n == val:
#             print(f"{val} found!")
#             found = True
#             break  # Exit the inner loop
#     if found:
#         break  # Exit the outer loop


# list = ["quauntum", "bots", "python", "java", "c++"]

# for i in range(len(list)):
#     print(i,list[i])
# else:
#     print("Loop completed without break")


#     a=(1, 2, 3, 4, 5)
#     b=(1, 2, 3, 4, 5)

#     print(a is b)

for num in range(10, 14):
   for i in range(2, num):
         if num%i == 1:
              print(num)
              break