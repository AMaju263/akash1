
def addStudentData():
    
    namelist = {}
    
    flag = True
    while flag == True:
    
        name =  input("Enter student's name: ")
        score = float(input("Enter student's score: "))

        namelist[name] = score

        check = input("do you want to want to add more students? ")

        if check.lower == "yes" or "y":
            continue
        else:
            flag  = False


    return namelist