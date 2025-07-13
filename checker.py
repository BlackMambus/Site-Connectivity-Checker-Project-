import requests
import time

def check_site_connectivity(url):
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url  # Default to HTTP if no scheme is provided

    print(f"🔍 Checking connectivity to: {url}")
    try:
        start_time = time.time()
        response = requests.get(url, timeout=10)
        end_time = time.time()

        print(f"✅ Site is reachable!")
        print(f"📶 Status Code: {response.status_code}")
        print(f"⏱️ Response Time: {round(end_time - start_time, 2)} seconds")
    except requests.exceptions.RequestException as e:
        print(f"❌ Site is not reachable. Error: {e}")

def main():
    while True:
        url = input("\nEnter a website URL (or type 'exit' to quit): ")
        if url.lower() == 'exit':
            print("👋 Exiting Site Connectivity Checker.")
            break
        check_site_connectivity(url)

if __name__ == "__main__":
    main()
