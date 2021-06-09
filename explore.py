from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import time
import re

base_url = 'https://prod-ssb-01.dccc.edu/PROD/bwckschd.p_disp_dyn_sched'

courses_link = re.compile(r'^https://prod-ssb-01.dccc.edu/PROD/bwckschd.p_disp_detail_sched?term_in=202101&crn_in=')


class Sourcing:
    def run(self):
        self.open_link()
        self.get_subject_list()
        self.get_the_title_email_name()

        self.driver.quit()

    def open_link(self):
        self.driver = webdriver.Chrome('chromedriver.exe')
        self.driver.get(base_url)
        self.term = self.driver.find_element_by_name('p_term')
        spring = self.term.find_element_by_xpath('/html/body/div[4]/form/table/tbody/tr/td/select/option[6]')
        spring.click()
        submit = self.term.find_element_by_xpath('/html/body/div[4]/form/input[2]')
        submit.click()

    def get_subject_list(self):
        self.subjects_block = self.driver.find_element_by_name('sel_subj')
        self.subjects = self.subjects_block.find_elements_by_xpath('/html/body/div[4]/form/table[1]/tbody/tr/td['
                                                                   '2]/select/option')
        # subjects is a list
        # print(self.subjects[70].text)

        # some repetition here subjects == subject_list

        self.subjects_list = []
        for self.subject in self.subjects:
            try:
                subject_name = self.subject.text.split(')')[1]
                if ')' == subject_name[-1]:
                    subject_name = subject_name

            except:
                subject_name = self.subject.text.split(']')[1]
            self.subjects_list.append(subject_name)
            # print(self.subjects_list)
            # click inside the loop systematically clicks on the the subjects... One after another
            self.subject.click()
        class_search = self.driver.find_element_by_xpath('/html/body/div[4]/form/input[12]')
        class_search.click()

    def get_the_title_email_name(self, ):

        # get title, name of lec and schedule type, email
        self.clean_links = []
        titles = []
        instructor_names = []
        instructor_emails = []
        malink = self.driver.find_elements_by_xpath("//a[@href]")
        # grab all links
        title_link = []

        for unclean_link in malink:
            urls = unclean_link.get_attribute("href")
            if re.match(courses_link, urls):
                title = unclean_link.text
                titles.append(title)
                self.clean_links.append(urls)
                mail_to = self.driver.find_elements_by_xpath("a[href^=mailto]")
                email = mail_to.get_attribute('href')
        print(titles)

    def get_the_class_capacity_and_type(self, ):
        class_capacity = []
        class_types = []
        for url in self.clean_links:
            self.driver.get(url)
            # time.sleep()

            class_cap = self.driver.find_element_by_xpath(
                '/html/body/div[4]/table[1]/tbody/tr[2]/td/table[1]/tbody/tr[2]/td[1]').text
            class_capacity.append(class_cap)
            class_type = self.driver.find_element_by_xpath('/html/body/div[4]/table[1]/tbody/tr[2]/td/text()[4]').text
            class_types.append(class_type)

    def add_to_xlsx(self):
        pass


if __name__ == '__main__':
    print("Starting....")
    souring = Sourcing()
    data = souring.run()
