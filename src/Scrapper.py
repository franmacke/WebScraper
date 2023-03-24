from selenium import webdriver
from selenium.webdriver.common.by import By

URL_TEST = 'https://www.adidas.com.ar/remera-argentina-campeon-2022/IR0032.html?cm_sp=SLOT-4.6-_-HOME_%3F_%3F_HOME_%3F-_-PRODUCTSELECTIONCAROUSEL-PRODUCT-CARD-_-1007018'
URL = "https://www.adidas.com.ar/camiseta-titular-argentina-3-estrellas-2022/IB3593.html?cm_sp=SLOT-4.5-_-HOME_%3F_%3F_HOME_%3F-_-PRODUCTSELECTIONCAROUSEL-PRODUCT-CARD-_-1007018"


DRIVER_URL = r'C:\Users\franc\Documents\GitHub\camiseta_scapper\chromedriver'


class WebScrapper:
    def __init__(self):
        self.webdriver = None
        self.options = webdriver.ChromeOptions()

    def initWebDriver(self):
        try:
            self.webdriver = webdriver.Chrome(executable_path=DRIVER_URL.join("\\chromedriver_win32.exe"), options=self.options)
        except:
            print('Hubo un error al iniciar webdriver')


    def update(self):
        self.webdriver.get(URL)
        self.webdriver.implicitly_wait(10)

        try:
            self.webdriver.find_element(By.ID, 'add-to-bag')
            return True
        except:
            return False

    def exit(self):
        self.webdriver.quit()
