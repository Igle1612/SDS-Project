from scapy.all import *
import random
import time
import ipaddress

# List of source IP addresses
public_ips = ['203.0.113.1',
              '72.14.204.147',
              '185.84.244.10',
              '104.244.42.1',
              '192.0.2.123',
              '216.58.214.46',
              '45.33.2.220',
              '66.249.64.1',
              '87.250.250.242',
              '151.101.65.121']

def generate_packet():
    src_ip = random.choice(public_ips)
    dst_ip = "192.168.1.1"
    return IP(src=src_ip, dst=dst_ip)/ICMP()

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
