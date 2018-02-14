import os.path
import sys

def get_dir_status(dir_path):

    try:
        result = os.path.isdir(dir_path)
    except OSError:
        print "Permission Denied!"
        sys.exit(1)
    return result

def main():
   dir_path = sys.argv[1]

   if get_dir_status(dir_path) == True:
        print "OK: Directory exists!!"
        sys.exit(0)
   elif (get_dir_status(dir_path) == False):
        print "CRITICAL: Directory is not accessible!"
        sys.exit(2)
   else:
        print "UNKNOWN"
        sys.exit(3)

if __name__ == "__main__":
   main()
