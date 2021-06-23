my_list=["tomer turkian" , "37" , "tomerturkian@gmail.com" , "0524217995"]
#print(my_list)

print("my name: " +my_list[0] + "\nAge: " + str(my_list[1]) + "\nmy email: " + my_list[2] + "\nmy phone: " +  my_list[3])

IP_list=["192.168.5.6" , "192.168.5.7"]
print(IP_list)
IP_list.append("192.168.5.8")
IP_list.append("192.168.5.9")
IP_list.append("192.168.5.10")
print(IP_list)
IP_list.pop(2)
print(IP_list)
print("The lehgth ip is: " + str(len(IP_list)) + "\n and the ip list: " + str(IP_list))