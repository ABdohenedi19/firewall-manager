from core import SystemCommand


class FirewallLogger:
    def __init__(self, log_path=r"C:\Firewall Manager project\firewall_log.txt"):
        self.log_path = log_path


    def enable_logging(self):
        cmd1 = "netsh advfirewall set allprofile logging droppedconnections enable"
        cmd2 = f'netsh advfirewall set allprofile logging filename="{self.log_path}"'
        return SystemCommand.run(cmd1) + SystemCommand.run(cmd2)