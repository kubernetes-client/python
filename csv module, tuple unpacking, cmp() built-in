import csv

# need to define cmp function in Python 3
def cmp(a, b):
    return (a > b) - (a < b)

# write stocks data as comma-separated values
with open('stocks.csv', 'w', newline='') as stocksFileW:
    writer = csv.writer(stocksFileW)
    writer.writerows([
        ['GOOG', 'Google, Inc.', 505.24, 0.47, 0.09],
        ['YHOO', 'Yahoo! Inc.', 27.38, 0.33, 1.22],
        ['CNET', 'CNET Networks, Inc.', 8.62, -0.13, -1.4901]
    ])

# read stocks data, print status messages
with open('stocks.csv', 'r') as stocksFile:
    stocks = csv.reader(stocksFile)

    status_labels = {-1: 'down', 0: 'unchanged', 1: 'up'}
    for ticker, name, price, change, pct in stocks:
        status = status_labels[cmp(float(change), 0.0)]
        print ('%s is %s (%.2f)' % (name, status, float(pct)))
