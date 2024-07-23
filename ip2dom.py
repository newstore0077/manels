import socket

def get_domain(ip_address):
    try:
        domain = socket.gethostbyaddr(ip_address)
        return domain[0]
    except socket.herror:
        return None

input_file = input("Masukkan nama file input (misalnya, ip.txt): ")
output_file = "output.txt"

try:
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            ip_address = line.strip()
            if ip_address:
                domain = get_domain(ip_address)
                result = f"{ip_address} -> {domain if domain else 'Tidak ditemukan domain'}"
                print(result)
                outfile.write(result + "\n")
    print(f"Hasil telah disimpan di {output_file}")
except FileNotFoundError:
    print(f"File {input_file} tidak ditemukan. Pastikan file tersebut ada di direktori yang sama dengan script ini.")
