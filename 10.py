def day_of_year(date):
    d, m = map(int, date.split('.'))
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return sum(days_in_month[:m - 1]) + d

with open('input_10.txt', 'r') as f:
    lines = f.read().splitlines()

current_date = lines[0]
n = int(lines[1])
cells = lines[2:]

current_day = day_of_year(current_date)

result = []

for line in cells:
    number, date = line.split()
    stored_day = day_of_year(date)
    if (current_day - stored_day) > 3:
        result.append(number)

with open('output_10.txt', 'w') as f:
    for number in result:
        f.write(number + '\n')
