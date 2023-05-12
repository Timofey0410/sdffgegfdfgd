print("Введите значение a: ")
a = int(input())
print("Введите значение b: ")
b = int(input())

print("Выберите действие: p , s , p1 , s1") 
действие = input()
if действие == "p":
    print((a + b) * 2)
elif действие == "s":
    print(a * b)
if действие == "p1":
    print(a * 4)
elif действие == "s1":
    print(a ** 2)