#!/usr/bin/python3

import bs4


def scrape_links():
    yt_html_file = open('/home/sam/Downloads/ElectronJSBackupPage.html')
    soup = bs4.BeautifulSoup(yt_html_file, 'html.parser')
    links_list = []
    # TODO: Figure out how to further delimit to JUST playlist videos as its grabbing
    # the sidebar videos
    for link in soup.select('a[href^="/watch"]'):
        if link.text:
            links_list.append(link['href'])
           

    return links_list


def write_to_bash_script(links_list):
    with open('/home/sam/Downloads/ytd_download.sh', 'w') as f:
        f.write('#!/bin/bash')
        f.write('\n')
        for link in links_list:
            f.write("youtube-dl -o '~/Downloads/%(title)s-%(id)s.%(ext)s'" + ' https://www.youtube.com' + str(link))
            f.write('\n')
        f.close()


def main():
    links_list = scrape_links()
    write_to_bash_script(links_list)


if __name__ == "__main__":
    main()
