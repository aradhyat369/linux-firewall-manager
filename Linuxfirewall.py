import os

def firewall_status():
    os.system("sudo ufw status")

def enable_firewall():
    os.system("sudo ufw enable")

def disable_firewall():
    os.system("sudo ufw disable")

def list_rules():
    print("\n--- UFW RULES ---")
    os.system("sudo ufw status numbered")
    print("\n--- IP BLOCK RULES ---")
    os.system("sudo iptables -L INPUT -n --line-numbers")

def block_ip():
    ip = input("Enter IP address to block: ")
    os.system(f"sudo ufw deny from {ip}")
    os.system(f"sudo iptables -I INPUT -s {ip} -j DROP")
    print("IP blocked successfully.")

def allow_ip():
    ip = input("Enter IP address to allow: ")
    os.system(f"sudo ufw delete deny from {ip}")
    os.system(f"sudo iptables -D INPUT -s {ip} -j DROP")
    print("IP allowed successfully.")

def block_port():
    port = input("Enter port to block: ")
    os.system(f"sudo ufw deny {port}")
    print("Port blocked successfully.")

def allow_port():
    port = input("Enter port to allow: ")
    os.system(f"sudo ufw allow {port}")
    print("Port allowed successfully.")

while True:
    print("\n========== LINUX FIREWALL ==========")
    print("1. Firewall Status")
    print("2. Enable Firewall")
    print("3. Disable Firewall")
    print("4. List Rules")
    print("5. Block IP")
    print("6. Allow IP")
    print("7. Block Port")
    print("8. Allow Port")
    print("0. Exit")
    print("====================================")

    choice = input("Enter choice: ")

    if choice == "1":
        firewall_status()
    elif choice == "2":
        enable_firewall()
    elif choice == "3":
        disable_firewall()
    elif choice == "4":
        list_rules()
    elif choice == "5":
        block_ip()
    elif choice == "6":
        allow_ip()
    elif choice == "7":
        block_port()
    elif choice == "8":
        allow_port()
    elif choice == "0":
        print("Firewall program closed.")
        break
    else:
        print("Invalid choice!")