#Define a dictionary for activities with the given time
#Calculate the hours of 'other' category 
#Print the dictionar
#Creat and display a pie chart about the activities 
#Print the time spend on requested activities



my_dict={"sleeping":8, "classes":6, "studying":3.5, "TV":2, "music":1}
otherhours = 24-sum(my_dict.values())
my_dict["other"]=otherhours


print(my_dict)

import matplotlib.pyplot as plt
plt.figure(figsize=(8, 8))
plt.pie(my_dict.values(), labels=my_dict.keys(), autopct='%1.1f%%')
plt.title('Daily Activities')
plt.show()
plt.clf
requested_activity = 'sleeping'  

# You can modify this variable to any activity in the dictionary
hours_spent = my_dict.get(requested_activity, 0)
print(f"On an average day, {hours_spent} hours are spent on {requested_activity}.")