import requests
from bs4 import BeautifulSoup

import csv 

file = open('movie.csv', mode='w', newline='')
writer=csv.writer(file)
writer.writerow(["영화명","평점","이미지 주소","감독","출연자","개봉일자"])

movie_url= f'https://movie.naver.com/movie/running/current.nhn'
movie_html=requests.get(movie_url)
movie_soup=  BeautifulSoup(movie_html.text,"html.parser")

movie_list_box=movie_soup.find('div',{'id':'content'})
movie_list=movie_list_box.find('ul',{'class':'lst_detail_t1'})
movie=movie_list.find_all("li")

final_result = []
for movie_info in movie:
    title = movie_info.find('dt',{'class':'tit'}).find('a').text
    image = movie_info.find('div',{'class':'thumb'}).find('a').find('img')["src"]
    rating = movie_info.find('dd',{'class':'star'}).find('div',{'class':'star_t1'}).find('span',{'class':'num'}).text

    detail = []
    detail = movie_info.find('dl',{'class':'lst_dsc'}).find('dl',{'class':'info_txt1'}).find_all('dd')
        
    director= detail[1].find('a').text
    
    
    if detail[-1].find('a').text == "":
        actor= None
    else:    
            
        actor1= detail[-1].find_all('a')
        temp=[]
        for real_actor in actor1:
            temp.append(real_actor.text)
        temp3=[]  
        for i in range(len(actor1)):
            actor= detail[-1].find_all('a')[i].text
            temp3.append(actor)        

    actor=temp3



    detail2 = movie_info.find('dl',{'class':'lst_dsc'}).find('dl',{'class':'info_txt1'}).find_all('dd')
    temp2 = []
    for detail2_list in detail2:
        temp2.append(detail2_list.text)
    
    new_temp2=[i.replace("\t","") for i in temp2]
    new_temp2=[i.replace("\r","") for i in new_temp2]
    new_temp2=[i.replace("\n","") for i in new_temp2]

   
    release_date=new_temp2[0]
    release_date=release_date[-13:-2]
    
    
    movie_character={
        '영화명':title,
        '평점':rating,
        '이미지주소':image,
        '감독':director,
        '출연자':actor,
        '개봉일자':release_date

    }

    final_result.append(movie_character)

for result in final_result:
    row = []
    row.append(result['영화명'])
    row.append(result['평점'])
    row.append(result['이미지주소'])
    row.append(result['감독'])
    row.append(result['출연자'])
    row.append(result['개봉일자'])
    writer.writerow(row)
print(final_result)






