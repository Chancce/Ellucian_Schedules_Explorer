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
        self.loop_through_subjects()
    def open_link(self):
        self.driver=webdriver.Chrome('chromedriver.exe')
        self.driver.get(base_url)
        self.term=self.driver.find_element_by_name('p_term')
        spring=self.term.find_element_by_xpath('/html/body/div[4]/form/table/tbody/tr/td/select/option[6]')
        spring.click()
        submit=self.term.find_element_by_xpath('/html/body/div[4]/form/input[2]')
        submit.click()
    def loop_through_subjects(self):
        self.subjects_block=self.driver.find_element_by_name('sel_subj')
        base_xpath=''
        self.subjects=self.subjects_block.find_elements_by_xpath('/html/body/div[4]/form/table[1]/tbody/tr/td['
                                                                 '2]/select/option')
        print(self.subjects)



if __name__ == '__main__':
    print("Starting....")
    souring = Sourcing()
    data = souring.run()



