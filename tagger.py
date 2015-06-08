import urllib.request as req
import urllib.parse as par
import sys
import re

from bs4 import BeautifulSoup as bs


url2 = 'https://www.youtube.com/watch?v=tXFAYZXnjSA'

def get_meaningful_text(str):
	return bs(str).getText()

def get_source(url):
	return str(req.urlopen(url).read())

def get_meta(str):
	return re.findall(r'<meta property="og:video:tag" content="(.*?)">', str)

def get_title(str):
	return re.findall(r'<meta name="title" content="(.*?)">', str)

def get_description(str):
	return re.findall(r'<p id="eow-description" >(.*?)</p>', str)

def get_recommended_channels(src, limit):
	related_vid = bs(src).find(id="watch-related")
	#related_vid = bs(str(related_vid)).find("a", class="content-link")
	related_vid = re.findall(r'href="/watch\?v=(.*?)"', str(related_vid))
	print(related_vid)

def main(args):
	page_source = get_source(url2)
	title = get_title(page_source)
	desc = get_description(page_source)
	meta = get_meta(page_source)
	get_recommended_channels(page_source, 5)

	print(meta)
	print(title)
	print(desc)
	print(get_meaningful_text(desc[0]))
	return

if __name__ == '__main__':
	main(sys.argv)

