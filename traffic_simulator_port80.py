from scapy.all import *
import random
import time
import ipaddress

# List of source IP addresses
public_ips = []
while len(public_ips) < 20:
    ip = ipaddress.IPv4Address(random.getrandbits(32))
    if not ip.is_private:
        public_ips.append(str(ip))

# Get a random IP from the list and send a TCP request to PORT 80
def generate_packet():
    src_ip = random.choice(public_ips)
    dst_ip = "192.168.1.101"
    return IP(src=src_ip, dst=dst_ip)/TCP(sport=3000, dport=80) 

# Simulate traffic for 10 minutes
start_time = time.time()
while (time.time() - start_time) < 600:
    num_connections = random.randint(1, 10)
    
    # Send num_connections number of recuests
    for i in range(num_connections):
        start_time_conn = time.time()
        # send the request using a random delay between every request
        while (time.time() - start_time_conn) < 20:
            packet = generate_packet()
            
            delay = random.randint(1, 10)
            time.sleep(delay)
            
            send(packet, verbose=False)
    
    delay = random.randint(1, 10)
    time.sleep(delay)

print("Traffic simulation complete.")
