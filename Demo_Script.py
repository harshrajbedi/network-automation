import getpass
import sys
import telnetlib

HOST = " " #ip_address of the target device
user = raw_input("Enter Telnet Username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until("Username: ")
tn.write(user + "\n")
if password:
    tn.read_until("Password: ")
    tn.write(password + "\n")

#below are the commands to execute on device
tn.write("enable\n")
tn.write("conf t\n")
tn.write("int g0/0")
tn.write("ip address 192.168.1.1 255.255.255.0\n")
tn.write("no shut\n")
tn.write("int g0/1")
tn.write("ip address 192.168.2.1 255.255.255.0\n")
tn.write("no shut\n")
tn.write("exit\n")
tn.write("router ospf 1\n")
tn.write("network 192.168.0.0 0.0.255.255 area 0\n")
tn.write("end\n")
tn.write("exit\n")

print tn.read_all()