import os.path
import sys

def get_rx(statistics_path):

    try:
        rx = open(statistics_path, "r")
        result = rx.read()
    except OSError:
        print "Permission Denied!"
        sys.exit(1)
    return result

def main():
   statistics_path = sys.argv[1]

   if int(get_rx(statistics_path)) > 0:
        print "OK: There's traffic in the in interface! Current: %i" % (int(get_rx(statistics_path)))
        sys.exit(0)
   elif (int(get_rx(statistics_path)) == 0):
        print "CRITICAL: No traffic identified for the interface!"
        sys.exit(2)
   else:
        print "UNKNOWN"
        sys.exit(3)

if __name__ == "__main__":
   main()
