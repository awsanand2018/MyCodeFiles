num_list=[34,3,53,0,10,1,-34,100,23]

num_list1=[34,3,53,0,10,1,-34,100,23]

asc_sorted_list=[]

dsc_sorted_list=[]

def asc_function(list_input):

    c=0

    while list_input:

        min_value=min(list_input)        

        x=list_input.pop(list_input.index(min_value))

        asc_sorted_list.append(x)        

        c+=1

    print(asc_sorted_list)

def dsc_function(list_input):

    d=0

    while list_input:        

        max_value=max(list_input)        

        y=list_input.pop(list_input.index(max_value))        

        dsc_sorted_list.append(y)

        d+=1

    print(dsc_sorted_list)

asc_function(num_list)

dsc_function(num_list1)

