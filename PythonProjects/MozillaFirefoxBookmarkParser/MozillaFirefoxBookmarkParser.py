#!/usr/bin/python3
# MozillaBookmarkParser.py - This project aims to obtain the anchor tags within
# the exported "bookmarks.html" file exported from Firefox to allow a user
# to easily transfer them to another browser like Qutebrowser or other
# utilities like DMenu
import bs4
import os

# Taken from this StackOverflow post:
# https://stackoverflow.com/questions/8112922/beautifulsoup-innerhtml
def innerHTML(element):
    return element.encode_contents()

def parseBookmarks():
    print('Parsing through "boomarks.html" file...')
    bookmarks_file = open("bookmarks.html")
    soup = bs4.BeautifulSoup(bookmarks_file, 'html.parser')
    anchors = soup.find_all('a')
    h3_tags = soup.find_all('h3')
    bookmarks_file.close()

    # Remove existing 'folders.txt' and 'links.txt' file
    # if its present already to create a fresh new file:
    folders_file = 'folders.txt'
    if os.path.isfile(folders_file):
        os.remove(folders_file)
        
    links_file = 'links.txt'
    if os.path.isfile(links_file):
        os.remove(links_file)

    folders_file = open('folders.txt', 'w')

    for h3_tag in h3_tags:
        h3_tag_inner_html = str(innerHTML(h3_tag), 'utf-8')
        folders_file.write(h3_tag_inner_html)
        folders_file.write('\n')

    folders_file.close()

    links_file = open('links.txt', 'w')

    for anchor in anchors:
        anchor_inner_html = str(innerHTML(anchor), 'utf-8')        
        links_file.write(str(anchor_inner_html + ' ' + anchor.get('href')))
        links_file.write('\n')

    links_file.close()

    print('Parsing complete. Enjoy your "folders.txt" and "links.txt" files! :)')


def main():
    parseBookmarks()

    
if __name__ == "__main__":
    main()
