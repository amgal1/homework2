from task3 import sales, total

s = 0
b = ""
m = -1
for d in sales:
    x = total(sales[d])
    s += x
    if x > m:
        m = x
        b = d

print("Итого за неделю: выручка", s)
if b:
    print(f"День с максимальной выручкой: {b} ({m})")
print("Средняя выручка за день:", round(s / len(sales)) if sales else 0)
