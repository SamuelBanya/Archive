# subscriptionlist.py - This is a Python 3 script that aims to obtain the
# YouTube user's Subscription list because they've sadly removed the ability
# to obtain a user's Subscriptions through RSS feeds on YouTube.

# This project aims to alleviate that in that a user should be able to
# view their YouTube content on their own terms using other utilities like
# youtube-dl

from selenium import webdriver
import getpass

def promptCreds():
    print('\nWelcome To YouTube Subscription List Generator!')
    print('MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM')
    print('MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM')
    print('MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM')
    print('MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM')
    print('MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM')
    print('MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM')
    print('MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM')
    print('MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM')
    print('MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM')
    print('MMMMMMMMMMMMWWXK0OOOkkkkxxxxxxxxxxxddddddddxxxxxxxxxkkkkkkOO0KNWWMMWWMMMMMM')
    print('MMMMMMMMMWWNOoc:;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;,;;;;;;;;;;;:ld0NWMMMMMMMM')
    print('MMMMMMMMMMXd;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;:xNMMMMMMMM')
    print('MMMMMMMMMNx;;;;;;;;;;;;;;;;;;;;;;;;;;,;;;;;;;;;;;;;;;;;;;;;;;;;;;:kWMMMMMMM')
    print('MMMMMMMMW0c,;;;;;;;;;;;;;;;;;;;;;;;;;,;;;;;;;;;;;;;;;;;;;;;;;;;;;,lKWMMMMMM')
    print('MMMMMMMMWk;,;;;;;;;;;;;;;;;;;;;;;;;,,;;;;;;;;;;;;;;;;;;;;;;;;;;;;,:OWMMMMMM')
    print('MMMMMMMMNd;,,;;,;;;;;;;;;,,;;;,:ddc;,,,;,;;;;;;,;;;,;;;;;,,,;;;;;,;xWMMMMMM')
    print('MMMMMMMMXo,,,,,,,,,,,,,,;,,,,,,cKWX0kdoc;,,,;,,,,,,,,,,,,,,,,,,,;,;dNMMMMMM')
    print('MMMMMMMMXo,,,,,,,,,,,,,,,,,,,;,cKWWMMWWX0xoc;,,,,,,,,,,,,,,,,,,,,,,dNMMMMMM')
    print('MMMMMMMWXl,,,,,,,,,,,,,,,,,,,;,cKWMMMMMMMWNKOxl:;,,,,,,,,,,,,,,,,,,oXMMMMMM')
    print('MMMMMMMMKl,;,;,,,,,,,,,,,,,,,;,cKWMMMMMMMMMWNXko:,,,,,,,,,,,,,,,,,,oXMMMMMM')
    print('MMMMMMMMKl,,,,,,,,,,,,,,,,,,,,,cKWMMMMMMWNKkoc;,,,,,,,,,,,,,,,,,,,,oXMMMMMM')
    print('MMMMMMMMXl,,,,,,,,,,,,,,,,,,,,,c0WWWNXKkdc;,,,,,,,,,,,,,,,,,,,,,,,,oNMMMMMM')
    print("MMMMMMMMXo,,,,,,,,,,,,,,,,,,,,'cOKkdl:;,,,,,,,,,,,,,,,,,,,,,,,,,,,,dNMMMMMM")
    print("MMMMMMMMNd,,,,,,,,,,,,,,,,,,,,,;c:,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,xWMMMMMM")
    print("MMMMMMMMWx,'',,''''''''''',,',,',,,'',,,,,''''',''''''''''''',,,,';kWMMMMMM")
    print("MMMMMMMMWO;''''''''''''''''''''''''''''''''''''''''''''''''''''''':0WMMMMMM")
    print("MMMMMMMMWXo'''''''''''''''''''''''''''''''''''''''''''''''''''''''dNMMMMMMM")
    print("MMMMMMMMMWKl'''''''''''''''''''''''''''''''''''''''''''''''''''''oXMMMMMMMM")
    print("MMMMMMMMMMMXkc,''....''''''''''''''''''''''''''''''''.....'.'',ckNMMMMMMMMM")
    print('MMMMMMMMMMMMMNKOxxddddooooollllllllllllllllllllllloooooodddxkOKNWMMMMMMMMMM')
    print('MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWWWWWWWWWWWWWWWWWMMMMMMMMMMMMMMMMMMMMMMMMMMM')
    print('MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM')
    print('MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM')
    print('MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM')
    print('MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM')
    print('MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM')
    print('MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM')
    print('MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM')
    print('+++++++++++++++++++++++++++++++++++++++++++++++++++')
    print('\'Y\' or \'N\': Did you already specify a Selenium Gecko Driver path in your seleniumDriverPath.txt file?: ')
    config_answer = str(input('Config txt file was used: ')).upper()
    print('+++++++++++++++++++++++++++++++++++++++++++++++++++')    
    if config_answer == 'Y':
        # TODO: Look into the user's specified "seleniumDriverPath.txt" file in the
        # same directory and rip the second line of the file:
        print('+++++++++++++++++++++++++++++++++++++++++++++++++++')        
        print('Looking in seleniumDriverPath.txt file within current program directory')
        selenium_driver_path = '/home/sam/utilities/SeleniumGeckoDriver'
        print('+++++++++++++++++++++++++++++++++++++++++++++++++++')        
    elif config_answer == 'N':
        print('+++++++++++++++++++++++++++++++++++++++++++++++++++')        
        print('Please enter the path for your Selenium Firefox Driver: ')
        # Location for latest Selenium Gecko Driver:
        # https://github.com/mozilla/geckodriver/releases
        selenium_driver_path = str(input('\nSelenium Firefox Driver Path:'))
    print('---------------------------------------------------')
    print('+++++++++++++++++++++++++++++++++++++++++++++++++++')
    print('Please enter your YouTube password information:')
    print('+++++++++++++++++++++++++++++++++++++++++++++++++++')
    password = str(getpass.getpass('\nPassword: '))    
    
    return selenium_driver_path, password


def visitYouTubePage(selenium_driver_path, password):
    browser = webdriver.Firefox(executable_path=selenium_driver_path)
    # TODO: Grab the YouTube login page, and authenticate for the
    # user
    browser.get('https://accounts.google.com/ServiceLogin/signinchooser?continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Den%26next%3Dhttps%253A%252F%252Fwww.youtube.com%252F&hl=en&service=youtube&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
    profile_identifier_button = browser.find_element_by_id('profileIdentifier')
    profile_identifier_button.click()
    print('profile_identifier_button clicked')
    browser.implicitly_wait(3)
    password_element = browser.find_element_by_css_selector("input[type='password']")
    password_element.send_keys(password)
    print('password_element filled in with password')
    next_button = browser.find_element_by_id('passwordNext')
    next_button.click()
    print('next_button clicked')
    # TODO: Visit the user's YouTube subscription page
    # FOR GENERAL LIST OF SUBSCRIPTIONS AKA YOUTUBE CHANNELS:
    # Utilize the already present XML that YouTube is hiding behind
    # the scenes:
    # https://www.youtube.com/feeds/videos.xml?channel_id=UC2eYFnH61tmytImy1mTYvhA
    # TODO: All you have to do is rip the "channel_id" values from the individual
    # links on the "Subscription" sidebar, and add this to a skeleton link:
    # Skeleton Link: "https://www.youtube.com/feeds/videos.xml?channel_id=" + channel_id
    # TODO: Rip the Channel links from the "SUBSCRIPTIONS" left hand side bar
    # TODO: Give the user the option to parse the HTML page that they saved from YouTube
    # by hitting Ctrl+U in Firefox, and parse it with BeautifulSoup4 
    # TODO: Parse the HTML page for the specific request data variable that contains all of the
    # YouTube channel subscriber links:
    # var = ytInitialGuideData
    # TODO: NOTE: This site version ACTUALLY has the export button present:
    # https://www.youtube.com/subscription_manager/sort_alphabetical?next=UCoUqzYqTYp9SE9RTkUYusZA&cur=1&p=2
    # This means they deliberately regressed this feature but its still available thankfully.
    # The 'href' for the "Export subscriptions" button action is:
    # href:"/subscription_manager?action_takeout=1"
    # TODO: Store this information into a dictionary of values of the YouTube
    # channel name as well as the subscription link
    # FOR INDIVIDUAL VIDEOS FROM "TODAY" SECTION:
    # TODO: Grab any HTML element with the "video-title" ID
    # under the "Today" tag
    # TODO: Place these elements into a list
    return


def main():
    selenium_driver_path, password = promptCreds()
    visitYouTubePage(selenium_driver_path, password)

    
if __name__ == '__main__':
    main()
