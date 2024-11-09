import requests
import sys

try:
    if sys.argv[1] == "-f" and sys.argv[3] == "-u":
        split = sys.argv[4].split("/")
        if split[-1] == "fuzz":
            text = sys.argv[4]
            file = open(sys.argv[2],'r')
            for i in file:
                new = text[:len(text)-4] + i
                get = requests.get(new)
                print(get.status_code,"   ",i)
        else:
            print("u need to write fuzz correct!!")
        
    else: 
        print("choose the write flag!")

except:
    print('you are not doing good or no host server!!')