'''Users can be added and a role can be assigned to them. Same role can be assigned to more than one user but an user can have only single role. So support Add User operation and Display Users operation (users can be displayed in any order).'''



list1=[]  #ROOT ROLE
list11=[] #ALL ROLE
list2=[]  #CEO SUB ROLE
list3=[]  #COO,CTO SUB ROLE
list4=[]  #SENIOR SUB ROLE
nlist=[]  #STORING ROLE ONLY ALLOCATE THE USER
namelist=[] #NAMELIST

root_role=str(input("Enter root role name : "))
list1.append(root_role)
list11.append(root_role)
while True:
    def switch():
            print("Operations.")
            print("1.Add Sub Role.")
            print("2. Display Roles.")
            print("3. Delete Role.")
            print("4. Add User.")
            print("5. Display Users.")
            operation=int(input())
            if operation==1:
                print("operation to be performed : 1")
                sub_role=str(input("Enter sub role name : "))
                rep_role=str(input("Enter reporting to role name : "))
                if rep_role == root_role:   #CHECK SUB ROLE OF CEO
                    list1.append(sub_role)
                    list2.append(sub_role)
                elif rep_role != root_role:  #CHECK SUB ROLE OF CEO
                    for x in list2:
                        if list2[0]==rep_role: 
                            list1.append(sub_role)
                            list3.append(sub_role)
                            break
                        elif list2[1]==rep_role:
                            list1.append(sub_role)
                            list4.append(sub_role)
                            break
            elif operation==2:
                if not len(list1):
                    print("empty")
                else:
                    print(*list1)
            elif operation==3:   #DELETE AND TRANSFER
                print("Operation to be performed : 3")
                delete_role=str(input("Enter the role to be deleted :"))
                for x in list1:   #FIND AND DELETE
                    if x==delete_role:
                        indx=list1.index(delete_role)
                        list1.remove(delete_role)
                        break
                transfer_role=str(input("Enter the role to be transferred :"))
                for x in list1:   #FIND AND TRANSFER
                    if x==transfer_role:
                        list1.remove(transfer_role)
                        list1.insert(indx,transfer_role)
                        break
            elif operation==4: #ADD USER
                print("Operation to be performed : 4")
                user_name=str(input("Enter User Name :"))
                role_name=str(input("Enter Role :"))
                for x in list1:
                    if x==role_name:
                        nlist.append(role_name) #ROLE ONLY ALLOCATE THE USER
                        namelist.append(user_name) #USERS LIST
            elif operation==5:
                print("Operation to be performed : 5")
                if not len(namelist):
                    print("empty")
                elif len(namelist)==len(nlist):
                    for x in range (len(namelist)): #PRINT USERS
                        print( namelist[x]," - ",nlist[x])
                
           
    switch()
