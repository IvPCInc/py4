squares = [x**2 for x in range(1, 11)]
print("1.", squares)

week_days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
days_dict = {day: idx+1 for idx, day in enumerate(week_days)}
print("2.", days_dict)

tags = ["Django", "FastAPI", "Numpy", "PYTHON", "Pandas", "FASTAPI", "Python", "random"]
lower_tags_set = {tag.lower() for tag in tags}
print("3.", lower_tags_set)

nums = [1, 3, 4, 87, 98, 15, 7, 4]
even_nums = [n for n in nums if n % 2 == 0]
print("4.", even_nums)

from math import factorial
factorials_dict = {n: factorial(n) for n in range(1, 6)}
print("5.", factorials_dict)
