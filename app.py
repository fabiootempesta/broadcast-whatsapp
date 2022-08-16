from time import sleep
from selenium import webdriver
import urllib

def isElementPresent(by, value):
    try:
        browser.find_element(by, value)
    except:
        return False
    return True


options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:/Users/gig9/AppData/Local/Google/Chrome/User Data/Default") #colocar o caminho do user no lugar do "gig9"

browser = webdriver.Chrome(options = options)

listaContatos = open('./listacontato.txt', 'r')
texto = urllib.parse.quote("Ignore this message. \n It's just a test. Sorry for the inconvenience.")



for contato in listaContatos.readlines():
    findElement = False
    
    browser.get(f"https://web.whatsapp.com/send?phone={contato}&text={texto}")
    
    while (findElement == False):
        if (isElementPresent("xpath", '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span')):
            browser.find_element("xpath", '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span').click()
            findElement = True
        
        if (isElementPresent("xpath", '//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div[2]/div')):
            findElement = True
        
        
        sleep(0.2)

    

    sleep(0.5)

exit()