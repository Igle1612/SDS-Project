# SDS-Project

**Start and create topology**

To execute and create the topo we must use `sudo python2 createTopo.py`

In */etc/snort/snort.conf* add the custom rules: `include $RULE_PATH/Myrules.rules`

Comment line: `$RULE_PATH/icmp-info.rules`

Then execute : `cp Myrules.rules /ets/snort/rules/`

**LoadBalancer:**

In other console execute `ryu-manager --ofp-tcp-listen-port 6634 load_balancer.py`

**Snort:**

First we create the interface executing: `sudo ./configSnort.sh`

To check the port number (it should be 8, if not it has to be changed on *telegraf_snort.py*: `sudo ovs-ofctl show s0 -O OpenFlow13`

To execute snort we must execute `sudo snort -i s0-snort -A unsock -l /tmp -c /etc/snort/snort.conf`

Then to execute ryu we use: `sudo ryu-manager --ofp-tcp-listen-port 6633 telegraf_snort.py`

**Redirection:**

As the *telegraf_snort.py* is already running, we just have to create the rules with *switchRules.sh* and execute `sudo ./switchRules.sh`

**Test:**
1. Load Balancer:

  Then, in mininet execute:
  `xterm h1 h2 h3 h4 h5 `

  And for each server:
  `python3 -m http.server 80`

  To test: `hout2 curl 192.168.1.100`

2. Snort:
   
   From hout1 execute: `attack_port80.py` or `attack.py`

   Then you should see some warnings going out.

3. Redirection:

   To check that redirection works try to ping should be enough. Honeypot should answer but the other ones no, as all is redirected to the honeyPot.
