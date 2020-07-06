import os
import sys
import shutil

def Resstart():

    if(os.path.exists("/run/restart-required")):
        return True

    return False

def Disk_check(disk,min_gb,min_percent):
    du = shutil.disk_usage(disk)
    percent_free = 100 * du.free / du.total
    gb_free= du.free / 2**30
    if(gb_free>min_gb or percent_free< min_percent):
        return True
    return False


def root_check_disk():
    Disk_check('/' ,0,100)


def main():

    if(root_check_disk()):
        print("root partition full.")
        sys.exit(1)
    print("All good!")
    
    if(Resstart()):
        print("Restart is required.")
        sys.exit(1)

    print("Restart is not required.")

    sys.exit(0)

main()
