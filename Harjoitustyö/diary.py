#programme starts
try:
    todo ="x"
    weekday = "y"
    i = 0
#todolist is empty, set a weekdays list
    todolist=[]
    weekdaylist=["monday","tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
#use loop funtion which stops when fields are empty
    while todo != "":
        todo = input("Please, write what you plan to do for this week: ")
        weekday = (input("Please, write a day of the week for plan above: ")).lower()   
#distribute todo things according weekdays and put things in the txt file
        if todo != "" and weekday in weekdaylist:
            todolist.append(todo) 
            i = i + 1  
            if weekday == weekdaylist[0]:
                filename_Monday = "monday.txt"
                file = open(filename_Monday, "w")
                thing = todo
                file.write(todo +"\n")
                file.close()
            elif weekday == weekdaylist[1]:
                filename_Tuesday = "tuesday.txt"
                file = open(filename_Tuesday, "w")
                thing = todo
                file.write(todo +"\n")
                file.close()
            elif weekday == weekdaylist[2]:
                filename_Wednesday = "wednesday.txt"
                file = open(filename_Wednesday, "w")
                thing = todo
                file.write(todo +"\n")
                file.close()
            elif weekday == weekdaylist[3]:
                filename_Thursday = "thursday.txt"
                file = open(filename_Thursday, "w")
                thing = todo
                file.write(todo +"\n")
                file.close()
            elif weekday == weekdaylist[4]:
                filename_Friday = "friday.txt"
                file = open(filename_Friday, "w")
                thing = todo
                file.write(todo +"\n")
                file.close()
            elif weekday == weekdaylist[5]:
                filename_Saturday = "saturday.txt"
                file = open(filename_Saturday, "w")
                thing = todo
                file.write(todo +"\n")
                file.close()
            elif weekday == weekdaylist[6]:
                filename_Sunday = "sunday.txt"
                file = open(filename_Sunday, "w")
                thing = todo
                file.write(todo +"\n")
                file.close()
        elif todo == "":
            print("The fields are empty")
#if weekday is not in the list above, print information about it and programme continue
        else:
            print("Where are no such a day in the week!")
# i counts objects in the todolist and join function take of []
    print("You have:", i, "thing(s) to do in this week:", ", ".join(todolist))        
#Here are exptions if smth goes wrong
except TypeError:
    print ("Where are no such a day in the week!")
except ConnectionError:
    print("Someting worng with connection. Please try again.")
except:
    print("Something else went wrong")