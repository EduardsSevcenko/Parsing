from bs4 import BeautifulSoup
import pandas as pd
import requests
import lxml

def parse_page(url):
    response = requests.get(url).text
    soup = BeautifulSoup(response,'lxml')
    vacancies_name = [i.text for i in soup.select('div._3zucV._2cmJQ._1SCYW div.f-test-search-result-item div._1h3Zg._2rfUm._2hCDz._21a7u a')]
    vacancies_url = ['https://www.superjob.ru/vacancy/search/' + i['href'] for i in soup.select('div._1ID8B div._3zucV._2cmJQ._1SCYW div.f-test-search-result-item div._1h3Zg._2rfUm._2hCDz._21a7u a')]
    vacancies_salary = [i.text for i in soup.select('div._1ID8B div._3zucV._2cmJQ._1SCYW div.f-test-search-result-item span._1h3Zg._2Wp8I._2rfUm._2hCDz._2ZsgW')]
    vacancies_to_return = []
    for num, item in enumerate(vacancies_name):
        vacancies_to_return.append({
            'name': item,
            'url': vacancies_url[num],
            'salary': vacancies_salary[num].replace(u'\xa0', ' '),
            'webpage': url
        })
    return vacancies_to_return

#url = 'https://www.superjob.ru/vacancy/search/'
#print(parse_page(url))

all_vacancies = []
for i in range(1,101):
    url = 'https://www.superjob.ru/vacancy/search/?page={}.html'.format(i)
    vacancies_temp = parse_page(url)
    if i == 100:
        response = requests.get(url).text
        soup = BeautifulSoup(response, 'lxml')
    all_vacancies += vacancies_temp

pd.DataFrame(all_vacancies).to_csv('vacancies.csv', index=False)

