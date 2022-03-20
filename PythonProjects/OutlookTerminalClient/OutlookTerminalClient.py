# IMAP stands for:
# Internet Message Access Protocol (IMAP)

# This uses the following third party modules (providing reference docs):
# pyzmail docs:
# http://magiksys.net/pyzmail/
# imapclient docs:
# https://imapclient.readthedocs.io/en/2.1.0/

import imapclient
import pyzmail
import getpass
import pprint
import imaplib
from datetime import date
import pyzmail


def userLogin():
    # This line is used to increase the size limit to: 10,000,000 bytes when running
    # searches for emails:imaplib._MAXLINE = 10000000
    print('\nWelcome To MS Outlook On The Command Line!')
    print('MMMMMMMMWNXK0Okdolc:;;;c0MMMMMMMMMMMMMMM')
    print('XK00Okxddolc::;;;;;;;;;c0MMMMMMMMMMMMMMM')
    print('c::;;;;;;;;;;;;;;;;;;;;c0MMMMMMMMMMMMMMM')
    print(';;;;;;;;;;;;;;;;;;;;;;;c0MMMMMMMMMMMMMMM')
    print(';;;;;;;;;;;;;;;;;;;;;;;cx0000000000000KX')
    print(';;;;;;;;;;::;;;;;;;;;;;:dOOOOOOOOOOOOOxl')
    print(';;;;;;:ok0KK0ko:;;;;;;;c0MMMMMMMMMMWNOdc')
    print(';;;;;cONN0kOXWNkc;;;;;;c0WMMMMMMMWXOxkOl')
    print(';;;;:OWXd;;;l0WNx;;;;;;:oOXWMMMWXkxOXWXo')
    print(';;;;lKWO:;;;;xNWO:;;;;;ckOxkXNKkxONWMMXo')
    print(';;;;lKW0c;;;:kWWO:;;;;;c0WNOkxx0NMMMMMXo')
    print(';;;;:kNNkc:cdXWXo;;;;;;c0MMMWNWMMMMMMMXo')
    print(';;;;;cxXNXKXNN0o;;;;;;;c0MMMMMMMMMMMMMXo')
    print(';;;;;;;coxkkxo:;;;;;;;;c0MMMMMMMMMMMMMXo')
    print(';;;;;;;;;;;;;;;;;;;;;;;:xO000000000000kl')
    print(';;;;;;;;;;;;;;;;;;;;;;;:xOOOOOOOOOOOOOO0')
    print(';;;;;;;;;;;;;;;;;;;;;;;c0MMMMMMMMMMMMMMM')
    print('lc::;;;;;;;;;;;;;;;;;;;c0MMMMMMMMMMMMMMM')
    print('NXXK0Okxxdolcc::;;;;;;;c0MMMMMMMMMMMMMMM')
    print('MMMMMMMMWWNNXKOkxolc:::lKMMMMMMMMMMMMMMM')
    print('+++++++++++++++++++++++++++++++++++++++++++++++++++')
    print('|||||||||||||         LOG IN          |||||||||||||')
    print('---------------------------------------------------')
    imapObj = imapclient.IMAPClient('outlook.office365.com', ssl=True, use_uid=True)
    # If the first number returned is '235', then this means that authentication
    # has been successful
    print('+++++++++++++++++++++++++++++++++++++++++++++++++++')
    print('Please enter your Outlook email login information:')
    username = str(input('\nUsername: '))
    print('---------------------------------------------------')
    print('+++++++++++++++++++++++++++++++++++++++++++++++++++')
    password = str(getpass.getpass('\nPassword: '))
    print('---------------------------------------------------')
    imapObj.login(username, password)
    print('***************************************************')
    print('|||||||||||||       LOGGED IN         |||||||||||||')
    print('***************************************************')
    select_info = imapObj.select_folder('INBOX', readonly=True)
    print('\n\nMESSAGES: %d messages in INBOX' % select_info[b'EXISTS'])

    return imapObj


def parseEmail(imapObj):
    continue_decision = True
    while continue_decision:
        print('\n')
        print('***************************************************')
        print('||||||||||| CHOOSE YOUR TYPE OF SEARCH  |||||||||||')
        print('***************************************************')
        print('Choices:')
        print('1. List available email folders in Outlook mailbox:')
        print('\n2. View email from a particular time frame:')
        search_decision = int(input('\nProvide a numerical value for one of the following options: '))
        if search_decision == 1:
            print('***************************************************')
            print('|||||||||||||    AVAILABLE FOLDERS    |||||||||||||')
            print('***************************************************')
            print('\nFOLDERS:')
            for item in imapObj.list_folders():
                print(str(item))
            user_input = str(input("\n\nWould you like to continue checking messages? ('y' or 'n'): ")).lower()
            if user_input == 'n':
                imapObj.logout()
                print('***************************************************')
                print('|||||||||||       G O O D B Y E !       |||||||||||')                
                print('|||||||||||      THANKS FOR USING:      |||||||||||')
                print('|||||||||||   OUTLOOK TERMINAL CLIENT   |||||||||||')
                print('***************************************************')                                
                continue_decision = False
        if search_decision == 2:
            print('***************************************************')
            print('|||||||||||||      SEARCH TERMS       |||||||||||||')
            print('|||||||||||||      (TIME FRAME)       |||||||||||||')
            print('***************************************************')
            future_date_check = False
            while not future_date_check:
                month = str(input('\nMonth (2-digit variant, ex: Enter \'05\' for May): '))
                while len(month) != 2:
                    month = str(input('\nINCORRECT INPUT!\nYou MUST enter a 2-digit month!\nMonth (2-digit variant, ex: Enter \'05\' for May): '))
                day = str(input('\nDay (2 digit variant, ex: 01): '))
                while len(day) != 2:
                    day = str(input('\nINCORRECT INPUT!\nYou MUST enter a 2-digit day!\nDay (2 digit variant, ex: 01): '))
                year = str(input('\nYear (4 digit variant, ex: 2020): '))
                while len(year) != 4:
                    year = str(input('\nINCORRECT INPUT!\nYou MUST enter a 4-digit year!\nYear (4 digit variant, ex: 2020): '))
                # TODO: Save combined_date so that a user can easily re-select
                # the same date so that they don't have to re-enter the
                # desired date:
                month = int(month)
                day = int(day)
                year = int(year)
                combined_date = date(year, month, day)
                current_date = date.today()
                # TODO: Figure out why I can't use 2019 and previous
                # years for the 'year' variable:
                if combined_date > current_date:
                    print('\nINCORRECT INPUT!\nYou CANNOT enter a future date!\nPlease re-enter the current date information.')
                if combined_date <= current_date:
                    future_date_check = True
            uid_list = imapObj.search(['SINCE', combined_date])
            # print('\n\nMessages: %s' %(uid_list))
            rawMessages = imapObj.fetch(uid_list, ['BODY[]'])
            print('\n\nSubjects of Messages: ')
            for uid in uid_list:
                uid_index = uid_list.index(uid)
                pyzmail_message = pyzmail.PyzMessage.factory(rawMessages[uid_list[uid_index]][b'BODY[]'])
                print(uid_index+1, ': %s' %(pyzmail_message.get_subject()))
            message_num = int(input('\n\nEnter the message number you would like to read: ')) - 1
            desired_msg = pyzmail.PyzMessage.factory(rawMessages[uid_list[message_num]][b'BODY[]'])
            # If they DO have Text and DON'T have HTML, use Text:
            if desired_msg.text_part != None:
                print('\n%s' %(desired_msg.text_part.get_payload().decode(desired_msg.text_part.charset)))
            # Print HTML version if all else fails:
            if desired_msg.text_part == None and desired_msg.html_part != None:
                print('\n%s' %(desired_msg.html_part.get_payload().decode(desired_msg.html_part.charset)))
            user_input = str(input("\n\nWould you like to continue checking messages? ('y' or 'n'): ")).lower()
            if user_input == 'n':
                imapObj.logout()
                print('***************************************************')
                print('|||||||||||       G O O D B Y E !       |||||||||||')
                print('|||||||||||      THANKS FOR USING:      |||||||||||')
                print('|||||||||||   OUTLOOK TERMINAL CLIENT   |||||||||||')
                print('***************************************************')                
                continue_decision = False


def main():
    imapObj = userLogin()
    parseEmail(imapObj)

    
if __name__ == "__main__":
    main()
