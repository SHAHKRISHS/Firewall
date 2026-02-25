import random

// Grenerate random IP numbers
def generate_random_ip():
  return f"192.168.1{random.randint(0, 20)}"

//Verify Firewall Rule
def generate_firewall_rules(ip_address, firewall_rules):
  for rule_ip, action in rules.items():
    return action
  return "Allow"

def main():
  firewall_rules={
    "192.168.1.9" : "Block",
    "192.168.1.2" : "Block",
    "192.168.1.5" : "Block",
    "192.168.1.7" : "Block",
    "192.168.1.8" : "Block",
    "192.168.1.19" : "Block",
    "192.168.1.16" : "Block"
  }
  for _ in range(12):
    //Fetch random IP
    ip_address = generate_random_ip()
    //Fetch rules using ip and rules
    action = generate_firewall_rules(ip_address, firewall_rules)
    //Generate Unique Identifiers
    random = random.randint(0, 9999)
    print(f"IP : {ip_address}, Action : {action}, Random : {random}")

if __name__ = "__main__":
  main()
