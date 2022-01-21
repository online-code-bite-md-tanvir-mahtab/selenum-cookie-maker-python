# importing all the module that are importent
from cgi import print_environ
from time import sleep
from cv2 import idct
from selenium import webdriver


edge_driver_path = 'F:\python practice\edgedriver_win64\msedgedriver.exe'
TIME = 300
def click_on_cookie(driver):
    big_cookie = driver.find_element_by_id(id_="cookie")
    # sleep(4)
    # now i am going to click it
    for _ in range(100):
        big_cookie.click()

def check_the_money(driver):
    number = driver.find_element_by_id(id_="money")
    money = (number.text.split(','))
    real_money = (''.join(money))
    return int(real_money)

def highest_upgradble(driver,price):
    pointer = driver.find_element_by_css_selector("#buyCursor b")
    list_of_pointer = int(pointer.text.split("-")[1])
    grandma = driver.find_element_by_css_selector("#buyGrandma b")
    list_of_grandma = int(grandma.text.split("-")[1])
    factory = driver.find_element_by_css_selector("#buyFactory b")
    list_of_factory = int(factory.text.split('-')[1])
    # mine  = driver.find_element_by_css_selector("#buyMine b")
    # list_of_mine = int(mine.text.split('-')[1])
    # shipment = driver.find_element_by_css_selector("#buyShipment b")
    # list_of_shipment = int(shipment.text.split('-')[1])
    # lab = driver.find_element_by_xpath(xpath='//*[@id="buyAlchemy lab"]')
    # list_of_lab = int(lab.text.split('-')[1])
    # portal = driver.find_element_by_css_selector("#buyPortal b")
    # list_of_portal = int(portal.text.split('-')[1])
    # timemachine = driver.find_element_by_xpath(xpath='//*[@id="buyTime machine"]')
    # list_of_timemachine = int(timemachine.text.split('-')[1])
    if list_of_pointer <= price and list_of_grandma> price:
        pointer.click()
    if list_of_grandma <= price and list_of_factory> price:
        grandma.click()
    # elif list_of_mine <= price:
    #     mine.click()
    if list_of_factory <= price:
        factory.click()
    # elif list_of_lab <= price:
    #     lab.click()
    # elif list_of_shipment <= price:
    #     shipment.click()
    # elif list_of_portal <= price:
    #     portal.click()
    # elif list_of_timemachine <= price:
    #     timemachine.click()


# now i am going to create the driver
driver = webdriver.Edge(executable_path=edge_driver_path)

# nwo let open and get the url
# driver.get(url="https://orteil.dashnet.org/cookieclicker/")
driver.get(url='http://orteil.dashnet.org/experiments/cookie/')
count_time = 0
while TIME>0:
    click_on_cookie(driver)
    count_time+=1
    if count_time == 5:
        price = check_the_money(driver)
        highest_upgradble(driver,price)
        count_time=0
    TIME -=1

total_price = check_the_money(driver)
total_second = driver.find_element_by_id(id_='cps').text
print(f"total you have earned :{total_price}")
print(f"total second :{total_second}")

# now i am going to close the browser
driver.close()