import os
from analytics import analyze_traffic
from network import fetch_uuid, quick_check


def display_menu():
    print("\n==========================================")
    print(" 🚀 Python Security Utility Tool ")
    print("==========================================")
    print("1. Fetch Random UUID from API")
    print("2. Analyze Traffic Data (from sample_traffic.csv)")
    print("3. Check Artifact Integrity (SHA256) & Port Status")
    print("4. Exit")
    print("==========================================")


def main():
    sample_file = os.path.join("Data", "sample_file.txt")
    traffic_file = os.path.join("Data", "sample_traffic.csv")

    while True:
        display_menu()
        choice = input("Select an option (1-4): ").strip()

        if choice == "1":
            fetch_uuid()
        elif choice == "2":
            analyze_traffic(traffic_file)
        elif choice == "3":
            host = input("Enter target host (default: 127.0.0.1): ").strip() or "127.0.0.1"
            port = input("Enter target port (default: 22): ").strip() or "22"
            quick_check(sample_file, host, port)
        elif choice == "4":
            print("\n[+] Exiting application. Goodbye!")
            break
        else:
            print("\n[!] Invalid selection. Please choose numbers between 1 and 4.")
            
if __name__ == "__main__":
    main()