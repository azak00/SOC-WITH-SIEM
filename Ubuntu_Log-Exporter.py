import re
import requests

### Requirement ####

## pip install requests

## Continuously monitor log file ###

### watch -n 30 sudo python3 Auth_Log_check.py ### run script every 30 sec



# Define variables for user customization
API_KEY = 'IPGEO_API_KEY'  # Replace with  actual API key
LOG_FILE_PATH = '/var/log/auth.log'  # Path to the auth log file
OUTPUT_FILE_PATH = 'Failed_ssh_geodata.log'  # Path to write geo data 

def get_geo_data(ip):
    url = f"https://api.ipgeolocation.io/ipgeo?apiKey={API_KEY}&ip={ip}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

def process_log_file(logfile):
    ips = set()
    with open(logfile, 'r') as file:
        for line in file:
            pattern = re.compile(r'Failed password for (\S+) from (\d+\.\d+\.\d+\.\d+) port')
            match = pattern.search(line)
            if match:
                username = match.group(1)
                ip = match.group(2)
                if ip not in ips:
                    ips.add(ip)
                    geo_data = get_geo_data(ip)
                    if geo_data:
                        with open(OUTPUT_FILE_PATH, 'a') as output_file:
                            output_file.write(f"IP: {ip}, Username: {username}, Latitude: {geo_data['latitude']}, Longitude: {geo_data['longitude']}, Country: {geo_data['country_name']}, State: {geo_data['state_prov']}, City: {geo_data['city']}\n")

if __name__ == "__main__":
    process_log_file(LOG_FILE_PATH)
