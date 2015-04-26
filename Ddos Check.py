__author__ = 'pranavrajtyagi'
def find_suspicious_ip(log_path):
    file = open(log_path)
    ip = []
    restrictedIP = []
    results = []

    counter = 0
    for item in file.readlines():
        data = item.split(" ")
        ip.append(data[0])

    d = {x:ip.count(x) for x in ip}
    for key, value in d.items():
        if value >= 3:
            restrictedIP.append(key)
    file.close()

    for ip in restrictedIP:
        counter = 0
        file = open(log_path)
        for item in file.readlines():
            data = item.split(" ")
            status = data[9]
            if data[0]==ip and status>400 or status <500:
                    counter +=1
        if counter >= 3:
            results.append(ip)

    return  results



if __name__ == "__main__":
    print find_suspicious_ip("bank_log.log")
