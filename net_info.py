import socket
import uuid

# get MAC address
def get_mac_address(): 
    mac=uuid.UUID(int = uuid.getnode()).hex[-12:] 
    return ":".join([mac[e:e+2] for e in range(0,11,2)])


# get local ipaddress
def getlocalIPaddress():
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    return ip

# get local computer name
def getlocalcomputername():
    return socket.gethostname()

print(getlocalcomputername())