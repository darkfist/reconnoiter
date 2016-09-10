import os


def get_nmap(ip):
    command = "nmap -F " + ip
    process = os.popen(command)
    results = str(process.read())
    return results
