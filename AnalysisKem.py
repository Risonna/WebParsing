from selenium import webdriver
import pandas as pd
import numpy as np
import time
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import re
import seaborn as sns
import matplotlib.pyplot as plt
from numpy import nan

driver = webdriver.Chrome()
jobs = []
salaries = []
descriptions = []

driver.get("https://kemerovo.hh.ru/search/vacancy?area=47&search_field=name&searc"
           "h_field=company_name&search_field=description&te"
           "xt=%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B8%D1%81%D1%82&enable_snippets=true")
content = driver.page_source
soup = BeautifulSoup(content, "html.parser")
# print(soup.find('span', attrs={'data-qa': 'serp-item__title'}).text)
# print(soup.find('span', class_=re.compile('compensation-text--\w+')).text)
# print(soup.find('span', attrs={'data-qa': 'vacancy-serp__vacancy-work-experience'}).text)
# print(soup.find('div', attrs={'data-qa': 'vacancy-serp__vacancy_snippet_requirement'}).text)

for page in range(0, 3):
    driver.get("https://kemerovo.hh.ru/search/vacancy?area=47&search_field=name&search_fi"
               "eld=company_name&search_field=description&tex"
               "t=%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B8%D1%81%D1%82&enabl"
               "e_snippets=true&page="+str(page))
    content = driver.page_source
    soup = BeautifulSoup(content, "html.parser")
    for tag in soup.findAll('div', class_=re.compile('vacancy-card--\w+')):
        job = tag.find('span', attrs={'data-qa': 'serp-item__title'})
        salary = tag.find('span', class_=re.compile('compensation-text--\w+'))
        description = tag.find('div', attrs={'data-qa': 'vacancy-serp__vacancy_snippet_requirement'})
        if job is not None:
            jobs.append(job.text)
        else:
            jobs.append(None)
        if salary is not None:
            salaries.append(salary.text)
        else:
            salaries.append(None)
        if description is not None:
            descriptions.append(description.text)
        else:
            descriptions.append(None)
print(len(jobs), len(salaries), len(descriptions))

df = pd.DataFrame({'Job': jobs, 'Salary': salaries, 'Description': descriptions})
df.head()
df.to_csv(r'C:\temp\kem_hh_ru.csv', index=False, encoding='utf-8')
