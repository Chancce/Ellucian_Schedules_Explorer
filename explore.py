from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import time
import re

base_url = 'https://prod-ssb-01.dccc.edu/PROD/bwckschd.p_disp_dyn_sched'


class Sourcing:
    def run(self):
        self.open_link()
        self.get_subject_list()
        self.loop_through_subjects()

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
        ''' self.subject_list = []
        for subject in self.subjects:
            self.subject_name = subject.get_attribute('innerHTML')
            self.subject_list.append(self.subject_name)

        print(self.subject_list)
            '''

    def loop_through_subjects(self, ):
        self.subject_list = []
        for subject in self.subjects:
            self.subject_name = subject.get_attribute('innerHTML')
            # moving append here selects all subjects
            # self.subject_list.append(self.subject_name)
            subject.click()
            class_search = self.driver.find_element_by_xpath('/html/body/div[4]/form/input[12]')
            class_search.click()

    def get_the_title(self):
        # get title, name of lec and schedule type, email
        pass

    def get_the_class_cap(self):
        # get the class capacity

        pass

    def add_to_xlsx(self):
        pass


if __name__ == '__main__':
    print("Starting....")
    souring = Sourcing()
    data = souring.run()
