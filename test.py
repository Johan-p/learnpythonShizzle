from pyvirtualdisplay import Display
from selenium import webdriver

display = Display(visible=1, size=(800, 600))
display.start()
driver = webdriver.Chrome('/usr/bin/google-chrome')
driver.get('https://automatetheboringstuff.com/')
print driver.title