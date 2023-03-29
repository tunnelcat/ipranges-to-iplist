#!/usr/bin/python3
import argparse

def ip_range(start_ip,end_ip):
    start = list(map(int,start_ip.split('.')))
    end = list(map(int,end_ip.split('.')))
    iprange=[start_ip]
    while start!=list(map(int,end_ip.split('.'))):
        for i in range(len(start)-1,-1,-1):
            if start[i]<255:
                start[i]+=1
                break
            else:
                start[i]=0
        iprange.append('.'.join(map(str,start)))
    return iprange

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    args = parser.parse_args()

    with open(args.filename) as file:
        for line in file:
            # strip trailing newline
            linestrip = line.rstrip('\n')

            # process lines with ranges
            if '-' in linestrip:
                arr = linestrip.split('-')
                
                # format: 192.168.1.1-192.168.1.3
                if '.' in arr[1]:
                    for ip in ip_range(arr[0],arr[1]):
                        print(ip)

                # format: 192.168.1.1-3
                else: 
                    start_octet = int(arr[0].split('.')[3])
                    end_octet = int(arr[1])

                    base_octets = '.'.join(arr[0].split('.')[0:3]) 
                    for i in range(start_octet, end_octet+1):
                        print(base_octets + '.' + str(i))

            # no range, treat like a single IP
            else: 
                print(linestrip)

if __name__=='__main__':
    main()
