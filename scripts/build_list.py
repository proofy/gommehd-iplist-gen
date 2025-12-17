import requests
import re

TARGET_FILE = "gommehd-ips.txt"

sources = [
    "https://mclist.co/server/gommehd.net",
    "https://crafty.gg/servers/gommehd.net",
    "https://minecraft-statistic.net/en/server/GommeHD.html",
]

ip_regex = re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b")

def fetch(url):
    try:
        print(f"Fetching {url} ...")
        r = requests.get(url, timeout=15)
        return r.text
    except Exception as e:
        print("ERROR:", e)
        return ""

def extract_ips(html):
    return set(re.findall(ip_regex, html))

all_ips = set()

for src in sources:
    html = fetch(src)
    ips = extract_ips(html)
    print(f"Found {len(ips)} IPs from {src}")
    all_ips |= ips

sorted_ips = sorted(all_ips)

with open(TARGET_FILE, "w") as f:
    f.write("# Auto-generated GommeHD IP list\n")
    f.write("# Source: public Minecraft trackers\n")
    for ip in sorted_ips:
        f.write(f"{ip}\n")

print(f"Written {len(sorted_ips)} IPs to {TARGET_FILE}")

