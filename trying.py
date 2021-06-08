from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import time
from selenium.common.exceptions import NoSuchElementException
import re
from selenium import webdriver
import re

source_info = ''
BASE_URL = 'https://prod-ssb-01.dccc.edu/PROD/bwckschd.p_disp_dyn_sched'
TERM = 'Fall'
DEPARTMENT = 'English'
MULTIPLE_URLS = 'urls'


# full_name = ''
# course_name = ''
# course_code = ''
# class_capacity = ''
# import pandas as pd


def get_chrome_web_driver(options):
    return webdriver.Chrome('chromedriver.exe', chrome_options=options)


def get_web_driver_options():
    return webdriver.ChromeOptions()


def set_ignore_certificate_error(options):
    options.add_argument('--ignore-certificate-errors')


def set_browser_as_incognito(options):
    options.add_argument('--incognito')


def set_automation_as_head_less(options):
    options.add_argument('--headless')


'''from config import (
    source_info,
    BASE_URL,
    TERM,
    DEPARTMENT,
    MULTIPLE_URLS,

    get_chrome_web_driver,
    get_web_driver_options,
    set_browser_as_incognito,
    set_ignore_certificate_error,
)'''

# open url
# select fall
# select dept
# get course name in title
# get lecname in title
# get course name in title
# get course code
# get capapcity


'''class DataResults:
    def __init__(self):
        pass
'''


class SourcingAPI:
    def __init__(self, base_url, term, department, multiple_urls):
        self.base_url = base_url
        self.term = term
        self.department = department
        options = get_web_driver_options()
        set_ignore_certificate_error(options)
        set_browser_as_incognito(options)
        self.driver = get_chrome_web_driver(options)

    def run(self):

        self.open_link()
        # self.convert_url_to_list()
        # self.get_all_titles_and_info()
        # self.get_class_info()
        self.driver.quit()

    def open_link(self):
        self.driver.get(self.base_url)
        element = self.driver.find_element_by_name('p_term')
        element.send_keys(self.term)
        # submit_btn = ActionChains(self.driver)
        submit_btn = element.find_element_by_xpath('//body//input[2]')
        submit_btn.click()
        subject_list = self.driver.find_element_by_name('sel_subj')
        # subject_select.send_keys(self.department)
        english = subject_list.find_element_by_xpath(
            '/html[1]/body[1]/div[4]/form[1]/table[1]/tbody[1]/tr[1]/td[2]/select[1]/option[8]')
        english.click()
        search_btn = subject_list.find_element_by_xpath('//body//input[12]')
        search_btn.click()
        #soup = BeautifulSoup(self.driver.page_source, "html.parser")

        elems = self.driver.find_elements_by_xpath("//a[@href]")

        list_urls = []
        titles = []
        names = []
        # emails = []
        for elem in elems:
            # href = elem.get_attribute('href')attrs={'href': re.compile("^https://prod-ssb-01.dccc.edu/PROD/bwckschd.p_disp_detail_sched?term_in=202009&crn_in=")
            att = re.compile('^https://prod-ssb-01.dccc.edu/PROD/bwckschd.p_disp_detail_sched\?term_in=202009&crn_in')

            urls = elem.get_attribute('href')
            title = elem.text

            if att.match(urls):
                # something =urls.splitlines()
                titles.append(title)

                # mail_to =self.driver.find_elements_by_xpath("a[href^=mailto]")
                # email = mail_to.get_attribute('href')
                list_urls.append(urls)
                # names.append(name)
                # emails.append(email)
        print(titles)
        # print(names)
        # print(emails)

        schedule_types = []

        '''datadisplaytable = self.driver.find_elements_by_class_name('datadisplaytable')
        # dddfault = datadisplaytable.find
        # schedule_type = datadisplaytable.get('dddefault')
        print(str(datadisplaytable))
        print(len(datadisplaytable))
        print(type(datadisplaytable))'''

        '''schedule_type = self.driver.find_element_by_xpath('/html/body/div[4]/table[1]/tbody/tr[16]/td/table/tbody/tr[2]/td[6]').text
        schedule_types.append(schedule_type)
        print(schedule_types)'''

        # bs4 coming in

        class_capacity = []
        for url in list_urls:
            new_driver = self.driver
            new_driver.get(url)
            # time.sleep()

            class_cap = self.driver.find_element_by_xpath(
                '/html[1]/body[1]/div[4]/table[1]/tbody[1]/tr[2]/td[1]/table[1]/tbody[1]/tr[2]/td[1]').text

            class_capacity.append(class_cap)

        print(class_capacity)
        # print(soup)

        # print titles only

        #print(soup)
        # printing class things to pandas
        '''class_info = pd.DataFrame(
            {
                'class_title': titles,
                'enrlment': class_capacity,
            }
        )
        print(class_info)'''

        '''def get_all_titles_and_info(self):

        print('Getting Class Info and title....')
        current_url = 'https://prod-ssb-01.dccc.edu/PROD/bwckschd.p_get_crse_unsec'
        all_links = requests.get(current_url)
        links = all_links.text
        print(links)'''


if __name__ == '__main__':
    print("Starting....")
    souring = SourcingAPI(BASE_URL, TERM, DEPARTMENT, MULTIPLE_URLS)
    data = souring.run()
