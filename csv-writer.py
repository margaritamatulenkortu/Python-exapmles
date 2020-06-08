import csv
from datetime import datetime

path = "/Users/margarita/Documents/Python-exapmles/data.csv"
file = open(path, newline='')
reader = csv.reader(file)
header = next(reader)  # fiest line is header so start with 2.line
# data = [row for row in reader] # read all data
# print(header)
# print(data[0])
# To make data to right type for priviously it was just a string
data = []
for row in reader:
    date = datetime.strptime(row[0], '%m/%d/%Y')
    open_price = float(row[1])  # open is built in function
    high = float(row[2])
    low = float(row[3])
    close = float(row[4])
    volume = int(row[5])
    adj_close = float(row[6])
    data.append([date, open_price, high, low, close, volume, adj_close])


returns_path = "/Users/margarita/Documents/Python-exapmles/returns.csv"
file = open(returns_path, 'w')
writer = csv.writer(file)
writer.writerow(['Date',"   ",'Return'])
for i in range(len(data) - 1):
    todays_row = data[i]
    todays_date = todays_row[0]
    todays_price = todays_row[-1]
    yesturdays_row = data[i+1]
    yesturdays_price = yesturdays_row[-1]

    daily_return = (todays_price - yesturdays_price) / yesturdays_price
    # writer.writerow([todays_date, daily_return])
    formatted_date = todays_date.strftime('%m/%d/%Y')
    writer.writerow([formatted_date, " ---- ", daily_return])