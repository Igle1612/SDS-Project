from scapy.all import *
import random
import time

# List of source IP addresses
public_ips = ['10.0.1.10', '10.0.2.10', '10.0.3.10', '10.0.4.10', '10.0.5.10']

def generate_packet():
    src_ip = random.choice(public_ips)
    dst_ip = "192.168.1.101"
    return IP(src=src_ip, dst=dst_ip)/TCP(sport=RandShort(), dport=80) 

num_requests = 50
duration = 600
cicle_time = 5
increase_factor = 25
elapsed_time = 0
requests_sent = 0

# Main loop
while elapsed_time < duration:
    start_time = time.time()
    print("Start sending:", num_requests, "requests every", cicle_time, "seconds")
    while time.time() - start_time < cicle_time and requests_sent < num_requests:
        packet = generate_packet()
        
        time.sleep(cicle_time/num_requests)
        
        send(packet, verbose=False)
        
        requests_sent += 1
    
    elapsed_time = int(time.time() - start_time)
    num_requests += increase_factor

    print(f"Elapsed time: {elapsed_time}s, Number of requests sent: {requests_sent}")

print("Traffic simulation complete.")
