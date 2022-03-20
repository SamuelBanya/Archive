#! /usr/bin/python3
import scrapy

# Notes From IRC:
# 13:58:52    mgedmin | put your requirements.txt (and a README) in a git repo, clone it on the vps in /opt/myproject, create a  │ aaearon
#                     | venv in /opt/myproject/venv, /opt/myproject/venv/bin/pip install -r /opt/myproject/requirements.txt, set │ Aaron
#                     | up systemd units or whatever, have fun                                                                   │ aball
# 13:58:58    mgedmin | maybe create an ansible playbook to do it all for you                                                    │ abirkill

class FinanceSpider(scrapy.Spider):
    name = 'finance_spider'
    start_urls = ['https://blog.scrapinghub.com']
    # start_urls = ['https://finance.yahoo.com/trending-tickers']

    def parse(self, response):
        # 'yfinlist-table': This is the class of the finance table present
        for row in response.css('tr'):
            yield {'row': row.css('tr ::text').get()}

        # This section is to cycle through each page
        for next_page in response.css('a.next-posts-link'):
            yield response.follow(next_page, self.parse)

EOF
