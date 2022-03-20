#!usr/bin/python3
# paletteScraper.py: This is a Selenium based webscraper that visits the
# following website, "https://paletton.com", and clicks the random

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import pendulum
import os
import os.path
import logging

serverLogFile = '/programmingprojects/PaletteOfTheDayWebscraper/PaletteScraperLog.txt'

# Remove the previous run's log on each run
if os.path.isfile(serverLogFile):
    os.remove(serverLogFile)

logging.basicConfig(filename='/programmingprojects/PaletteOfTheDayWebscraper/PaletteScraperLog.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s -%(message)s')


def visit_page_with_selenium():
    palette_list = []
    options = Options()
    options.headless = True
    browser = webdriver.Firefox(options=options, executable_path='/utilities/geckodriver')
    browser.get('https://paletton.com')

    # Reference I used to figure out how to deal with iFrames
    # with Selenium:
    # https://www.techbeamers.com/switch-between-iframes-selenium-python/

    randomize_button = browser.find_element_by_css_selector('.randomize > a:nth-child(1) > span:nth-child(1)')

    randomize_button.click()

    unlike_button = browser.find_element_by_css_selector('.control-random > button:nth-child(2)')

    unlike_button.click()
    
    iFrame = browser.find_element_by_css_selector('iframe.pane')

    # Now that we have found the iFrame, let's switch to it using
    # the .switch_to.frame() method:
    browser.switch_to.frame(iFrame)
    
    # Obtain 'col-data' attribute:
    first_color = browser.find_element_by_css_selector('div.preview-box:nth-child(1)').get_attribute('col-data')
    second_color = browser.find_element_by_css_selector('div.preview-box:nth-child(2)').get_attribute('col-data')
    third_color = browser.find_element_by_css_selector('div.preview-box:nth-child(3)').get_attribute('col-data')
    fourth_color = browser.find_element_by_css_selector('div.preview-box:nth-child(4)').get_attribute('col-data')
    if first_color == second_color and first_color == third_color and first_color == fourth_color:
        first_color = browser.find_element_by_css_selector('.bgcol-pri-4').get_attribute('col-data')
        second_color = browser.find_element_by_css_selector('.bgcol-pri-3').get_attribute('col-data')
        third_color = browser.find_element_by_css_selector('.bgcol-pri-2').get_attribute('col-data')
        fourth_color = browser.find_element_by_css_selector('.bgcol-pri-1').get_attribute('col-data')
    palette_list.append(first_color)
    palette_list.append(second_color)
    palette_list.append(third_color)
    palette_list.append(fourth_color)
    
    browser.close()
    
    return palette_list


def create_content(palette_list):
    current_date_central = pendulum.now('America/Chicago').format('dddd, MMMM D, YYYY')

    current_time_central = pendulum.now('America/Chicago').format('hh:mm:ss A')
    
    content = ''

    content += '<link rel="stylesheet" href="css/output.css" type="text/css"/>'

    content += '<h1 id="program_header">Palette Of The Day Webscraper</h1>'

    content += '\n'

    content += '<h2 id="updated_header">Last Time Updated: ' + str(current_date_central) + ' at ' + str(current_time_central) + ' CST</h2>'

    content += '\n'

    # TODO: Figure out how to get the div's in color

    content += '<h2>1. </h2>'

    # Based on this:
    # https://www.dotconferences.com/2018/11/david-desandro-read-color-hex-codes

    first_num = int(str(palette_list[0])[0])

    second_num = int(str(palette_list[0])[2])
    
    sum_two_nums = int(first_num + second_num)

    if sum_two_nums < 9:
        text_color = "white"
    else:
        text_color = "black"

    logging.debug('\n\nfirst_num: ' + str(first_num))

    logging.debug('\nsecond_num: ' + str(second_num))

    logging.debug('\nsum_two_nums: ' + str(sum_two_nums))
    
    logging.debug('\ntext_color: ' + str(text_color))
    
    content += '<div style="background-color:#' + palette_list[0] + '; color:' + text_color + '">Color 1: #' + palette_list[0] + '</div>'

    content += '<h2>2. </h2>'

    first_num = int(str(palette_list[1])[0])

    second_num = int(str(palette_list[1])[2])
    
    sum_two_nums = int(first_num + second_num)

    if sum_two_nums < 9:
        text_color = "white"
    else:
        text_color = "black"

    logging.debug('\n\nfirst_num: ' + str(first_num))

    logging.debug('\nsecond_num: ' + str(second_num))

    logging.debug('\nsum_two_nums: ' + str(sum_two_nums))
        
    logging.debug('\ntext_color: ' + str(text_color))    

    content += '<div style="background-color:#' + palette_list[1] + '; color:' + text_color + '">Color 2: #' + palette_list[1] + '</div>'

    content += '<h2>3. </h2>'

    first_num = int(str(palette_list[2])[0])

    second_num = int(str(palette_list[2])[2])
    
    sum_two_nums = int(first_num + second_num)
    
    if sum_two_nums < 9:
        text_color = "white"
    else:
        text_color = "black"        

    logging.debug('\n\nfirst_num: ' + str(first_num))

    logging.debug('\nsecond_num: ' + str(second_num))

    logging.debug('\nsum_two_nums: ' + str(sum_two_nums))
        
    logging.debug('\ntext_color: ' + str(text_color))    

    content += '<div style="background-color:#' + palette_list[2] + '; color:' + text_color + '">Color 3: #' + palette_list[2] + '</div>'

    content += '<h2>4. </h2>'

    first_num = int(str(palette_list[3])[0])

    second_num = int(str(palette_list[3])[2])
    
    sum_two_nums = int(first_num + second_num)

    if sum_two_nums < 9:
        text_color = "white"
    else:
        text_color = "black"        

    logging.debug('\n\nfirst_num: ' + str(first_num))

    logging.debug('\nsecond_num: ' + str(second_num))

    logging.debug('\nsum_two_nums: ' + str(sum_two_nums))
    
    logging.debug('\ntext_color: ' + str(text_color))

    content += '<div style="background-color:#' + palette_list[3] + '; color:' + text_color +'">Color 4: #' + palette_list[3] + '</div>'    
    
    return content


def writeContentToFile(content):
    with open('/home/sam/public_html/pythonprojectwebsites/PaletteOfTheDayWebscraper/output.html', 'w') as f:
        f.write(content)

    f.close()

    return content


def main():
    palette_list = visit_page_with_selenium()
    content = create_content(palette_list)
    writeContentToFile(content)

    
if __name__ == "__main__":
    main()
