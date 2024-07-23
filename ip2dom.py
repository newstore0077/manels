import socket

def get_domain(ip_address):
    try:
        domain = socket.gethostbyaddr(ip_address)
        return domain[0]
    except socket.herror:
        return None

input_file = "ip.txt"
output_file = "output.txt"

with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
    for line in infile:
        ip_address = line.strip()
        if ip_address:
            domain = get_domain(ip_address)
            if domain:
                outfile.write(f"{ip_address} -> {domain}\n")
            else:
                outfile.write(f"{ip_address} -> Tidak ditemukan domain\n")
