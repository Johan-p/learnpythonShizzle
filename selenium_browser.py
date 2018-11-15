"""


"""
print(__doc__)

from selenium import webdriver
browser = webdriver.Chrome()
browser.get('https://automatetheboringstuff.com')

elem = browser.find_element_by_css_selector('body > div.main > div:nth-child(1) > div:nth-child(3) > a')
print elem.text


elem.click()

#for text fields, that you want to fill
#elem.send_keys('string')

#if its part of a form, use .submit to submit it
#elem.submit()

browser.quite()

def var():
	pass


a = None

if __name__=='__main__':
	var()