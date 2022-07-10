import selectors_lib

class Standart:
    driver = ''
    def __init__(self, driver):
        self.driver = driver

    def make_scr(self, name):
        scr = self.driver.get_screenshot_as_file('C:\\Users\\lp-ph\\OneDrive\\Документы\\code\\For_Lessons\\test_smoke\\screens' + name + '.png')

    def scroll_page(self, x , y):
        self.driver.execute_script("window.scroll(" + str(x) + "," + str(y) + ")")

class Header:
    driver = ''
    selectors = selectors_lib.selectors
    def __init__(self, driver):
        self.driver = driver

    def select_items(self, number):
        elements = self.driver.find_elements_by_css_selector(self.selectors['mainMenu'])
        if (len(elements) > 0):
            elements[number].click()
            return True
        else:
            return "Not found"

    def search_play(self, request, keys):
        element = self.driver.find_element_by_css_selector(self.selectors['search'])
        element.send_keys(request)
        element.send_keys(keys.ENTER)

        element = self.driver.find_element_by_css_selector(self.selectors['resultSearch'])
        if "Вы искали: "+request in element.text:
            return True
        else:
            return False



     

class Weather:
    driver = ''

    def __init__(self, driver):
        self.driver = driver

    def open_page_10_days(self):
        try:
            self.driver.find_elements_by_css_selector(self.selectors['forecast'])[0].click()
            res1 = True
        except:
            res1 = False 
        return res1
        
    def check_prognoz(self, length, selector):
        elements = self.driver.find_elements_by_css_selector(selector)
        if len(elements) == length:
            res2 = True
        else:
            res2 = False
        return res2

    def next_30_days(self):
        elements = self.driver.find_elements_by_css_selector(self.selectors['allDays'])
        if (len(elements) > 0):
            num_str = self.driver.find_elements_by_css_selector(self.selectors['lenMounth'])[0].text
            num = int(num_str.split(' ')[0])
            dis_elements = self.driver.find_elements_by_css_selector(self.selectors['colorlessDays'])
            if (len(elements) - len(dis_elements) == num):
                return True
            else:
                return "Ne-sootvetstvie dney"
        else:
            return "DOLGOVATO BUDET"


       