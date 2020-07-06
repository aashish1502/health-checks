import os
import sys

def Resstart():

    if(os.path.exists("/run/restart-required")):
        return True

    return False

def main():

    if(Resstart()):
        print("Restart is required.")
        sys.exit(1)

    print("Restart is not required.")

    sys.exit(0)

main()
