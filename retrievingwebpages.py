import urllib.request, urllib.parse, urllib.error
fhand = urllib.request.urlopen("http://data.pr4e.org/romeo.txt")  # whatever site you want type in here
for line in fhand:
    print(line.decode().strip())