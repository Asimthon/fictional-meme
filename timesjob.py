from bs4 import BeautifulSoup
import requests
import pandas as pd
timesjob={}
#n=input(f'Enter the range')
job_list=[]
company_list=[]
experience_list=[]
location_list=[]
skill_list=[]
posting_list=[]
lists=[company_list,location_list,experience_list,skill_list,posting_list]
for page in range(1,5):
    url=f'https://www.timesjobs.com/candidate/job-search.html?from=submit&actualTxtKeywords=python&searchBy=0&rdoOperator=OR&searchType=personalizedSearch&luceneResultSize=25&postWeek=60&txtKeywords=python&pDate=I&sequence=1&startPage={page}'
#url="https://www.timesjobs.com/candidate/job-search.html?from=submit&actualTxtKeywords=python&searchBy=0&rdoOperator=OR&searchType=personalizedSearch&luceneResultSize=25&postWeek=60&txtKeywords=python&pDate=I&sequence=3&startPage=40"
    response_code=requests.get(url)
    print(response_code)
    html_text=requests.get(url).content
    soup=BeautifulSoup(html_text,'lxml')
#print(soup)
#print(soup.title.get_text())
    details=soup.find_all('li','clearfix job-bx wht-shd-bx')
#print(details)
    for detail in details:
        print(f'page {page} is collected')
        company_name=detail.find('h3','joblist-comp-name').get_text().replace('\r\n',' ')
        print(f' Company name is {company_name}')
        location=detail.find('ul','top-jd-dtl clearfix').get_text().replace('-',' ').replace('_',' ').replace('card travel','').replace('location on','').split('yrs')[1].replace('\n',' ')
        print(f'Location of {company_name } is:- {location}')
        experience=detail.find('ul','top-jd-dtl clearfix').get_text().replace('_',' ').replace('card travel','').replace('location on','').split('yrs')[0].replace('\n',' ')
        print(f' Experience required is:- {experience} years')
        skill=detail.find('span','srp-skills').get_text().replace(' ','').replace('\n',' ').title()
        print(f'Skill needed is:- {skill}')
        posting=detail.find('span','sim-posted').get_text().replace('\n',' ')
        print(f'Duration of posting is:- {posting}')
        values = [company_name,location,experience,skill,posting]
        for l, v in zip(lists, values):
            l.append(v)
keys = ['Company Name', 'Location', 'Experience in years', 'Skills Required', 'Duration of Posting']
for k, v in zip(keys, lists):
    timesjob[k] = v
timesjob = pd.DataFrame(timesjob, columns=keys)
print(timesjob)
timesjob.to_csv('timesjob.csv')
timesjob.to_json('timesjob.json')
timesjob.to_excel('timesjob.xlsx')




