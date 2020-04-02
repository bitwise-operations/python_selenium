from selenium import webdriver
import time


class Locators():
    LINK = "//a[@href]"
    SEARCH_FIELD = "input[name='q']"
    IMAGES = "//*[text()='Картинки']/.."
    TOOLS = "//*[text()='Инструменты']/.."
    SIZE = "//*[text()='Размер']/.."
    BIG = "//*[text()='Большой']/.."
    NEXT = "//span[text()='Следующая']/.."
    RATING_IN_SEARCH = "//a[@href='%s']/../../div[2]/div/div"
    RATING_IN_REVIEWS = "//h2[text()='Отзывы']/../../c-wiz/div/div"
    LINK_IVI = 'play.google.com/store/apps/details?id=ru.ivi.client'
    PATH = # specify the path to the repository /python_selenium

class Google_page(Locators):

    def __init__(self):
        # specify the full path to the file chromedriver
        self.driver = webdriver.Chrome('%s/python_selenium/chromedriver' % PATH)
        self.base_url = 'https://www.google.com/'

    def search(self):
        # open the search page and make a query with the parameter
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_css_selector(Locators.SEARCH_FIELD).send_keys('ivi\n')

    def switch_to_images(self):
        # go to the google images section and select large images
        driver = self.driver
        driver.find_element_by_xpath(Locators.IMAGES).click()
        driver.find_element_by_xpath(Locators.TOOLS).click()
        time.sleep(1)
        driver.find_element_by_xpath(Locators.SIZE).click()
        driver.find_element_by_xpath(Locators.BIG).click()

    def all_url_element(self):
        # get all the links that are on the page
        driver = self.driver
        elements = driver.find_elements_by_xpath(Locators.LINK)
        return elements

    def count_url_ivi(self):
        # for testing we get all the links to ivi in the google images section
        self.search()
        self.switch_to_images()
        elements = self.all_url_element()
        count_url = 0
        for elem in elements:
            if 'ivi.ru' in elem.get_attribute("href"):
                count_url += 1
        return count_url

    def next_page_search(self):
        # go to the next search page
        self.driver.find_element_by_xpath(Locators.NEXT).click()

    def rating_on_content(self):
        # for the test pass the first 5 pages of the search 
        # and save the rating values ivi for play.google.com
        rating_val = []
        self.search()
        for i in range(5):
            self.save_to_rating(rating_val)
            self.next_page_search()  
        return rating_val

    def save_to_rating(self, rating_value):
        # save the rating values ivi for play.google.com
        elements = self.all_url_element()
        for elem in elements:
            if Locators.LINK_IVI in elem.get_attribute("href"):
                l = elem.get_attribute("href")
                rating = self.driver.find_element_by_xpath(Locators.RATING_IN_SEARCH % l)
                rating = rating.text.split()
                rating_value.append(rating[1])
        return rating_value


    def rating_on_the_page(self):
        # for the test go through the first 5 pages of the search 
        # and save the links for play.google.com go to 
        # and save the ivi rating values
        rating_v = []
        links = []
        self.search()
        for i in range(5):
            elements_l = self.all_url_element()
            for x in elements_l:
                if Locators.LINK_IVI in x.get_attribute("href"):
                    links.append(x.get_attribute("href"))
            self.next_page_search()
        for link in links:
            self.driver.get(link)
            r = self.driver.find_element_by_xpath(Locators.RATING_IN_REVIEWS)
            r = r.text
            rating_v.append(r)
        return rating_v

    def search_wiki(self):
        # for the test go through the first 5 pages of the search
        # find and save a wiki link
        # go to the wiki article and find all links to ivi
        self.search()
        link_wiki = ''
        for i in range(5):
            el = self.all_url_element()
            for e in el:
                if 'wikipedia.org' in e.get_attribute("href"):
                    link_wiki = e.get_attribute("href")
                    break
            self.next_page_search()
        self.driver.get(link_wiki)
        link_w = self.all_url_element()
        link_ivi = False
        for li in link_w:
            if 'ivi.ru' in li.get_attribute("href"):
                link_ivi = True
        return link_ivi


    def driver_close(self):
        # close the window
        self.driver.quit()
