from bs4 import BeautifulSoup
import pandas as pd
import requests
import lxml

def parse_page(url):
    response = requests.get(url).text
    soup = BeautifulSoup(response,'lxml')
    vacancies_name = [i.text for i in soup.select('div.vacancy-serp div.vacancy-serp-item vacancy-serp-item_premium span.bloko-header-3 a.vacancy-serp__vacancy-title')]
    vacancies_url = ['https://hh.ru/search/vacancy?area=1&fromSearchLine=true&st=searchVacancy&text=/' + i['href'] for i in soup.select('div.vacancy-serp div.vacancy-serp-item vacancy-serp-item_premium span.bloko-header-3 a.vacancy-serp__vacancy-title')]
    vacancies_salary = [i.text for i in soup.select('div.vacancy-serp div.vacancy-serp-item vacancy-serp-item_premium span.bloko-header-3 span.bloko-header-section-3 bloko-header-section-3_lite')]
    vacancies_to_return = []
    for num, item in enumerate(vacancies_name):
        vacancies_to_return.append({
            'name': item,
            'url': vacancies_url[num],
            'salary': vacancies_salary[num],#.replace(u'\xa0', ' '),
            'webpage': url
        })
    return vacancies_to_return

#url = 'https://www.superjob.ru/vacancy/search/'
#print(parse_page(url))

all_vacancies = []
for i in range(1,41):
    url = 'https://hh.ru/search/vacancy?area=1&fromSearchLine=true&st=searchVacancy&text=&page={}.html'.format(i)
    vacancies_temp = parse_page(url)
    if i == 40:
        response = requests.get(url).text
        soup = BeautifulSoup(response, 'lxml')
    all_vacancies += vacancies_temp

pd.DataFrame(all_vacancies).to_csv('vacancies2.csv', index=False)

