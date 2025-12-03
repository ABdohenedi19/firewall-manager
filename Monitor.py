import time
import datetime
import os

class LoggerMonitor:
    def __init__(self, log_path=r"C:\Firewall Manager project\firewall_log.txt"):
        self.log_path = log_path
        if not os.path.exists(self.log_path):
            open(self.log_path, "w").close()

    def log(self, message: str):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        full_message = f"[{timestamp}] {message}"
        with open(self.log_path, "a") as f:
            f.write(full_message + "\n")
        print(full_message)

    def start(self):
        self.log(f"[+] Real-time monitoring started on: {self.log_path}")
        print("[Press CTRL + C to stop]")

        try:
            with open(self.log_path, "r") as f:
                f.seek(0, 2)  # Move to end of file
                while True:
                    line = f.readline()
                    if line:
                        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        print(f"[{timestamp}] [MONITOR] {line.strip()}")
                    else:
                        time.sleep(0.5)

        except KeyboardInterrupt:
            self.log("[+] Monitoring stopped.")
        except FileNotFoundError:
            print("[!] Log file not found. Enable logging first.")





