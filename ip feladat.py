import ipaddress

def check_ip(ip):
    try:
        ip_obj = ipaddress.ip_address(ip)
        if ip_obj.version == 4:
            print("Ez egy IPv4-es cím")
        elif ip_obj.version == 6:
            print("Ez egy IPv6-os cím")
    except ValueError:
        print("Ez se IPv4-es, se IPv6-os cím")
while True:
    ipcim = input("Adj meg egy IP címet: ")
    check_ip(ipcim.strip())
