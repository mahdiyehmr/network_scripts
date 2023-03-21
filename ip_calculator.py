ip_with_cidr = input("Please enter your IP address with its cidr [e.g. 192.168.3.10/24]:\n")
if("." not in ip_with_cidr):
    print("Invalid input")
elif(ip_with_cidr.count(".")!=3):
    print("Invalid input")
elif(ip_with_cidr.startswith(".")):
    print("Invalid input")
elif(ip_with_cidr.endswith("/")):
    print("Invalid input")
elif("/" not in ip_with_cidr):
    print("Invalid input")
else:
    #seperating ip and cidr
    list_ip_cidr = ip_with_cidr.split("/")
    ip = list_ip_cidr[0]
    cidr = int(list_ip_cidr[1])
    if (cidr < 1 or cidr > 32):
        print("Invalid cidr")
    else:
        #seperating octets
        list_ip = ip.split(".")
        #add each octet in a variable and making it integer
        first_octet = int(list_ip[0])
        second_octet = int(list_ip[1])
        third_octet = int(list_ip[2])
        forth_octet = int(list_ip[3])
        if (first_octet < 0 or second_octet < 0 or third_octet < 0 or forth_octet < 0):
            print("Invalid! Can't have negative input")
        elif first_octet == 0 :
            print("Invalid! First octet can't be zero")
        elif ( first_octet > 255 or second_octet > 255 or third_octet > 255 or forth_octet > 255):
            print("Invalid! Can't have value greater than 255")
        elif(first_octet == 127):
            print("reserved IP for loopback")
        elif(first_octet == 169 and second_octet == 254):
            print("APIPA")
        elif 223 < first_octet < 240:
            print("Class D:multicast")
        elif 239 < first_octet < 256:
            print("Class E")
        elif first_octet == second_octet == third_octet == forth_octet == 255:
            print("Reserved broadcast")
        else:
            #calculating subnet mask from cidr
            if cidr < 8:
                first = 0
                broadcast_first = 0
                # calculating subnet mask from cidr
                for i in range(0 , cidr):
                    first += pow(2,7 - i)
                #calculating broadcast first octet
                for i in range(0,8 - cidr):
                    broadcast_first += pow(2,i)
                subnet_mask = str(first)+".0.0.0"
                netid = str(first & first_octet)+".0.0.0"
                first_ip = str(first & first_octet) + ".0.0.1"
                last_ip = str((first & first_octet) + broadcast_first) + ".255.255.254"
                broadcast = str((first & first_octet) + broadcast_first) + ".255.255.255"
            elif cidr < 16:
                second = 0
                broadcast_second = 0
                for i in range(0 , cidr - 8):
                    second += pow(2,7 - i)
                for i in range(0,16 - cidr):
                    broadcast_second += pow(2,i)
                subnet_mask = "255."+ str(second)+".0.0"
                netid = list_ip[0] + "." + str(second & second_octet) + ".0.0"
                first_ip = list_ip[0] + "." + str(second & second_octet) + ".0.1"
                last_ip = list_ip[0] + "." + str((second & second_octet) + broadcast_second) + ".255.254"
                broadcast = list_ip[0] + "." + str((second & second_octet) + broadcast_second) + ".255.255"
            elif cidr < 24:
                third = 0
                broadcast_third = 0
                for i in range(0 , cidr - 16):
                    third += pow(2,7 -i)
                for i in range(0, 24 - cidr):
                    broadcast_third += pow(2,i)
                subnet_mask = "255.255." + str(third) + ".0"
                netid = list_ip[0] + "." + list_ip[1] + "." + str(third & third_octet) + ".0"
                first_ip = list_ip[0] + "." + list_ip[1] + "." + str(third & third_octet) + ".1"
                last_ip = list_ip[0] + "." + list_ip[1] + "." + str((third & third_octet) + broadcast_third) + ".254"
                broadcast = list_ip[0] + "." + list_ip[1] + "." + str((third & third_octet) + broadcast_third) + ".255"
            else:
                forth = 0
                broadcast_forth = 0
                for i in range(0 , cidr - 24):
                    forth += pow(2,7 - i)
                for i in range(0, 32 - cidr):
                    broadcast_forth += pow(2,i)
                subnet_mask = "255.255.255."+ str(forth)
                netid = list_ip[0] + "." + list_ip[1] + "." + list_ip[2] + "." + str(forth & forth_octet)
                first_ip = list_ip[0] + "." + list_ip[1] + "." + list_ip[2] + "." + str((forth & forth_octet) + 1)
                last_ip = list_ip[0] + "." + list_ip[1] + "." + list_ip[2] + "." + str((forth & forth_octet) + broadcast_forth -1)
                broadcast = list_ip[0] + "." + list_ip[1] + "." + list_ip[2] + "." + str((forth & forth_octet) + broadcast_forth)
                if(cidr == 32):
                    first_ip = last_ip = broadcast = netid
            print(f"Subnet Mask: {subnet_mask}")
            print(f"Network Id: {netid}")
            print(f"First IP: {first_ip}")
            print(f"Last IP: {last_ip}")
            print(f"Broadcast : {broadcast}")
