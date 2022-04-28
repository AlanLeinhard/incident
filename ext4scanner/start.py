#/bin/sh
from subprocess import Popen, PIPE, call, check_call

# import pip

def main():
    cmd = 'sudo apt install python3-pip && pip install packaging==21.3 pyparsing==3.0.7 PyQt5==5.15.6 PyQt5-Qt5==5.15.2 PyQt5-sip==12.9.1 sip==6.5.1 toml==0.10.2'
    # cmd = 'python3 ./ext4scanner/main.py'
    # cmd = 'ls -l'
    call(cmd, shell=True)
    # check_call("easy_install -r requirements.txt", shell=True)
    # cmd = 'source venv/bin/activate && python3 ./ext4scanner/main.py && deactivate && rm -r venv'
    # Popen(cmd, shell=True)
    # pip.main(['install', '-r', 'requirements.txt'])


if __name__ == "__main__":
        main()
