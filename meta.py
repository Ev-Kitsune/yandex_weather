from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Setting:

    mainPth = ""
    IM_PWAIT = 3
    Keys = Keys
    x = 1024
    y = 768
    
    def initDriver(self, pathToDriver):
        """
        Инициализация вебдрайвера
        """
        driver = webdriver.Chrome(pathToDriver)
        
        driver.implicitly_wait(self.IM_PWAIT)
        driver.set_window_size(self.x, self.y)
    
        return driver