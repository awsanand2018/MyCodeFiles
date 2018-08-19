import csv
html_output=''
name_list=[]
with open("sample.csv") as csv1:
    csv_reader=csv.DictReader(csv1)
    next(csv_reader)
    
    for l in csv_reader:
        if l['fname']=="No rewards":
            break
        name_list.append("{} {}".format(l['fname'],l['lname']))
    
    html_output+='\nThere are currently {} people who contributed through patrons'.format(len(name_list))
    html_output+="\n<ul>"
    for n in name_list:
        html_output+="\n\t<li>{}</li>".format(n)
    html_output+="\n</ul>"
    print(html_output)
        
