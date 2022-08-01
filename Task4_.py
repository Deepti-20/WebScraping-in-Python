from bs4 import BeautifulSoup
import requests
import json
def scrape_movie_details():
    details_dict = {}
    url="https://www.imdb.com/title/tt0066763/"
    page= requests.get(url)
    # print(responce)
    soup=BeautifulSoup(page.text,"html.parser")
    poster=soup.find("div",class_="ipc-poster").a["href"]
    # print(poster)
    poster1="https://www.imdb.com"+poster
    details_dict["poster_image_url"]=poster1
    biodata=soup.find("span",class_="GenresAndPlot__TextContainerBreakpointXL-cum89p-2 gCtawA").text
    details_dict["bio"]=biodata
    movie_name=soup.find("div",class_="TitleBlock__Container-sc-1nlhx7j-0 hglRHk").h1.text
    # print(movie_name)
    details_dict["Movie_name"]=movie_name
    # print(details_dict)
    data= soup.findAll("ul",class_="ipc-metadata-list ipc-metadata-list--dividers-all ipc-metadata-list--base")
    # print(data)
    for i in data:
        f=i.findAll('li',class_="ipc-metadata-list__item")
        # print(f)
        for fi in f:
            if "Country" in fi.text:
                country=fi.find('div',class_="ipc-metadata-list-item__content-container").text
                # print(country)
            elif "Language" in fi.text:
                language=fi.findAll('a')
                # print(language)
            # elif "poster_image_url" in fi.text:
                # poster_image_url=fi.find("div",class_="ipc-lockup-overlay-screen").text
                for l in language:
                    # print(l.text)
                    details_dict["language"]=l.text
                    details_dict["country"]=country
                    # details_dict["poster_image_url"]=poster_image_url
                # print(details_dict)
    Genres=soup.find("div",class_="ipc-chip-list GenresAndPlot__GenresChipList-cum89p-4 gtBDBL").text
    # print(Genres)
    runtime=soup.find("span",class_="ipc-inline-list__item")
    print(runtime)
    details_dict["runtime"]=runtime
    details_dict["Genres"]=Genres
    # print(details_dict)
    director=soup.find("li",class_="ipc-metadata-list__item").a.text
    # print(director)
    details_dict["director"]=director
    # print(details_dict)
    with open("web_task4.json","w")as file:
        json.dump(details_dict,file,indent=4)
d=scrape_movie_details()

# <li role="presentation" class="ipc-inline-list__item">2h 2min</li>
# ipc-metadata-list--item__content-container