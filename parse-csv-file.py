import csv
import os
with open("sample.csv") as rf:
    csv_reader=csv.DictReader(rf)
    with open("sample1.csv","w") as wf:
        csv_headers=['fname','lname','email']
        if os.path.isfile('sample1.csv'):
            q=input("File already exists. Do you want to overwrite?")
        if q.lower()=='yes':
            csv_writer=csv.DictWriter(wf,fieldnames=csv_headers,delimiter=',')
            csv_writer.writeheader()
            for l in csv_reader:
                
                csv_writer.writerow(l)
        else:
            print("Please try with a different file name")