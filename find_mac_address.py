from netmiko import ConnectHandler
# Define parameters for multiple device
sw1 = {
    "device_type": "cisco_ios",
    "ip": "192.168.10.1",
    "username": "mahdiyeh",
    "password": "mirsharifi"
}

sw2 = {
    "device_type": "cisco_ios",
    "ip": "192.168.10.11",
    "username": "mahdiyeh",
    "password": "mirsharifi"
}

sw3 = {
    "device_type": "cisco_ios",
    "ip": "192.168.10.12",
    "username": "mahdiyeh",
    "password": "mirsharifi"
}

sw4 = {
    "device_type": "cisco_ios",
    "ip": "192.168.10.13",
    "username": "mahdiyeh",
    "password": "mirsharifi"
}

sw5 = {
    "device_type": "cisco_ios",
    "ip": "192.168.10.14",
    "username": "mahdiyeh",
    "password": "mirsharifi"
}

sw6 = {
    "device_type": "cisco_ios",
    "ip": "192.168.10.15",
    "username": "mahdiyeh",
    "password": "mirsharifi"
}

sw7 = {
    "device_type": "cisco_ios",
    "ip": "192.168.10.16",
    "username": "mahdiyeh",
    "password": "mirsharifi"
}
def check_arp(device,ip):
        output = []
        try:
                net_connect = ConnectHandler(**device)
                output = net_connect.send_command("show arp | i "+ip)
        except Exception:
                pass
        if(len(output)>0):
                output =str(output).split()
                if(ip != output[1]):
                        pass
                else:
                        exists = True
        return output
def check_mac_table(device,mac):
        output = []
        try:
                net_connect = ConnectHandler(**device)
                output = net_connect.send_command("show mac address-table | i "+mac)
        except Exception:
                pass
        if(len(output)>0):
            output =str(output).split()
        return output
ip = raw_input("Please enter the IP address [e.g. 192.168.10.10]")
#checking if device is connected
arp = check_arp(sw1,ip)
if(not arp):
        print("Device isn't connected or IP doesn't exists!")
        exit()
mac = arp[3]
mac_record = check_mac_table(sw1,mac)
if(mac_record[3] == "Et0/0"):
#device is under SW2
    switch = sw2
else:
#device is under SW3
    switch = sw3
mac_record = check_mac_table(switch,mac)
if(mac_record):
        if(switch == sw2):
            #check if device is under SW4
            if(mac_record[3] == "Et0/1"):
                switch = sw4
                switch_name = "SW4"
            else:
            #device is under SW5
                switch = sw5
                switch_name = "SW5"
            output = check_mac_table(switch,mac)
            print("The device is connected to port {} of {}. The mac address is {}. The device belongs to vlan{}".format(output[3],switch_name,mac,output[0]))
        else:
        #device is under SW3
            mac_record = check_mac_table(sw3,mac)
            if(mac_record):
                if(mac_record[3] == "Et0/1"):
                    switch = sw6
                    switch_name = "SW6"
                else:
                #device is under SW7
                    switch = sw7
                    switch_name = "SW7"
                output = check_mac_table(switch,mac)
                print("The device is connected to port {} of {}. The mac address is {}. The device belongs to vlan{}".format(output[3],switch_name,mac,output[0]))
