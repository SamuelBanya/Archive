import bs4
import requests
import pendulum

def getCurrentNashvilleTime():
    current_date_central = pendulum.now('America/Chicago').format('dddd, MMMM D, YYYY')

    current_time_central = pendulum.now('America/Chicago').format('hh:mm:ss A')

    return current_date_central, current_time_central


def scrapeDuckDuckGo():
    r = requests.get('https://weather.com/weather/today/l/Nashville+TN?canonicalCityId=d2e9d5e23261bad08730344442ecada76f5e96e85bdebe15cb4658490e1b09f0')
    soup = bs4.BeautifulSoup(r.text, 'html.parser')

    return soup


def displayWeather(soup, current_date_central, current_time_central):
    weather_div_tag = soup.find('div', class_='today_nowcard-temp')
    # print('\n\nLength of children of weatherDivTag: ' + str(len(list(weatherDivTag.children))))
    # print('\n\nPrinting children of weatherDivTag: ')
    for child in weather_div_tag.children:
        # print('\n\nCurrent child: ')
        # print(child)
        # print('\n\nchild.string: ' + str(child.string))
        # print('\n\nAttribute list: ' + str(child.attrs))
        # print('\n\nchild.get_text(): ' + str(child.get_text()))
        weather_span = child.get_text()
    print('Current Weather in Nashville, TN: ' + weather_span + 'F')
    print('Current Date in Nashville, TN: ' + str(current_date_central))
    print('Current Time in Nashville, TN: ' + str(current_time_central))

    content = ''

    content += '<link rel="stylesheet" href="css/output.css" type="text/css"/>'

    content += '<meta charset="utf-8"/>'

    content += '<h1 id="program_header">Nashville Weather Webscraper</h1>'

    content += '\n'

    content += '<h2 id="updated_header">Last Time Updated: ' + str(current_date_central) + ' at ' + str(current_time_central) + ' CST</h2>'

    content += '\n'

    # Remove weird 'Â' character:
    weather_span = str(weather_span).replace('Â', '')

    # Remove last character as a final attempt to remove the 'Â' character present:
    weather_span = str(weather_span)[:-1]

    # Adding u'\N{DEGREE SIGN}' to get rid of the unicode stupidness going on
    # This is why Unicode sucks but can be dealt with swiftly
    degreeChar = u'\N{DEGREE SIGN}'
    content += '<h3 id="weather_header">Current Weather in Nashville, TN: ' + str(weather_span) + degreeChar  + 'F</h3>'

    return content

def writeContentToFile(content):

    with open('/var/www/musimatic/pythonprojectwebsites/NashvilleWeatherWebscraper/output.html', 'w') as f:
        f.write(content)

    f.close()

    return content


def main():
    current_date_central, current_time_central = getCurrentNashvilleTime()
    soup = scrapeDuckDuckGo()
    content = displayWeather(soup, current_date_central, current_time_central)
    writeContentToFile(content)

if __name__ == "__main__":
    main()
