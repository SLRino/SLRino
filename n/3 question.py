'''Now the sub role can be added to any role. And also display the roles in role hierarchy order.The role hierarchy order of the above tree would be CEO, CCO ,CTO, Senior Product Engineering Manager, Senior Product Marketing Manager, Director of Technology.... and so on.'''






list1=[]      #STORE ALL ROLES
root_role=str(input("Enter root role name : "))
list1.append(root_role)
while True:
    def switch():
            print("Operations")
            print("1.Add Sub Role")
            print("2. Display Roles.")
            operation=int(input())
            if operation==1:
                print("operation to be performed : 1")
                sub_role=str(input("Enter sub role name : "))
                rep_role=str(input("Enter reporting to role name : "))
                if rep_role == root_role:     #CHECK SUB ROLES OF CEO
                    list1.append(sub_role)
                elif rep_role != root_role:   #CHECK SUB ROLES OF COO,CTO
                    for x in list1:
                        if x==rep_role:
                            list1.append(sub_role)
                    
            elif operation==2:
                if not len(list1):
                    print("empty")
                else:
                    
                    print(*list1)
                    
    switch()


























