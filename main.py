from general import *
from domain_name import *
from ip_address import *
from nmap import *
from robots_txt import *
from whois import *


print("\nWelcome to Reconnoiter - A Python based Web Scanner")
print('Get "nmap", "robots.txt" and "whois" data of any website in seconds.')

name = input("\nGive a name to this project: ")
url = input("Enter the url you want to scan: ")
print("\nPlease wait while we are scanning the website and obtaining data...")

root_dir = "Reports"
create_dir(root_dir)


def gather_info(name, url):
    domain_name = get_domain_name(url)
    ip_address = get_ip_address(url)
    nmap = get_nmap(ip_address)
    print('"nmap" data scanned, obtained and stored in a file...')
    robots_txt = get_robot_txt(url)
    print('"robots.txt" data scanned, obtained and stored in a file...')
    whois = get_whois(domain_name)
    print('"whois" data scanned, obtained and stored in a file...')
    create_report(name, nmap, robots_txt, whois)


def create_report(name, nmap, robots_txt, whois):
    project_dir = root_dir + "/" + name
    create_dir(project_dir)

    write_file(project_dir + "/nmap.txt", nmap)
    write_file(project_dir + "/robots.txt", robots_txt)
    write_file(project_dir + "/whois.txt", whois)


gather_info(name, url)
print("\nWebsite scanning complete. All data is stored in " + name + " directory\n")
