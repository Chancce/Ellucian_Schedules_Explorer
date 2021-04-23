from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import time
import re

base_url = 'https://prod-ssb-01.dccc.edu/PROD/bwckschd.p_disp_dyn_sched'
courses_link = re.compile('^https://prod-ssb-01.dccc.edu/PROD/bwckschd.p_disp_detail_sched?term_in=202101&crn_in')


class Sourcing:
    def run(self):
        self.open_link()
        self.get_subject_list()
        self.loop_subject_list()
        # self.get_the_title()

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

        #some repetition here subjects == subject_list

        self.subjects_list = []
        for subject in self.subjects:
            try:
                subject_name = subject.text.split(')')[1]
                if ')' == subject_name[-1]:
                    subject_name = subject_name

            except:
                subject_name = subject.text.split(']')[1]
            self.subjects_list.append(subject_name)


    def loop_subject_list(self,):

        for classs in self.subjects:
            classs.click()
            class_search = self.driver.find_element_by_xpath('/html/body/div[4]/form/input[12]')
            class_search.click()

            pass

        #print(subjects_list)

    def loop_through_subjects(self, ):
        pass

    def get_the_title(self, ):
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
