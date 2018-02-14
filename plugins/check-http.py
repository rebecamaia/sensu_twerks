import requests
import sys

def get_status_code(url):

    try:
        req = requests.get(url,timeout=10)
    except requests.exceptions.Timeout:
        print "WARNING: Time Out!"
        sys.exit(1)
    return req.status_code

def main():
   url = sys.argv[1]

   if get_status_code(url) == 200:
        print "OK: URL for %s is accessible!" % (str(url))
        sys.exit(0)
   elif (get_status_code(url) == 404):
        print "CRITICAL: URL for %s is not accessible!" % (str(url))
        sys.exit(2)
   else:
        print "UNKNOWN: status code for requests: %d" % (get_status_code(url))
        sys.exit(3)

if __name__ == "__main__":
   main()
