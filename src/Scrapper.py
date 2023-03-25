from selenium import webdriver
from selenium.webdriver.common.by import By
import platform, os


DEBUG = os.getenv('DEBUG')
DRIVER_URL = ".\\chromedriver\\chromedriver_win32.exe" if platform.system() == 'Windows' else "./chromedriver/chromedriver_linux"

if DEBUG:
    URL = "https://www.adidas.com.ar/remera-argentina-campeon-2022/IR0032.html?cm_sp=SLOT-4.6-_-HOME_%3F_%3F_HOME_%3F-_-PRODUCTSELECTIONCAROUSEL-PRODUCT-CARD-_-1007018"
else:
    URL = "https://www.adidas.com.ar/camiseta-titular-argentina-3-estrellas-2022/IB3593.html?cm_sp=SLOT-4.5-_-HOME_%3F_%3F_HOME_%3F-_-PRODUCTSELECTIONCAROUSEL-PRODUCT-CARD-_-1007018"

class WebScrapper:
    def __init__(self):
        self.webdriver = None
        self.options = webdriver.ChromeOptions()
        self.talles = {
            'XS': False,
            'S': False,
            'M': False,
            'L': False,
            'XL': False,
            '2XL': False
        }

    def initWebDriver(self):
        try:
            self.webdriver = webdriver.Chrome(executable_path=DRIVER_URL, options=self.options)
        except:          
            print('Hubo un error al iniciar webdriver')
            raise Exception


    def update(self):
        self.webdriver.get(URL)
        self.webdriver.implicitly_wait(1)

        return self.hayCamisetas()
    
    
    def tallesDisponibles(self):
        try:
            self.webdriver.find_element(By.ID, 'add-to-bag')
        except:
            return self.talles

        talles = self.webdriver.find_element(By.XPATH, '//div[@data-auto-id="size-selector"]')

        for boton in talles.find_elements(By.TAG_NAME, 'button'):
            talle = boton.find_element(By.TAG_NAME,'span').get_attribute('innerHTML')

            if 'size-selector__size--unavailable___1EibR' not in boton.get_attribute('class').split(' '):
                self.talles.update({talle: True})

            else:
                self.talles.update({talle: False})

    def hayCamisetas(self):
        self.tallesDisponibles()
        return self.talles
        
    def exit(self):
        self.webdriver.quit()

