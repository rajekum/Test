import re
def grab_ip(file):
    ips = []
    occurence = {}
    with open("/Users/rajekum/Documents/git/file.txt") as file:
        for ip in file:
            ip_data=re.findall(r'(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})',ip)
            for i in ip_data:
                ips.append(i)
        for ipaddr in ips:
            if ipaddr in occurence:
                occurence[ipaddr] = occurence[ipaddr] + 1
            else:
                occurence[ipaddr] = 1
        final = sorted(occurence.items(), key = 
             lambda kv:(kv[1], kv[0]))
        for x in reversed(final):
            print(x)
print(grab_ip('data'))
