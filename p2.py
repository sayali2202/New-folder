#wap to accept days and check the working day or not
day=input("Enter the day:")
if day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
    print("Working day")
elif day in ["Saturday", "Sunday"]:
    print("Weekend")
else:
    print("Invalid day")