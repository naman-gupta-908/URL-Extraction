from urllib.request import urlopen
page=urlopen(input("Enter the website for its source code: "))

sourcecode=page.read()
print(sourcecode)