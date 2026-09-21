import csv
import os
from collections import Counter


def analyze_traffic(csv_path="sample_traffic.csv"):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    full_csv_path = os.path.join(base_dir, csv_path)

    print(f"\n--- Analyzing Network Traffic from: {csv_path} ---")

    if not os.path.exists(full_csv_path):
        print(f"[!] File not found: {full_csv_path}")
        return None

    ip_bytes = Counter()
    try:
        with open(full_csv_path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if "src_ip" in row and "bytes" in row:
                    ip_bytes[row["src_ip"]] += int(row["bytes"])

        if not ip_bytes:
            print("[!] No traffic data found in CSV.")
            return None

        top_talker, total = ip_bytes.most_common(1)[0]
        print(f"[+] Top talker IP: {top_talker} ({total} bytes)")
        return top_talker, total

    except Exception as e:
        print(f"[!] Error analyzing traffic file: {e}")
        return None