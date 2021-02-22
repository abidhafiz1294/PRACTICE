import csv
file= open('example.csv')
file_reader=csv.reader(file)
"""list=list(file_reader)
print(list)"""
print(file_reader)
for row in file_reader:
    print('Row no = '+ str(file_reader.line_num)+''+ str(row))


