with open('task8', 'r') as f:
    steps = [int(line.strip()) for line in f]

days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

result = []
i = 0
for days in days_in_month:
    month = steps[i:i+days]
    average = sum(month) / days
    result.append(average)
    i += days

with open('output.txt', 'w') as f:
    for avg in result:
        f.write(f"{avg}\n")
