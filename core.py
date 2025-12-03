import subprocess


class SystemCommand:
    @staticmethod
    def run(cmd: str):
        try:
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
            return result.stdout if result.returncode == 0 else result.stderr
        except Exception as e:
            return str(e)