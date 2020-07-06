import os
import sys
import shutil

def Restart():

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
    Disk_check('/' ,2,10)


def main():

    checks=[
        (Restart(),"Restart required"),
        (root_check_disk(),"root partition full")
        ]

    okay=True

    for check,statement in checks:
        if(check):
            print(statement)
            okay =False

    if not okay:
        sys.exit(1)

    print("Everything is okay!")
    sys.exit(0)


main()
