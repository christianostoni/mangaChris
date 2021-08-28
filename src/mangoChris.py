from bs4 import BeautifulSoup
import requests

def manga_downloader(titolo):
    
    h = 1
    i = 0
    e = 1
    simple_url = 'https://beta.mangaeden.com'
    base_url = "https://beta.mangaeden.com/it/it-directory/?title="
    titolo = titolo.replace(" ", "+")
    url = base_url + titolo

    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    manga_list = soup.find(id='mangaList')

    openManga = manga_list.find_all(class_='openManga')
    closedManga = manga_list.find_all(class_='closedManga')

    titolo_array = []
    link_array = []
    for link in openManga:
        link = link.get('href')
        link_array.append(link)

    for titolo in openManga:
        titolo = titolo.get_text()
        titolo_array.append(titolo)

    for link in closedManga:
        link = link.get('href')
        link_array.append(link)

    for titolo in closedManga:
        titolo = titolo.get_text()
        titolo_array.append(titolo)

    if len(link_array) == 0:
        print('nessun manga trovato')
        return 0

    print("cosa vuoi vedere? :)")
    for titolo in titolo_array:
        print(i, titolo_array[i])
        i = i + 1

    scelta = int(input("digita il numero del manga che vuoi leggere: "))
    link_scelto = link_array[scelta]
    manga_url = simple_url + link_scelto

    capitolo = input('seleziona il volue che vuoi scaricare: ')
    percorso = input('seleziona il percorso della cartella nel quale scaricare il manga: ')

    capitolo_url = manga_url+capitolo

    prima_pagina_capitolo_url = capitolo_url+"/"+str(h)


    for e in range(1000):
        #primo link
        url = capitolo_url + "/" + str(h)
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')

        #secondo link
        h = int(h) + 1
        url2 = capitolo_url + "/" + str(h)
        r2 = requests.get(url2)
        soup2 = BeautifulSoup(r2.content, 'html.parser')
        if soup == soup2:
             break

        #download immagini
        mainImg = soup2.find(id='mainImg')
        src = mainImg.get('src')
        link_immagine = 'https:'+src
        response = requests.get(link_immagine, headers={
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0 Safari/537.36'
        })
        f = open(percorso + "\image" + str(e) + ".jpg", "wb")
        f.write(response.content)
        f.close()
        print('download successfull')
        e = e + 1
    print('finito')
    print('sviluppato da chistian ostoni')
    print("per favore se hai tempo dai un'occhiatina al mio github")
    print("https://github.com/christianostoni")

print('\n\t\tbenvenuti su mangoChris\t\t')
titolo = input('inserisci il nome del manga che desideri scaricare: ')
manga_downloader(titolo)
