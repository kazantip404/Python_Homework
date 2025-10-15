lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]
print("\n <30 и делится на 3")
result = [number for number in lst if number < 30 and number % 3 == 0]
print(result)
