from subprocess import Popen, PIPE

def main():
    cmd = 'python3 -m venv venv && source venv/bin/activate && python3 ./ext4scanner/main.py && deactivate && rm -r venv'
    # cmd = 'python3 ./ext4scanner/main.py'
    # cmd = 'ls -l'
    Popen(cmd, shell=True)


if __name__ == "__main__":
        main()
