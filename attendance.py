<<<<<<< HEAD
import csv
import os
name_list = ["Anand", "Karthik", "Suresh", "Dilip", "Paul"]
nameq = input("What's your name?")
name = nameq[0].upper() + nameq[1:].lower()
file_exists=os.path.isfile("attendance1.csv")
def attendance_check(val):
    with open("attendance1.csv", "a",newline='') as csvfile:
        fn = ["Name", "Joined?"]
        writer = csv.DictWriter(csvfile, fieldnames=fn)
        if not file_exists:
            writer.writeheader()
        writer.writerow({'Name': name, 'Joined?': val})

if name in name_list:
    print("Hey there {0}!".format(name))
    attendance_check("Yes")
else:
    q = input("Are you new here? ")
    if q.lower() == 'yes':
        print("Welcome {}!".format(name))
        attendance_check("Newbie")
