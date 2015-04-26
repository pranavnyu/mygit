__author__ = 'pranavrajtyagi'

def is_valid_address(address):
    try:
        split_add = address.split('.')
        last = split_add.pop(3)
        last_part = last.split(':')
        split_add.insert(3,last_part[0])
        last_part.pop(0)
        valid_ip = ip_add(split_add)
        valid_port = port_add(last_part)
        if valid_ip == True and valid_port == True:
            return True
    except IndexError:
        print "not a valid address"



def ip_add(split_add):
    for part in split_add:
        if int(part) >= 0 and int(part) <= 255:
            continue
        else:
            print "not a valid address"
            return False

    return True

def port_add(last_part):
    for port in last_part:
        if int(port) >= 1 and int(port) <= 65636:
            continue
        else:
            print "not a valid port number"
            return  False

    return True
def main():
    address  =raw_input("Enter the address here: ")
    validation = is_valid_address(address)
    if validation == True:
        print "this is a valid address"

main()

