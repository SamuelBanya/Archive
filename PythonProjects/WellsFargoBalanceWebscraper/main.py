#!/usr/bin/python3
# WellsFargoBalanceWebscraper: This is a Python3 script that utilizes
# Firefox's Selenium webdriver in order to obtain the current
# balance for a user's account

from selenium import webdriver
import getpass

def promptForCreds():
    print('\nWelcome To Wells Fargo Balance Webscraper!')
    print("............................................................")
    print("............................................................")
    print("............................................................")
    print("............................................................")
    print("............................................................")
    print("............................................................")
    print("............................................................")
    print("............................................................")
    print("..':lll::lllc:clllllllllllcccllllc;...;clllc,...':llolcc,...")
    print("..'cxOkc:dOOo:lkkookOxoddxkocx00kl,...,lkOdc,..'lOxlclkkc...")
    print("....ckOl;dOOo:okl';xOxdkl;:,,oOOx;.....;xOl'...'lkOxoodd;...")
    print("....'oOkxkkOOkkd,.;xOxdxl:c;,oO0x;.':c,;xOl'.':cldoloxkkl'..")
    print(".....;dO0d:oO0x:.,lkOdlddxkolx00klclkkllkOdccokkkOdcclxOl'..")
    print("......;cl;.,cl:'.;lllllllllccllllllllccllllllllcccclool:'...")
    print("............................................................")
    print("....',;;,;;;;,'.',,'..',,,;,,;,,'...';::;,,,...',;::;,'.....")
    print("....,lxkxoodxx:,lkkl,.;lxkxlldkko;'cdkxodxko,':dxdoodxo;....")
    print(".....'oOxloolo:lkkkkl'.,dOd::dkOkcckOo,',lxd:ckOo,..,dOx;...")
    print(".....'oOkxko,'ckOxk0kc',dOxodO0Ol,lOOc.'cdkkddOOc...'lOkc...")
    print(".....;dOxcc:,:xOdlox0x::x0d;:x0OdlokOd:,:dOk::xOd;',:xOd,...")
    print("....,ldxdo:':oxdo::dxxdodxdl:lxxkdc:oxdddddo,.;lddooddc,....")
    print(".....'''''...''''.''''''''''..',,'...',,,'''....',,,''......")
    print("............................................................")
    print("............................................................")
    print("............................................................")
    print("............................................................")
    print("............................................................")
    print("............................................................")
    print("............................................................")
    print("............................................................")
    print('+++++++++++++++++++++++++++++++++++++++++++++++++++')
    print('Please enter your Wells Fargo login information:')
    username = str(input('\nUsername: '))
    print('---------------------------------------------------')
    print('+++++++++++++++++++++++++++++++++++++++++++++++++++')
    password = str(getpass.getpass('\nPassword: '))
    print('---------------------------------------------------')
    
    return username, password


def accessWellsFargoPage(username, password):
    browser = webdriver.Firefox()
    browser.get('https://www.wellsfargo.com/')
    usernameElem = browser.find_element_by_id('userid')
    usernameElem.send_keys(username)
    passwordElem = browser.find_element_by_id('password')
    passwordElem.send_keys(password)
    signonButton = browser.find_element_by_id('btnSignon')
    signonButton.click()


def main():
    username, password = promptForCreds()
    accessWellsFargoPage(username, password)

    
if __name__ == '__main__':
    main()
