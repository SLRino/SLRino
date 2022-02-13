'''Support delete user operation and also while deleting a role the user with the current role is transferred to the role to be transferred.'''




list1=[]  #ALL ROLE
list11=[] #ROOT ROLE
list2=[]  #CEO SUB ROLE
list3=[]  #COO,CTO SUB ROLE
list4=[]  #SENIOR SUB ROLE
nlist=[]  #STORING ROLE ONLY ALLOCATE THE USER
namelist=[] #NAMELIST
listname1=[] #USER OF ROOT ROLE
listname2=[] #USER OF CEO SUB ROLE
listname3=[] #USER OF COO,CTO SUB ROLE
listname4=[] #ALL USER 
listname44=[] #USER OF SENIOR SUB ROLE
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
            print("6. Display Users and Sub Users.")
            print("7. Delete User.")
            operation=int(input())
            if operation==1:
                print("operation to be performed : 1")
                sub_role=str(input("Enter sub role name : "))
                rep_role=str(input("Enter reporting to role name : "))
                if rep_role == root_role:     #CHECK SUB ROLE OF CEO
                    list1.append(sub_role)
                    list2.append(sub_role)
                elif rep_role != root_role:    #CHECK SUB ROLE OF CEO
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
                print("operation to be performed : 2")
                if not len(list1):
                    print("empty")
                else:
                    print(*list1)
            elif operation==3:     #DELETE AND TRANSFER
                print("Operation to be performed : 3")
                delete_role=str(input("Enter the role to be deleted :"))
                for x in list1:     #FIND AND DELETE
                    if x==delete_role:
                        indx=list1.index(delete_role)
                        list1.remove(delete_role)
                        break
                transfer_role=str(input("Enter the role to be transferred :"))
                for x in list1:     #FIND AND TRANSFER
                    if x==transfer_role:
                        list1.remove(transfer_role)
                        list1.insert(indx,transfer_role)
                        break
            elif operation==4:  #ADD USER
                print("operation to be performed : 4")
                user_name=str(input("Enter User Name :"))
                role_name=str(input("Enter Role :"))
                for x in list1:
                    if x==role_name:
                        nlist.append(role_name)   #ROLE ONLY ALLOCATE THE USER
                        namelist.append(user_name)   #USERS LIST
            elif operation==5:   
                print("operation to be performed : 5")
                if not len(namelist):
                    print("empty")
                elif len(namelist)==len(nlist):   
                    for x in range (len(namelist)):
                        print( namelist[x]," - ",nlist[x])  #PRINT USERS
            elif operation==6:
                print("operation to be performed : 6")
                for x in range(len(namelist)):  #ARRANGE THE USER BASED ON ROLES
                    store=nlist[x]
                    store1=namelist[x]
                    for i in list11:   #FIND A ROOT ROLE OF USER
                        if store==i:
                            listname1.append(store1)
                    for i in list2:   #FIND A CEO SUB ROLE OF USER
                        if store==i:
                            listname2.append(store1)
                    for i in list3:  #FIND A COO SUB ROLE OF USER
                        if store==i:
                            listname3.append(store1)
                    for i in list4: #FIND A CTO SUB ROLE OF USER
                        if store==i:
                            listname44.append(store1)
                listname4.extend(listname1) #STORE THE ARRANGED USER
                listname4.extend(listname2)
                listname4.extend(listname44)
                listname4.extend(listname3)
                
                for x in listname4: #PRINT THE ALL USER
                    stor1=x
                    for i in listname1: #PRINT A ROOT ROLE OF USER
                        if stor1==i:
                            print(i," - ",*listname2,*listname44,*listname3)
                    for i in listname2:  #PRINT A CEO SUB ROLE OF USER
                        if stor1==i:
                            print(i," - ",*listname3)
                    for i in listname44:  #PRINT A COO SUB ROLE OF USER
                        if stor1==i:
                            print(i," - ")
                    for i in listname3:   #PRINT A CTO SUB ROLE OF USER
                        if stor1==i:
                            print(i," - ")
            elif operation==7:
                print("operation to be performed : 7")
                delete_user=str(input("Enter username to be deleted :"))
                for x in listname4:    #FIND AND DELETE THE USER
                    if delete_user==x:
                        listname4.remove(x)
                        for x in listname1:
                            if x==delete_user:
                                listname1.remove(x)
                        for x in listname2:
                            if x==delete_user:
                                listname2.remove(x)
                        for x in listname3:
                            if x==delete_user:
                                listname3.remove(x)
                for x in listname4:   #PRINT THE ALL USER
                    stor1=x
                    for i in listname1:
                        if stor1==i:   #PRINT THE ROLE UNDER ROOT ROLE
                            print(i," - ",*listname2,*listname44,*listname3)
                    for i in listname2:
                        if stor1==i:   
                            print(i," - ",*listname3)

                    for i in listname44:
                        if stor1==i:
                            print(i," - ")
                    for i in listname3:
                        if stor1==i:
                            print(i," - ")
    switch()