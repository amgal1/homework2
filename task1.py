t = "Дом, в котором мы живём, — это не просто дом. В доме живут люди, и люди эти делают дом домом. Без людей дом — просто стены, а стены без дома и без людей — уже не дом, а коробка."

s = ""
for c in t.lower():
    if c.isalpha():
        s += c
    else:
        s += " "
w = s.split()

d = {}
for x in w:
    d[x] = d.get(x, 0) + 1

print(f"Всего слов: {len(w)}, из них уникальных: {len(d)}")

a = sorted(d.items(), key=lambda x: (-x[1], x[0]))[:5]
print("Топ-5 слов:", ", ".join(f"{k} ({v})" for k, v in a))

m = 0
for x in w:
    if len(x) > m:
        m = len(x)
r = []
for x in w:
    if len(x) == m and x not in r:
        r.append(x)
print("Самое длинное слово:", ", ".join(r))

n = {}
for x in w:
    n[len(x)] = n.get(len(x), 0) + 1
print("Слова по длинам:", dict(sorted(n.items())))
