subjects =  ["English", "Math", "Sindhi"]
obtain = 0
total = 300
#print(subjects[0])
for i in range(len(subjects)):

    #print(subjects[i])
    subjects[i] = eval(input(f"Enter the Marks of {subjects[i]} : "))
    obtain = obtain + subjects[i]
print(f"total obtain marks are {obtain} and percetage is : ", obtain/total * 100)
    
