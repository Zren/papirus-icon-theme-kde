#!/usr/bin/python3

from bs4 import BeautifulSoup
import sys

def insertStylesheet(soup):
	if not soup.svg.defs:
		defs = soup.new_tag('defs')
		soup.svg.insert(0, defs)
	
	if not soup.svg.style:
		style = soup.new_tag('style')
		style['id'] = 'current-color-scheme'
		style['type'] = 'text/css'
		style.string = '.ColorScheme-Text { color:#555555; }'
		soup.svg.defs.insert(0, style)

def convertIconSvgString(xml):
	soup = BeautifulSoup(xml, 'html.parser')
	#print(soup.svg.defs)

	modified = False
	paths = soup.find_all('path')
	for path in paths:
		# print(path['style'])
		if 'style' not in path and len(paths) == 1:
			path['style'] = 'fill:currentColor' # ;fill-opacity:1;stroke:none
		elif 'style' in path and 'fill:#555555' in path['style']:
			path['style'] = path['style'].replace('fill:#555555', 'fill:currentColor')
		else:
			continue

		del path['opacity']
		path['class'] = 'ColorScheme-Text'
		modified = True
	
	if soup.svg.style and 'type' not in soup.svg.style:
		soup.svg.style['type'] = 'text/css'
		modified = True

	if modified:
		insertStylesheet(soup)
		return soup.prettify(formatter="xml")
	else:
		return xml


def convertIconSvg(filename):
	with open(filename) as f:
		xml = f.read()

	xml2 = convertIconSvgString(xml)

	if xml != xml2:
		with open(filename, 'w') as f:
			f.write(xml2)

if __name__ == '__main__':
	print(sys.argv)
	convertIconSvg(sys.argv[1])
