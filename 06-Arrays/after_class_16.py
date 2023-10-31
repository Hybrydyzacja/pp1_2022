# An array contains natural numbers: 15, 8, 31, 47, 2, 19. 
# Create a program that displays the contents of the array in reverse order. 
# Use any loop statement. Sample result:
# existed array: 15 8 31 47 2 19 
# reverse array: 19 2 47 31 8 15


array = [15, 8, 31, 47, 2, 19]
print(array)


for numbers in range(len(array)):
    print(array[::-1])
    break

#lub tak, ale wtedy zamienimy listę na nową

# a = array.reverse()
# print(array)

array = [15, 8, 31, 47, 2 , 19]
print(f'existed array: {array}')

l = len(array)
for n in range(l // 2):
    array[n], array[l - n - 1] = array[l - n - 1], array[n]

array.reverse()
# tak jest zdecydowanie szybciej 
print(f'reversed array {array}')