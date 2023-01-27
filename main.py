import requests
import json
from datetime import datetime

class WebsiteMonitor:
    def __init__(self, url, threshold):
        self.url = url
        self.threshold = threshold

    def check_website(self):
        try:
            response = requests.get(self.url, timeout=5)
            response.raise_for_status()
            response_time = response.elapsed.total_seconds()
            status = "up"
        except requests.exceptions.HTTPError as err:
            status = "down"
            response_time = None
        except requests.exceptions.RequestException as e:
            status = "down"
            response_time = None
        data = {
            "url": self.url,
            "status": status,
            "response_time": response_time,
            "timestamp": str(datetime.now())
        }
        return data

    def write_to_file(self, data, filename):
        with open(filename, "a") as f:
            json.dump(data, f)
            f.write("\n")
            
    def send_alert(self, data):
        if data["response_time"] and data["response_time"] > self.threshold:
            print(f"ALERT: Response time is above threshold. Website: {data['url']}, Response Time: {data['response_time']}")
        if data["status"] == "down":
            print(f"ALERT: Website is down. Website: {data['url']}")

    def run(self):
        data = self.check_website()
        self.write_to_file(data, "website_status.json")
        self.send_alert(data)
        print(data)

monitor = WebsiteMonitor("https://www.google.com", threshold=2)
monitor.run()
