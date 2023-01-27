# website-monitoring-script

This script is used to monitor the availability and response time of a website. It checks the website's status by sending a GET request and measures the response time. If the response time is above a certain threshold or if the website is down, the script sends an alert. The script also logs the website's status, response time, and timestamp in a JSON file.

## Usage

1. Clone the repository to your local machine.
2. Install the required dependencies by running `pip install -r requirements.txt`
3. Create an instance of the `WebsiteMonitor` class, passing in the URL of the website to be monitored and the threshold value for response time.
4. Call the `run()` method on the instance to start monitoring the website.
5. Schedule the script to run at regular intervals using a cron job.

Example:
```python
monitor = WebsiteMonitor("https://www.google.com", threshold=2)
monitor.run()

