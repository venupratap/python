import json
import csv

# Opening JSON file
f = open('data.json')

# returns JSON object as
# a dictionary
data = json.load(f)
print(data)
s = []
reviews = data["data"]["repository"]["pullRequest"]["reviews"]["nodes"]
comments = data["data"]["repository"]["pullRequest"]["comments"]["nodes"]

for each in reviews:
    s.append(each['body'])

print(type(s))
print(s)
#filename = "reviews.csv"

with open('Example.csv', 'w') as csvfile:
    my_writer = csv.writer(csvfile)
    for ele in s:
        my_writer.writerow([ele+""])



















