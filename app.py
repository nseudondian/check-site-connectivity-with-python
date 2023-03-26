import urllib.request as urllib

print("This app checks the connectivity of your website")

def main(url):
    print("Connecting...")

    response = urllib.urlopen(url)
    print(url, "connected successfully, code", response.getcode())

url = input("Enter url of website to check: ")  

main(url)