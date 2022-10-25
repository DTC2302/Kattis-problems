#take the first line of input and split it to the two separte variables
cap_and_schools = input().split()
capacity = int(cap_and_schools[0])
num_schools = int(cap_and_schools[1])

#initate the teams from each school and how many teams will go from each
num_teams = list()
goes_there = list()

#assign values to the lists
for i in range(num_schools):
    num_teams.append(int(input()))
    goes_there.append(0)
    

remaining_capacity =capacity
print(num_teams)
school=1

#loop for total number of teams
while remaining_capacity>0:
    while 1:
        #make sure the school isnt out of teams then increase the
        #number of teams they have going and decrease the teams left
        if(num_teams[school -1])>0:
            goes_there[school -1]+=1
            num_teams[school -1]-=1
            break
        #skip the empty schools or go back to the first
        else:
            if school == num_schools:
                school = 1
            else:
                school +=1
    #go to the next school
    if school == num_schools:
        school = 1
    else:
        school +=1
    remaining_capacity-=1
#print the number of teams going per school
for i in range(num_schools):
    print(goes_there[i])