import geoip2.database
import ipaddress
import re
import requests
import os
import logging
from collections import OrderedDict

# 设置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# GeoIP 数据库文件路径
GEOIP_DB_PATH = 'GeoLite2-Country.mmdb'

def get_location_from_db(ip):
    if not os.path.exists(GEOIP_DB_PATH):
        logger.error(f"GeoIP database file not found at {GEOIP_DB_PATH}")
        return None

    try:
        with geoip2.database.Reader(GEOIP_DB_PATH) as reader:
            response = reader.country(ip)
            return response.country.iso_code
    except Exception as e:
        logger.error(f"Error querying GeoIP database for IP {ip}: {str(e)}")
        return None

def get_location_from_api(ip):
    try:
        response = requests.get(f"https://ipapi.co/{ip}/country_code/")
        if response.status_code == 200:
            return response.text.strip()
    except Exception as e:
        logger.error(f"Error querying online API for IP {ip}: {str(e)}")
    return None

def get_location(ip):
    location = get_location_from_db(ip)
    if location is None:
        logger.info(f"Falling back to online API for IP {ip}")
        location = get_location_from_api(ip)
    return location or "Unknown"

def extract_ip_and_port(input_string):
    pattern = r'((\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|[0-9a-fA-F:]+)(?::(\d+))?)'
    match = re.match(pattern, input_string)
    if match:
        full_match, ip, port = match.groups()
        return ip, full_match
    return None, None

def validate_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

# 输入的IP地址
input_data = """
162.159.153.160
162.159.153.233
162.159.153.168
162.159.153.47
162.159.153.32
162.159.152.55
162.159.153.247
162.159.152.215
162.159.153.244
162.159.152.153
162.159.153.191
162.159.152.236
162.159.153.78
162.159.152.6
162.159.152.208
162.159.153.202
162.159.153.87
162.159.152.177
162.159.153.57
162.159.153.35
104.19.57.19
104.19.57.11
104.19.32.105
104.19.63.165
104.19.56.252
104.19.57.21
104.19.56.248
104.19.58.164
104.19.62.96
104.19.32.79
104.19.32.104
104.19.63.178
104.19.60.188
104.19.62.32
104.19.32.88
104.19.57.24
104.19.58.226
104.19.63.237
104.19.58.169
104.19.32.169
162.159.153.247#CT
162.159.153.168#CT
162.159.153.32#CT
162.159.152.208#CT
162.159.153.160#CT
162.159.153.78#CT
162.159.153.233#CT
162.159.152.177#CT
172.64.142.255#CM-HKG
172.64.141.241#CM-LAX
172.67.177.83#CM-SEA
172.67.182.254#CM-SEA
172.67.163.130#CM-SEA
172.67.120.210#CU-LAX
172.64.162.72#CU-LAX
172.67.103.151#CU-LAX
172.64.97.71#CU-LAX
172.67.108.109#CU-LAX
172.64.135.241#CT-SJC
172.67.229.227#CT-LHR
172.67.201.241#CT-LHR
172.67.214.76#CT-LHR
104.19.248.79#CT-LAX
172.66.0.233#CF-27.01MB/s
198.41.196.11#CF-26.82MB/s
104.19.16.230#CF-26.04MB/s
104.18.51.56#CF-24.25MB/s
104.18.54.169#CF-24.17MB/s
172.66.153.88#CF-15.77MB/s
104.18.115.135#CF-12.92MB/s
104.18.56.136#CF-10.55MB/s
104.19.142.247#CF-7.4MB/s
104.16.113.66:443#CT-TG@Warp_Key
104.18.125.207:443#CT-TG@Warp_Key
162.159.39.119:443#CT-TG@Warp_Key
162.159.153.174:443#CN-TG@Warp_Key
104.17.217.69:443#CN-TG@Warp_Key
104.16.155.28:443#CN-TG@Warp_Key
104.19.43.77:443#CM-TG@Warp_Key
104.19.34.103:443#CM-TG@Warp_Key
104.19.39.130:443#CM-TG@Warp_Key
172.64.21.215:443#CU-TG@Warp_Key
172.64.161.155:443#CU-TG@Warp_Key
104.19.122.68:443#CU-TG@Warp_Key
47.242.176.237:2053#HK
8.210.43.213:2053#HK
47.242.60.161:443#HK
43.154.181.11:11021#HK
47.75.101.0:3443#HK
47.76.33.40:2083#HK
47.76.33.40:2096#HK
119.247.140.108:29722#HK
58.176.95.46:443#HK
58.176.229.127:35002#HK
35.187.231.66:55740#SG
43.156.6.97:10392#SG
43.134.189.122:34237#SG
91.200.242.204:19090#JP
103.76.128.220:10000#JP
176.119.149.243:3000#JP
176.119.149.242:3000#JP
176.119.149.241:3000#JP
43.153.181.217:443#JP
45.251.240.213:34237#JP
38.47.121.146:31008#JP
210.149.87.139:9527#JP
150.66.24.104:34237#JP
211.75.243.91:16764#TW
103.123.133.244:18846#TW
61.220.65.189:26832#TW
61.220.65.189:27114#TW
123.241.137.138:12071#TW
59.124.90.154:32495#TW
152.70.245.66:12693#KR
146.56.146.7:21713#KR
129.154.223.89:15800#KR
140.238.8.194:15800#KR
193.123.232.127:31137#KR
146.56.37.60:20018#KR
140.238.7.57:9999#KR
146.56.144.32:11202#KR
146.56.37.60:20017#KR
175.125.207.253:36167#KR
99.83.209.185:443#US
65.75.194.96:23190#US
174.136.206.70:39880#US
64.64.250.72:697#US
67.230.166.61:443#US
98.142.143.20:3009#US
75.2.32.4:443#US
154.21.89.12:12446#US
65.75.195.188:50795#US
174.136.206.95:57757#US
146.59.34.218:2053#PL
    """  # 重复的IP

# 用于存储结果的有序字典
results = OrderedDict()
invalid_ips = []

# 处理输入数据
for line in input_data.split('\n'):
    line = line.strip()
    if line:
        ip, full_ip = extract_ip_and_port(line)
        if ip and validate_ip(ip):
            if full_ip not in results:
                country_code = get_location(ip)
                results[full_ip] = country_code
        else:
            if line not in invalid_ips:
                invalid_ips.append(line)

# 打印结果
print("IP Geolocation Results:")
for full_ip, country_code in results.items():
    print(f"{full_ip}#{country_code}")

if invalid_ips:
    print("\nInvalid IPs:")
    for ip in invalid_ips:
        print(f"Invalid IP: {ip}")

# 打印统计信息
print("\nStatistics:")
print(f"Total unique valid IPs: {len(results)}")
print(f"Invalid IPs: {len(invalid_ips)}")