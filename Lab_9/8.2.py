import dpkt, sys

ip_list = []

src = {}
dst = {}

pcap = dpkt.pcap.Reader(open(sys.argv[1]))

for (_, buffer) in pcap:

    connection = dpkt.ethernet.Ethernet(buffer)
    
    if connection.type != dpkt.ethernet.ETH_TYPE_IP:
        continue
    
    ip = connection.data
    
    if ip.p != dpkt.ip.IP_PROTO_TCP:
        continue
        
    tcp = ip.data

    if not (tcp.flags & dpkt.tcp.TH_SYN):
        host = ip.src
        
        if host not in src:
            src[host] = 1
        
            if host not in ip_list:
                ip_list.append(host)
        
        else:
            src[host] += 1

    if tcp.flags & (dpkt.tcp.TH_SYN | dpkt.tcp.TH_ACK):
        host = ip.dst
        
        if host not in dst:
            
            dst[host] = 1
            
            if host not in ip_list:
                ip_list.append(host)

        else:
            dst[host] += 1

output_file = open('8.2.txt', 'w')

for ip in ip_list:
    if (ip in src) and (ip in dst):
        
        ip_str = ip.encode('hex')

        output_file.write(str(int(ip_str[0:2], 16)))
        output_file.write('.')
        output_file.write(str(int(ip_str[2:4], 16)))
        output_file.write('.')
        output_file.write(str(int(ip_str[4:6], 16)))
        output_file.write('.')
        output_file.write(str(int(ip_str[6:8], 16)))
        output_file.write(' ' + str(src[ip]) + ' ' + str(dst[ip]) + '\n')

print 'Written IP Addresses to File : 8.2.txt Successfully'