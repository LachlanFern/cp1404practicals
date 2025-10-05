#1
name = input("Please enter your name: ")
write_file = open("name.txt", "w")
print(f"{name}",file=write_file)
write_file.close()

#2
read_file = open("name.txt", "r")
read_name = read_file.readline()
print(f"Hi {read_name}")
read_file.close()

#3
with open("numbers.txt", "r") as num_file:
 num1 = int(num_file.readline())
 num2 = int(num_file.readline())
answer = num1 + num2
print(answer)

#4
total = 0
with open("numbers.txt", "r") as number_file:
    for line in number_file:
        total += int(line)
print(total)
