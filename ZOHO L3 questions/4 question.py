'''Support delete role operation. If a role is deleted then all its properties (child roles) will be transferred to the role entered by the user as input.'''





list1=[]     #STORE ALL NODES
root_role=str(input("Enter root role name : "))
list1.append(root_role)
while True:
    def switch():
            print("Operations")
            print("1.Add Sub Role")
            print("2. Display Roles.")
            print("3. Delete Role.")
            operation=int(input())
            if operation==1:
                print("operation to be performed : 1")
                sub_role=str(input("Enter sub role name : "))
                rep_role=str(input("Enter reporting to role name : "))
                if rep_role == root_role:     #CHECK SUB ROLES OF CEO
                    list1.append(sub_role)
                elif rep_role != root_role:    #CHECK SUB ROLES OF COO,CTO
                    for x in list1:
                        if x==rep_role:
                            list1.append(sub_role)
            elif operation==2:
                if not len(list1):         #CHECK ROLES LIST 
                    print("empty")
                else:
                    print(*list1)
            elif operation==3:            
                print("Operation to be performed : 3")
                delete_role=str(input("Enter the role to be deleted :"))
                for x in list1:          #FIND AND DELETE A ROLE
                    if x==delete_role:
                        indx=list1.index(delete_role)
                        list1.remove(delete_role)
                        break
                transfer_role=str(input("Enter the role to be transferred :"))
                for x in list1:
                    if x==transfer_role:   #FIND AND REPLACE THE ROLE
                        list1.remove(transfer_role)
                        list1.insert(indx,transfer_role)
                        break
                
    switch()






