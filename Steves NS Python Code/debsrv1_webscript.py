import pycurl, time, random

# Set up list with the interfaces, example below
# interface_list = ["eth0", "eth1", "ifgrp1-3", "e8-2"]

interface_list = ["ens192","ens192:0","ens192:1","ens192:2","ens192:3","ens192:4","ens192:5","ens192:6"]

# Set up server list to hit:
# server_list = ["192.168.0.20", "192.168.0.21", "192.168.0.22"]

server_list = ["172.31.10.11","172.31.10.12","172.31.10.13","172.31.10.14","172.31.10.15","172.31.10.16","172.31.10.17"]

# Creates curl object and performs it
def curl_post(url, iface, output, user_agent=None):
    # Set up the curl object
    curl = pycurl.Curl()
    curl.setopt(pycurl.URL, url)
    curl.setopt(pycurl.FOLLOWLOCATION, 1)
    curl.setopt(pycurl.INTERFACE, iface)
    curl.setopt(pycurl.SSL_VERIFYHOST, 0)
    curl.setopt(pycurl.SSL_VERIFYPEER, 0)
    if user_agent == "Safari":
        curl.setopt(pycurl.USERAGENT, 'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_0_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15')
    if user_agent == "Chrome":
        curl.setopt(pycurl.USERAGENT, 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36')
    # Hide terminal output if False param
    if output == False:
        curl.setopt(pycurl.WRITEFUNCTION,lambda x : None)
    curl.perform()
    curl.close()

# Define different tests below

# Hit each interface to each server once
def alpha():
    print('Now Running Alpha')
    for interface in interface_list:
        for server in server_list:
#            print('interface {0} : curl {1}\n\n'.format(interface, server))
            curl_post(server, interface, False, "Safari")

# eth0 hits google 100 times
def beta():
    # eth0
    for x in range(100):
        curl_post("www.google.com", "eth0", True)
    print("\n\neth0 interface 100 curls to Google done!\n")

def gamma():
    print('Now Running Gamma')
    for interface in interface_list:
        for server in server_list:
#            print('interface {0} : curl {1}\n\n'.format(interface, server))
            curl_post(server, interface, False, "Chrome")


# Main function that executes the tests above
if __name__ == "__main__":
# To run continuously, use while command
# To stop, ps -aux and use kill command on process id
#   while True:
    for x in range(100):
        alpha()
#       beta()
        gamma()
        sleeptime=random.randrange(0,10)
        print('Sleeping for',sleeptime)
        time.sleep(sleeptime)

# To run and close terminal, use nohup command.
# nohup python3 debsrv1_webscript.py &