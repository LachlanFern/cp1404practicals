
for i in range(1, 21, 2):
    print(i, end=' ')
print()

#loop a
for i in range(0, 101, 10):
    print(i, end=' ')
print()

#loop b
for i in range(20, 0 , -1):
    print(i, end=' ')
print()

#loop c
number_of_stars = int(input("Number of stars: "))
print("*" * number_of_stars)

#loop d
number_of_stars = int(input("Number of stars: ")) #can I get rid of this or do I need it because it is it's own loop 
for i in range(0, number_of_stars + 1, 1):
    print("*" * i,)
print()