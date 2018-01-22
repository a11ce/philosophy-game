import wikipedia
import sys
import re

def a(test_str):
    ret = ''
    skip1c = 0
    skip2c = 0
    for i in test_str:
        if i == '[':
            skip1c += 1
        elif i == '(':
            skip2c += 1
        elif i == ']' and skip1c > 0:
            skip1c -= 1
        elif i == ')'and skip2c > 0:
            skip2c -= 1
        elif skip1c == 0 and skip2c == 0:
            ret += i
    return ret


curArt = wikipedia.page(sys.argv[1])
while True:
	print(curArt.title)
	fullText = curArt.html()

	splitText = fullText.splitlines()
	linkLine = ""
	for line in splitText:
		#print(line)
		if "<b>" in line and not "<table" in line:
			linkLine = line
			break
	linkLine = a(linkLine)
	#print(linkLine)
	nextPage = (linkLine.split("<a href=\"/wiki/"))[1].split("\"")[0]

	nextPage = nextPage.replace("_", " ")
	curArt = wikipedia.page(nextPage)
