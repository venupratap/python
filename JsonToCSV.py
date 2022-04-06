import json
import csv
# Opening JSON file
f = open('comments.json')

# returns JSON object as
# a dictionary
data = json.load(f)
print(data)
res = [ sub['body'] for sub in data ]
print(str(res))
with open('Example.csv', 'w', newline = '') as csvfile:
    my_writer = csv.writer(csvfile, delimiter = ' ')
    my_writer.writerow(res)



# Closing file
f.close()
