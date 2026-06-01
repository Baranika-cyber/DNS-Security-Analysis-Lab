import pandas as pd
from collections import Counter
import re

# Read Wireshark CSV
data = pd.read_csv("logs.csv")

# Extract domains from Info column
domains = []

for info in data["Info"]:
    match = re.search(r'(?:A|AAAA)\s+([a-zA-Z0-9.-]+\.[a-zA-Z]{2,})', str(info))
    if match:
        domains.append(match.group(1))

# Count domains
domain_counts = Counter(domains)

print("=== Top DNS Queries ===")
for domain, count in domain_counts.most_common(10):
    print(f"{domain} -> {count} requests")