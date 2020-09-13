import requests
import sys
import lxml.html

try:
    bug_me_get = requests.get("https://bugmenot.com/view/" + sys.argv[1]).content
except IndexError:
    print("No credz try a different URL")
    quit()

bug_me_parsed = lxml.html.fromstring(bug_me_get)

for creds in bug_me_parsed.xpath("//kbd"):
    print(creds.text_content())

'''
TODO:

-help message
-number of results argument
-print success rate
-auto add to clipboard
-sort by age/success

'''
