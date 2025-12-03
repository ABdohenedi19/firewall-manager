from firewall_controller import FirewallController
from Logger import FirewallLogger
from Monitor import LoggerMonitor

fw = FirewallController()
logger = FirewallLogger()

class App:
    @staticmethod
    def menu():
        print("=== Simple Python Firewall ===")
        print("1 - Block Program")
        print("2 - Delete Rule")
        print("3 - List Rules")
        print("4 - Enable Firewall Logging")
        print("5 - Monitor Log (Realtime)")
        print("6 - Exit")
        print("==============================")
        print()

    def run(self):
        while True:
            self.menu()
            choice = input("Choose option: ")

            if choice == "1":
                path = input("Enter program path: ")
                name = input("Enter rule name: ")
                print(fw.block_program(path, name))

            elif choice == "2":
                name = input("Enter rule name: ")
                print(fw.delete_rule(name))

            elif choice == "3":
                print(fw.list_rules())

            elif choice == "4":
                log_path = input("Enter log file path (Press Enter for default): ") or logger.log_path
                logger.log_path = log_path
                print(logger.enable_logging())

            elif choice == "5":
                log_path = input("Enter log file path (Press Enter for default): ") or logger.log_path
                monitor = LoggerMonitor(log_path)
                monitor.start()

            elif choice == "6":
                print("Exiting...")
                break

            else:
                print("Invalid choice.")

if __name__ == "__main__":
    App().run()
