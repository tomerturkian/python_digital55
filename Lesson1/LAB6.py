from time import sleep
choise=(input("menu: enter your choise:\n1.insert a number:\n2.insert 4 adress IP:\n3.insert 4DNS:\n4.check if string is polindrom\n"))
if(choise=="1"):
    print("the new number is: " +str((int(input("enter a number: " )))**3))
elif(choise=="2"):
    list_ip=[]
    list_ip.append(input("enter new ip: "))
    list_ip.append(input("enter new ip: "))
    list_ip.append(input("enter new ip: "))
    list_ip.append(input("enter new ip: "))
    print("The new_list:\n" +str(list_ip))
elif(choise=="3"):
    dns_dict={}
    dns_dict.update({input("enter a url: "): input("enter IP: ")})
    dns_dict.update({input("enter a url: "): input("enter IP: ")})
    dns_dict.update({input("enter a url: "): input("enter IP: ")})
    dns_dict.update({input("enter a url: "): input("enter IP: ")})
    print("\nthe new dns_dict:\n" +str(dns_dict))
elif(choise=="4"):
    word=input("enter a word: ")
    if (word == word[::-1]):
        print("this is polindrom!")
    else:
        print("this isn't polindrom!")
else:
    print("Enter 1-4 onley!")





