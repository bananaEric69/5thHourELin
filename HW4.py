#Name: Eric Lin
#Class: 5th
#assignment:HW4

print("Hello World")

iphoneDict = {
    "Company" : "Apple",
    "Model" : "Iphone 10",
    "Release date" : [2017, 2018, 2019]
}

print(iphoneDict["Release date"][0])
iphoneDict.update({"color": "silver"})
print(iphoneDict)

iphoneDict.clear()
print(iphoneDict)

classmate = {
        "classmate1": {
            "Name" : "Sam",
            "Grade" : 9,
           "Gamer" : True,
  },
        "classmate2": {
            "Name" : "Gage",
            "Grade" : 9,
           "Gamer" : True,
        },
           "classmate3": {
             "Name" : "Kevin",
               "Grade" : 11,
              "Gamer" : True,
     }
}
print(classmate["classmate1"]["Name"],classmate["classmate2"]["Name"],classmate["classmate3"]["Name"])









