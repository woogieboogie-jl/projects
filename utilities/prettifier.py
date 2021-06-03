from bs4 import BeautifulSoup as bs
import os


location_dir = input("your desired directory?...")
list_scripts = [dirs for dirs in os.listdir(location_dir) if dirs.endswith(".html") is True]
print(list_scripts)

for script in list_scripts:
    with open (location_dir + "/" + script, 'r', encoding="UTF-8") as input_raw:
        soup = bs(input_raw, 'html.parser')
        html = soup.prettify()
        print(html)
    with open (location_dir + "/" + script.replace(".html", "_prettified.html"), 'w', encoding="UTF-8") as output:
        output.write(html)
