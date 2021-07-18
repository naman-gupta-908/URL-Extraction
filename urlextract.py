from urllib.request import urlopen

page=urlopen(input("Enter the website for its header info: "))
print(page.headers)