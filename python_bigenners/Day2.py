print("Welcome to the tip calculator")
total=float(input("What is the total bill? $"))
num_of_people=int(input("how many peoples? "))
tips=int(input("What precentage tip do you like to give? %"))
total_paid=float(total+(total*(tips/100)))
print(total_paid)
each=print(f"each one should pay= {total_paid/num_of_people}")