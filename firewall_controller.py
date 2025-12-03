from core import SystemCommand


class FirewallController:
    def __init__(self):
        self.cmd = SystemCommand


    def block_program(self, program_path: str, rule_name: str):
        command = (f'netsh advfirewall firewall add rule '
                   f'name="{rule_name}" dir=out program="{program_path}"'
                   f' action=block enable=yes')
        return self.cmd.run(command)


    def delete_rule(self, rule_name: str):
        command = f'netsh advfirewall firewall delete rule name="{rule_name}"'
        return self.cmd.run(command)


    def list_rules(self):
        return self.cmd.run("netsh advfirewall firewall show rule name=all")