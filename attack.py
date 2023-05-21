from scapy.all import *
import random
import time
import ipaddress
import socket

def get_ip_address():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address

def generate_packet():
    src_ip = node_ip
    dst_ip = "192.168.1.1"
    return IP(src=src_ip, dst=dst_ip)/ICMP()

node_ip = get_ip_address()
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
