# Mozilla Firefox Bookmark Parser

This project allows you to easily parse the existing exported "bookmarks.html" file from Firefox's Bookmarks menu so that you can easily just add your existing bookmarks to a .txt file so that you can refer to them within another web browser.

This allows you to easily transfer any links between browsers without having to depend upon Mozilla, and allows you freedom to choose whatever browser you want.

## Installation Instructions:

Git clone the repository with:
git clone https://github.com/SBanya/MozillaFirefoxBookmarkParser.git

Other Python 3 based dependencies:

Please install the BeautifulSoup 4 library with pip3:
pip3 install bs4

### Usage Instructions:

Open your Mozilla Firefox browser, and click the Bookmarks menu > Show All Bookmarks.

Then, click "Import and Backup" > "Export Bookmarks to HTML...".

This will take all of your bookmarks in Mozilla Firefox and export them all into a webpage called "bookmarks.html".

Place your exported "bookmarks.html" file into this same project directory.

The Python 3 based "MozillaFirefoxBookmarkParser.py" script will parse the HTML tags present in the "bookmarks.html" file will parse any <h3> tags present to place them in a corresponding "folders.txt" file in the same directory, and will parse any <a> anchor tags and place them in a corresponding "links.txt" file in the same directory.

Use the following command:
python3 MozillaFirefoxBookmarkParser.py

The resulting "folders.txt" will now be present in the same directory, which contains the list of folders from your bookmarks.

The resulting "links.txt" file will be now present in the same directory so that you can easily refer to it within other browsers (Qutebrowser) or other utilities like DMenu.

Enjoy, and thanks for checking out my utility :)