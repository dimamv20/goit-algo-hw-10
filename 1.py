from pulp import *

limonad = LpVariable("Лимонад", lowBound=0, cat='Integer')
fruktoviy_sik = LpVariable("Фруктовий сік", lowBound=0, cat='Integer')

model = LpProblem("Максимізація виробництва", LpMaximize)

model += limonad + fruktoviy_sik, "Загальна кількість продуктів"

model += 2 * limonad + fruktoviy_sik <= 100, "Обмеження на воду"
model += limonad + fruktoviy_sik <= 50, "Обмеження на цукор"
model += limonad <= 30, "Обмеження на лимонний сік"
model += 2 * fruktoviy_sik <= 40, "Обмеження на фруктове пюре"

model.solve()

print("Кількість продукту 'Лимонад':", value(limonad))
print("Кількість продукту 'Фруктовий сік':", value(fruktoviy_sik))
