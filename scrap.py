import requests
import sqlite3
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime




# region diccionarios

########FOTOS

#DICCIONARIO CON LAS URL DE CADA EQUIPO
urlTeamsLaligaFotos = {
    0: "atletico-madrid/startseite/verein/13/saison_id/2020",
    1: "fc-barcelona/startseite/verein/131/saison_id/2020",
    2: "real-madrid/startseite/verein/418/saison_id/2020",
    3: "fc-sevilla/startseite/verein/368/saison_id/2020",
    4: "real-sociedad-san-sebastian/startseite/verein/681/saison_id/2020",
    5: "fc-villarreal/startseite/verein/1050/saison_id/2020",
    6: "fc-valencia/startseite/verein/1049/saison_id/2020",
    7: "athletic-bilbao/startseite/verein/621/saison_id/2020",
    8: "real-betis-sevilla/startseite/verein/150/saison_id/2020",
    9: "fc-getafe/startseite/verein/3709/saison_id/2020",
    10: "fc-granada/startseite/verein/16795/saison_id/2020",
    11: "celta-vigo/startseite/verein/940/saison_id/2020",
    12: "ud-levante/startseite/verein/3368/saison_id/2020",
    13: "deportivo-alaves/startseite/verein/1108/saison_id/2020",
    14: "ca-osasuna/startseite/verein/331/saison_id/2020",
    15: "sd-eibar/startseite/verein/1533/saison_id/2020",
    16: "real-valladolid/startseite/verein/366/saison_id/2020",
    17: "sd-huesca/startseite/verein/5358/saison_id/2020",
    18: "cadiz-cf/startseite/verein/2687/saison_id/2020",
    19: "fc-elche/startseite/verein/1531/saison_id/2020"

}
#DICCIONARIO CON LOS NOMBRES DE LOS EQUIPOS
nombreEquiposFotos={

    0: "ATLETICO",
    1: "BARCELONA",
    2: "REAL MADRID",
    3: "SEVILLA",
    4: "REAL SOCIEDAD",
    5: "VILLARREAL",
    6: "VALENCIA",
    7: "ATHLETIC",
    8: "BETIS",
    9: "GETAFE",
    10: "GRANADA",
    11: "CELTA",
    12: "LEVANTE",
    13: "ALAVES",
    14: "OSASUNA",
    15: "EIBAR",
    16: "VALLADOLID",
    17: "HUESCA",
    18: "CADIZ",
    19: "ELCHE"



}


####NOTICIAS
nombreEquiposNoticias={

    0: "ATLETICO",
    1: "BARCELONA",
    2: "REAL MADRID",
    3: "SEVILLA",
    4: "REAL SOCIEDAD",
    5: "VILLARREAL",
    6: "VALENCIA",
    7: "ATHLETIC",
    8: "BETIS",
    9: "GETAFE",
    10: "GRANADA",
    11: "CELTA",
    12: "LEVANTE",
    13: "ALAVES",
    14: "OSASUNA",
    15: "EIBAR",
    16: "VALLADOLID",
    17: "HUESCA",
    18: "CADIZ",
    19: "ELCHE",
    20: "GENERAL"

}
linkEquiposNoticias={

    0: "https://www.marca.com/futbol/atletico.html?intcmp=MENUESCU&s_kw=atletico",
    1: "https://www.marca.com/futbol/barcelona.html?intcmp=MENUESCU&s_kw=barcelona",
    2: "https://www.marca.com/futbol/real-madrid.html?intcmp=MENUESCU&s_kw=realmadrid",
    3: "https://www.marca.com/futbol/sevilla.html?intcmp=MENUESCU&s_kw=sevilla",
    4: "https://www.marca.com/futbol/real-sociedad.html?intcmp=MENUESCU&s_kw=realsociedad",
    5: "https://www.marca.com/futbol/villarreal.html?intcmp=MENUESCU&s_kw=villarreal",
    6: "https://www.marca.com/futbol/valencia.html?intcmp=MENUESCU&s_kw=valencia",
    7: "https://www.marca.com/futbol/athletic.html?intcmp=MENUESCU&s_kw=athletic",
    8: "https://www.marca.com/futbol/betis.html?intcmp=MENUESCU&s_kw=betis",
    9: "https://www.marca.com/futbol/getafe.html?intcmp=MENUESCU&s_kw=getafe",
    10: "https://www.marca.com/futbol/granada.html?intcmp=MENUESCU&s_kw=granada",
    11: "https://www.marca.com/futbol/celta.html?intcmp=MENUESCU&s_kw=celta",
    12: "https://www.marca.com/futbol/levante.html?intcmp=MENUESCU&s_kw=levante",
    13: "https://www.marca.com/futbol/alaves.html?intcmp=MENUESCU&s_kw=alaves",
    14: "https://www.marca.com/futbol/osasuna.html?intcmp=MENUESCU&s_kw=osasuna",
    15: "https://www.marca.com/futbol/eibar.html?intcmp=MENUESCU&s_kw=eibar",
    16: "https://www.marca.com/futbol/valladolid.html?intcmp=MENUESCU&s_kw=valladolid",
    17: "https://www.marca.com/futbol/huesca.html?intcmp=MENUESCU&s_kw=huesca",
    18: "https://www.marca.com/futbol/cadiz.html?intcmp=MENUESCU&s_kw=cadiz",
    19: "https://www.marca.com/futbol/elche.html?intcmp=MENUESCU&s_kw=elche",
    20: "https://www.marca.com/futbol/primera-division.html?intcmp=MENUMIGA&s_kw=laliga-santander"

}

####TABLAS
#DICCIONARIO CON LOS NOMBRES DE LOS EQUIPOS
nombreEquiposTablas={

    0: "ATLETICO",
    1: "BARCELONA",
    2: "REAL MADRID",
    3: "SEVILLA",
    4: "REAL SOCIEDAD",
    5: "VILLARREAL",
    6: "VALENCIA",
    7: "ATHLETIC",
    8: "BETIS",
    9: "GETAFE",
    10: "GRANADA",
    11: "CELTA",
    12: "LEVANTE",
    13: "ALAVES",
    14: "OSASUNA",
    15: "EIBAR",
    16: "VALLADOLID",
    17: "HUESCA",
    18: "CADIZ",
    19: "ELCHE"



}
nombreEquipos = {

    0: "\nA T L E T I C O\n",
    1: "\nB A R C E L O N A\n",
    2: "\nR E A L   M A D R I D\n",
    3: "\nS E V I L L A \n",
    4: "\nR E A L   S O C I E D A D\n",
    5: "\nV I L L A R R E A L\n",
    6: "\nV A L E N C I A\n",
    7: "\nA T H L E T I C\n",
    8: "\nB E T I S\n",
    9: "\nG E T A F E\n",
    10: "\nG R A N A D A\n",
    11: "\nC E L T A\n",
    12: "\nL E V A N T E\n",
    13: "\nA L A V E S\n",
    14: "\nO S A S U N A\n",
    15: "\nE I B A R\n",
    16: "\nV A L L A D O L I D\n",
    17: "\nH U E S C A\n",
    18: "\nC A D I Z\n",
    19: "\nE L C H E\n"

}
#Diccionario con los links
equipos_estadisticasTablas = {
    0: "https://resultados.as.com/resultados/ficha/equipo/atletico/42/2020/estadisticas/primera/",
    1: "https://resultados.as.com/resultados/ficha/equipo/barcelona/3/2020/estadisticas/primera/",
    2: "https://resultados.as.com/resultados/ficha/equipo/real_madrid/1/2020/estadisticas/primera/",
    3: "https://resultados.as.com/resultados/ficha/equipo/sevilla/53/2020/estadisticas/primera/",
    4: "https://resultados.as.com/resultados/ficha/equipo/r_sociedad/16/2020/estadisticas/primera/",
    5: "https://resultados.as.com/resultados/ficha/equipo/villarreal/19/2020/estadisticas/primera/",
    6: "https://resultados.as.com/resultados/ficha/equipo/valencia/17/2020/estadisticas/primera/",
    7: "https://resultados.as.com/resultados/ficha/equipo/athletic/5/2020/estadisticas/primera/",
    8: "https://resultados.as.com/resultados/ficha/equipo/betis/171/2020/estadisticas/primera/",
    9: "https://resultados.as.com/resultados/ficha/equipo/getafe/172/2020/estadisticas/primera/",
    10: "https://resultados.as.com/resultados/ficha/equipo/granada/347/2020/estadisticas/primera/",
    11: "https://resultados.as.com/resultados/ficha/equipo/celta/6/2020/estadisticas/primera/",
    12: "https://resultados.as.com/resultados/ficha/equipo/levante/136/2020/estadisticas/primera/",
    13: "https://resultados.as.com/resultados/ficha/equipo/alaves/4/2020/estadisticas/primera/",
    14: "https://resultados.as.com/resultados/ficha/equipo/osasuna/13/2020/estadisticas/primera/",
    15: "https://resultados.as.com/resultados/ficha/equipo/eibar/108/2020/estadisticas/primera/",
    16: "https://resultados.as.com/resultados/ficha/equipo/valladolid/18/2020/estadisticas/primera/",
    17: "https://resultados.as.com/resultados/ficha/equipo/huesca/864/2020/estadisticas/primera/",
    18: "https://resultados.as.com/resultados/ficha/equipo/cadiz/91/2020/estadisticas/primera/",
    19: "https://resultados.as.com/resultados/ficha/equipo/elche/121/2020/estadisticas/primera/"

}
urlTeamsLaliga = {
    0: "atletico-madrid/startseite/verein/13/saison_id/2020",
    1: "fc-barcelona/startseite/verein/131/saison_id/2020",
    2: "real-madrid/startseite/verein/418/saison_id/2020",
    3: "fc-sevilla/startseite/verein/368/saison_id/2020",
    4: "real-sociedad-san-sebastian/startseite/verein/681/saison_id/2020",
    5: "fc-villarreal/startseite/verein/1050/saison_id/2020",
    6: "fc-valencia/startseite/verein/1049/saison_id/2020",
    7: "athletic-bilbao/startseite/verein/621/saison_id/2020",
    8: "real-betis-sevilla/startseite/verein/150/saison_id/2020",
    9: "fc-getafe/startseite/verein/3709/saison_id/2020",
    10: "fc-granada/startseite/verein/16795/saison_id/2020",
    11: "celta-vigo/startseite/verein/940/saison_id/2020",
    12: "ud-levante/startseite/verein/3368/saison_id/2020",
    13: "deportivo-alaves/startseite/verein/1108/saison_id/2020",
    14: "ca-osasuna/startseite/verein/331/saison_id/2020",
    15: "sd-eibar/startseite/verein/1533/saison_id/2020",
    16: "real-valladolid/startseite/verein/366/saison_id/2020",
    17: "sd-huesca/startseite/verein/5358/saison_id/2020",
    18: "cadiz-cf/startseite/verein/2687/saison_id/2020",
    19: "fc-elche/startseite/verein/1531/saison_id/2020"

}







# endregion

# region bases de datos

con = sqlite3.connect('equipos.db')
cursorObj=con.cursor()


#borra las tablas si tenian algo

cursorObj.execute('DROP table if exists api_asistencias')
cursorObj.execute('DROP table if exists api_clasificacion')
cursorObj.execute('DROP table if exists api_fotos')
cursorObj.execute('DROP table if exists api_goleadores_equipos')
cursorObj.execute('DROP table if exists api_goles_encajados')
cursorObj.execute('DROP table if exists api_noticias')
cursorObj.execute('DROP table if exists api_pichichi')


try:
    ############FOTOS
    cursorObj.execute('''CREATE TABLE api_fotos(Equipo TEXT, Nombre TEXT, LinkFoto TEXT,id INT)''')  # comentar una vez ejecutadi
    ############NOTICIAS
    cursorObj.execute(
        '''CREATE TABLE api_noticias(Titulo TEXT, Foto TEXT, Contenido TEXT, Equipo TEXT,id INT)''')  # comentar una vez creadas las tablas
    ############TABLAS
    cursorObj.execute('''CREATE TABLE api_clasificacion (Equipo TEXT, Puntos INT,id INT)''')  # comentar una vez ejecutado
    cursorObj.execute('''CREATE TABLE api_pichichi (Nombre TEXT, Goles INT,id INT)''')  # comentar una vez ejecutado
    cursorObj.execute('''CREATE TABLE api_asistencias (Nombre TEXT, Asistencias INT,id INT)''')  # comentar una vez ejecutado
    cursorObj.execute(
        '''CREATE TABLE api_goles_encajados (Nombre TEXT, Goles_encajados INT,id INT)''')  # comentar una vez ejecutado
    cursorObj.execute(
        '''CREATE TABLE api_goleadores_equipos (Equipo TEXT, Nombre TEXT, Goles INT,id INT)''')  # comentar una vez ejecutado
    cursorObj.execute(
        '''CREATE TABLE api_equipos(Equipo TEXT, Jugadores INT, EdadMedia INT, ValorTotal FLOAT, ValorMedio FLOAT, Actualizacion TEXT,id INT)''')
    cursorObj.execute(
        '''CREATE TABLE api_jugadores(jugador TEXT, edad INT, pais TEXT, equipos TEXT, dorsal INT, posicion TEXT, precio FLOAT, actualizacion TEXT,id INT)''')

    con.commit()  # comentar una vez ejecutado

except:
    con.commit()



#PASAR A DB FOTOS
def pasarAdbFotos(equipo,jugador,linkfoto):


    i=0
    while i < len(equipo):
        con.execute('''INSERT INTO api_fotos(Equipo,Nombre,LinkFoto,id) VALUES(?, ?, ?, ?)''',
                    (str(equipo[i]), str(jugador[i]), str(linkfoto[i]),int(i)))

        con.commit()
        i=i+1;

    print("Informacion migrada a la DB")
#PASAR A DB NOTICIAS
def pasarAdbNoticias(titulo,foto,contenido,equipo):

    i=0
    while i < len(titulo):
        con.execute('''INSERT INTO api_noticias(titulo,Foto,Contenido,Equipo,id) VALUES(?, ?, ?, ?, ?)''',
                    (str(titulo[i]), str(foto[i]), str(contenido[i]), str(equipo[i]),int(i)))

        con.commit()
        i=i+1;

    print("Informacion migrada a la DB")
#PASAR A DB TABLAS
def pasar_DB1(columna1, columna2, tabla, nombre_columna1, nombre_columna2):

    i = 0


    while i < len(columna1):
        con.execute(f'INSERT INTO {tabla}({nombre_columna1},{nombre_columna2},id) VALUES(?, ?, ?)',
                    (str(columna1[i]), int(columna2[i]),int(i)))

        con.commit()
        i = i + 1;

    print("Informacion migrada a la DB")
#goleadores equipo
def pasar_DB2(equipo, nombre, tabla, columna,nombre_columna):

    i = 0

    while i < len(equipo):
        con.execute(f'INSERT INTO {tabla} (Equipo,Nombre,{nombre_columna},id) VALUES(?, ?, ?, ?)',
                    (str(equipo[i]), str(nombre[i]), int(columna[i]),int(i)))

        con.commit()
        i = i + 1;

    print("Informacion migrada a la DB")

def pasarAdbJugadores(players,price,dorsales,paises,edades,posiciones,equipo,actualizacion):

    numero = cursorObj.execute('SELECT COUNT(pais) from api_jugadores')
    j = cursorObj.fetchone()[0]
    i=0
    while i < len(players):
        con.execute('''INSERT INTO api_jugadores(jugador,edad,pais,equipos,dorsal,posicion,precio,actualizacion,id) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                  (players[i], edades[i], paises[i], equipo[i], dorsales[i], posiciones[i], price[i],actualizacion,int(j)))
        con.commit()
        i=i+1;
        j=j+1;
    print("Informacion migrada a la DB")

def pasarAdbMedias(resultado,num,edad,total,valor,actualizacion,id):

    con.execute('''INSERT INTO api_equipos(Equipo,Jugadores,EdadMedia,ValorTotal,ValorMedio,Actualizacion,id) VALUES(?, ?, ?, ?, ?, ?, ?)''',
                  (resultado,num,edad,total,valor,actualizacion,id))
    con.commit()

    print("Informacion migrada a la DB")



    print("Informacion migrada a la DB")
#c.close()
# endregion

# region fotos

#variables
urlTransfermark = "https://www.transfermarkt.es/"
PlayersList = list()
linklist = list()
listaFotos = list()
listaEquipos = list()


#funciones

def scrapeofoto(indice,links,nombres,listafotos):

    url=links[indice]

    header = {"User-Agent": "Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11"}

    pageTree = requests.get(url, headers=header)
    pageSoup = BeautifulSoup(pageTree.content, 'html.parser')

    fotoscarnet=pageSoup.find_all("div",{"class": "dataBild"})[0].find_all("img")

    try:
        fotos=pageSoup.find_all("div",{"class": "galerie-content"})[0].find_all("img")
        listafotos.append(fotos[0]['data-src'])

    except:
        listafotos.append(fotoscarnet[0]['src'])
def scrapeoFotos(url, players,links,equipo,listaequipos):
    header = {"User-Agent": "Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11"}

    pageTree = requests.get(url, headers=header)
    pageSoup = BeautifulSoup(pageTree.content, 'html.parser')

    player = pageSoup.find_all("td", {"itemprop": "athlete"})

    link = pageSoup.select("td[class='hauptlink']",href=True)

    for i in link:

        links.append("https://www.transfermarkt.es"+i.find_all("a")[0]['href'])


    for i in player:
        players.append(i.text)
        listaEquipos.append(nombreEquiposFotos[equipo])

#Main

for clave in urlTeamsLaligaFotos:

    valor= nombreEquiposFotos[clave]
    print('.')
    scrapeoFotos(urlTransfermark + urlTeamsLaligaFotos[clave], PlayersList,linklist,clave,listaEquipos)

cont=0
for i in PlayersList:
    scrapeofoto(cont, linklist, PlayersList,listaFotos)
    print(i+"--"+listaEquipos[cont]+"---"+listaFotos[cont])
    cont= cont+1

pasarAdbFotos(listaEquipos,PlayersList,listaFotos)


# endregion

# region noticias
#VARIABLES

titulos=list()
fotos=list()
contenidos=list()
equipos=list()



#FUNCIONES
def scrapeonoticia(url, titulo,foto,contenido,cantidad,equipolista,equipo):
    header = {"User-Agent": "Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11"}

    pageTree = requests.get(url, headers=header)
    pageSoup = BeautifulSoup(pageTree.content, 'html.parser')
    links = list()

    link = pageSoup.select("li[class='content-item']",href=True)


#saco los links de las noticias, si generan algun error entonces no los coge
    cont=0
    i=0

    while cont<cantidad:
        try:
            print("noticias de " + equipo)

            links.append(link[i].find_all("a")[0]['href']) #append del link
            pageTree2 = requests.get(links[i], headers=header)
            pageSoup2 = BeautifulSoup(pageTree2.content, 'html.parser')

            #---prueba titulos
            #print(pageSoup2.find_all("h1", {"class": "ue-c-article__headline"})[0].text)
            titulos.append(pageSoup2.find_all("h1", {"class": "ue-c-article__headline"})[0].text)

            #---prueba fotos
            try:
                fotos.append(pageSoup2.find_all("img", {"class": "ue-c-article__media--image"})[0]['src'])
                # print(pageSoup.find_all("img", {"class": "ue-c-article__media--image"})[0]['src'])
            except:
                fotos.append("https://e00-marca.uecdn.es/assets/v21/img/destacadas/marca__logo-generica.jpg")

            #---prueba contenido
            contenido.append(pageSoup2.find_all("div", {"class": "ue-c-article__body"})[0].text)

            #print(pageSoup2.find_all("div", {"class": "ue-c-article__body"})[0].text)

            equipolista.append(equipo)#append del equipo

            cont+=1
            i+=1

        except:
            print("pasando")
            i+=1


#MAIN
#LLAMADA A LA FUNCION DE SCRAPEO PARA CADA EQUIPO
for i in range(21):

    scrapeonoticia(linkEquiposNoticias[i], titulos, fotos, contenidos,5, equipos, nombreEquiposNoticias[i])

pasarAdbNoticias(titulos,fotos,contenidos,equipos)


# endregion

# region tablas

#FUNCIONES

def scrapeoTablas(url,listajugadores,listadatos,cantidad):




    page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0'})
    soup = BeautifulSoup(page.content, 'html.parser')

    jugador=soup.find_all('span',class_='name')
    dato=soup.find_all('td',class_='cantidad')

    cont=0;



    for i in jugador:
        if cont==cantidad:
            break;
        listajugadores.append(i.text)
        cont=cont+1;
    cont=0;
    for i in dato:
        if cont==cantidad:
            break;
        if cont==0:
            listadatos.append(i.text[0:2])
        else:
            listadatos.append(i.text)

        cont=cont+1;

def est_equipo(numequipo,listajugs,listagoles,listaequipos):
    page = requests.get(equipos_estadisticasTablas[numequipo], headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0'})
    soup = BeautifulSoup(page.content, 'html.parser')

    jugador=soup.find_all('span',class_='player-inline')
    goles=soup.find_all('tbody')[1].find_all('td')
    goleadoresequipo1=list()
    golescont=0;
    aux=list()

    for i in range(int(len(goles)/3)):
        aux.append(list());
        aux[i].append(jugador[i].text)
        aux[i].append(int(goles[golescont].text))
        golescont=golescont+3;
    goleadoresequipo1.append(sorted(aux, key=lambda x: x[1],reverse=True))


    cont=0
    for i in range(5):
        #print(goleadoresequipo1[0][i][0])
        listajugs.append(goleadoresequipo1[0][i][0])
        listagoles.append(goleadoresequipo1[0][i][1])
        listaequipos.append(nombreEquiposTablas[numequipo])


#MAIN

# region estadisticas individuales de equipo

jugadores=list()
goles=list()
equipos=list()


for i in range(20):
    est_equipo(i, jugadores, goles, equipos)

for i in range(len(jugadores)):
    print(f'{jugadores[i]}--{goles[i]}--{equipos[i]}')





pasar_DB2(equipos,jugadores,"api_goleadores_equipos",goles,"Goles")



# endregion

# region generales


#scrapeo clasificacion

equipos=list()
ptos=list()
golesf=list()
golesc=list()

page = requests.get('https://resultados.as.com/resultados/futbol/primera/', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0'})
soup = BeautifulSoup(page.content, 'html.parser')


equipo = soup.find_all('a', class_='nombre-equipo')
puntos = soup.find_all('td', class_='destacado')




for i in puntos:
    ptos.append(i.text)


for i in equipo:
    equipos.append(i.text.rstrip('\n')[1:])


for i in range(20):
    print(f'{i+1}-     {equipos[i]}      {ptos[i]}')


pasar_DB1(equipos,ptos,"api_clasificacion","Equipo","Puntos")





#goleadores

goleadores=list()
goles=list()
scrapeoTablas('https://resultados.as.com/resultados/futbol/primera/2020_2021/ranking/jugadores/goles/',goleadores,goles,20)

print("TABLA DE GOLEADORES")
for i in range(20):
    print(f' {i+1}- {goleadores[i]}  {goles[i]} ')

pasar_DB1(goleadores,goles,"api_pichichi","Nombre","Goles")


#ASISTENCIAS

asistentes=list()
asistencias=list()
scrapeoTablas('https://resultados.as.com/resultados/futbol/primera/2020_2021/ranking/jugadores/asistencias-de-gol/',asistentes,asistencias,20)

print("TABLA DE ASISTENCIAS")
for i in range(20):
    print(f' {i+1}- {asistentes[i]}  {asistencias[i]} ')

pasar_DB1(asistentes,asistencias,"api_asistencias","Nombre","Asistencias")

#GOLES ENCAJADOS


porteros=list()
encajados=list()
scrapeoTablas('https://resultados.as.com/resultados/futbol/primera/2020_2021/ranking/jugadores/goles-encajados/',porteros,encajados,20)

print("TABLA DE GOLES ENCAJADOS")
for i in range(20):
    print(f' {i+1}- {porteros[i]}  {encajados[i]} ')


pasar_DB1(porteros,encajados,"api_goles_encajados","Nombre","Goles_encajados")



# endregion

# endregion

#region jugadores


def current_date_format(date):
    months = ("01", "02", "03", "04", "05", "06","07", "08", "09", "10", "11", "12")
    day = date.day
    month = months[date.month - 1]
    year = date.year
    messsage = "{}-{}-{}".format(day, month, year)

    return messsage



def scrapeo(url, players, prices, dorsales, paises, edades, posiciones, equipos):
    header = {"User-Agent": "Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11"}
    """"
    Mapeo de la página para ello se crea priero el 
    árbol de la página usando los headers originales del navegador
    """
    pageTree = requests.get(url, headers=header)
    pageSoup = BeautifulSoup(pageTree.content, 'html.parser')

    equipo = "local"
    aux = 0
    now = datetime.now()
    actualizacion = current_date_format(now)

    # Cuando la función ha encontrado los objetos que buscamos los añade a la lista de jugadores

    for i in pageSoup.find_all("td", {"itemprop": "athlete"}):
        players.append(i.text)
        aux += 1
        resultado="local"

    for i in pageSoup.find_all("td", {"class": "rechts hauptlink"}):
        valor=i.text

        if (valor.find("€")==-1):
            valor2=0
            prices.append(valor2)

        else:
            if (valor.find(",") == -1):
                split = valor.split(" ")
                valor = split[0]
                valor2 = float(valor)/1000
                prices.append(valor2)
            else:
                split = valor.split(',')
                valor = split[0]
                valor2 = int(valor)
                prices.append(valor2)





    for i in pageSoup.find_all("div", {"class": "rn_nummer"}):

        dorsal=i.text

        if dorsal=="-":
            dorsal2=0
            dorsales.append(dorsal2)
        else:
            dorsales.append(int(dorsal))





    for i in pageSoup.find_all(lambda tag: tag.name == 'td' and tag.get('class') == ['zentriert']):
        img = i.find('img', alt=True)
        if img is not None:
            paises.append(img['alt'])

    for i in pageSoup.find_all(lambda tag: tag.name == 'td' and tag.get('class') == ['zentriert']):

        if (len(i.text) > 3):
            edad=i.text[12:14]
            edad2=int(edad)
            edades.append(edad2)

    for i in pageSoup.find_all(lambda tag: tag.name == 'table' and tag.get('class') == ['inline-table']):
        lenght = len(i.text)
        if (i.text[lenght - 7:lenght] == "Portero"):
            text = i.text[lenght - 7:lenght]
            posiciones.append(text)
        if (i.text[lenght - 15:lenght] == "Defensa central"):
            text = i.text[lenght - 15:lenght]
            posiciones.append(text)
        if (i.text[lenght - 17:lenght] == "Lateral izquierdo"):
            text = i.text[lenght - 17:lenght]
            posiciones.append(text)
        if (i.text[lenght - 15:lenght] == "Lateral derecho"):
            text = i.text[lenght - 15:lenght]
            posiciones.append(text)
        if (i.text[lenght - 6:lenght] == "Pivote"):
            text = i.text[lenght - 6:lenght]
            posiciones.append(text)
        if (i.text[lenght - 11:lenght] == "Mediocentro"):
            text = i.text[lenght - 11:lenght]
            posiciones.append(text)
        if (i.text[lenght - 20:lenght] == "Mediocentro ofensivo"):
            text = i.text[lenght - 20:lenght]
            posiciones.append(text)
        if (i.text[lenght - 17:lenght] == "Extremo izquierdo"):
            text = i.text[lenght - 17:lenght]
            posiciones.append(text)
        if (i.text[lenght - 15:lenght] == "Extremo derecho"):
            text = i.text[lenght - 15:lenght]
            posiciones.append(text)
        if i.text[lenght - 10:lenght] == "Mediapunta":
            text = i.text[lenght - 10:lenght]
            posiciones.append(text)
        if i.text[lenght - 16:lenght] == "Delantero centro":
            text = i.text[lenght - 16:lenght]
            posiciones.append(text)
        if i.text[lenght - 18:lenght] == "Interior izquierdo":
            text = i.text[lenght - 18:lenght]
            posiciones.append(text)
        if i.text[lenght - 16:lenght] == "Interior derecho":
            text = i.text[lenght - 16:lenght]
            posiciones.append(text)

    for i in pageSoup.find_all(lambda tag: tag.name == 'div' and tag.get('class') == ['dataName']):
        equipo = i.text
        equipo=equipo.rstrip()
        resultado=equipo[2:len(equipo)]

    for i in range(aux):
        equipos.append(resultado)

    d = (
    {"Players": players, "Dorsal": dorsales, "Valor": prices, "Edad": edades, "Pais": paises, "Posicion": posiciones,
     "Equipo": equipos, "Actualizacion":actualizacion})


    df = pd.DataFrame(data=d)

    print(df)

    pasarAdbJugadores(players,prices,dorsales,paises,edades,posiciones,equipos,actualizacion)

PlayerList = list()
ValuesList = list()
DorsalList = list()
PaisList = list()
EdadList = list()
PosicionList = list()
EquipoList = list()

for clave in urlTeamsLaliga:
    valor = nombreEquipos[clave]
    print(valor)
    scrapeo(urlTransfermark + urlTeamsLaliga[clave], PlayerList, ValuesList, DorsalList, PaisList, EdadList,
            PosicionList, EquipoList)
    PlayerList = list()
    ValuesList = list()
    DorsalList = list()
    PaisList = list()
    EdadList = list()
    PosicionList = list()
    EquipoList = list()

#endregion

#region medias
def scrapeo_medias(url):

    numero = cursorObj.execute('SELECT COUNT(Equipo) from api_equipos')
    colls = cursorObj.fetchone()[0]

    header = {"User-Agent": "Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11"}
    """"
    Mapeo de la página para ello se crea priero el 
    árbol de la página usando los headers originales del navegador
    """
    pageTree = requests.get(url, headers=header)
    pageSoup = BeautifulSoup(pageTree.content, 'html.parser')

    equipo = "local"
    resultado="local"

    aux =0
    now = datetime.now()
    actualizacion = current_date_format(now)
    totalValor=0
    totalEdad=0
    mediaEdad=0
    mediaValor=0

    # Cuando la función ha encontrado los objetos que buscamos los añade a la lista de jugadores


    for i in pageSoup.find_all("td", {"class": "rechts hauptlink"}):
        valor=i.text

        if (valor.find("€")==-1):
            valor2=0


        else:
            if (valor.find(",") == -1):
                split = valor.split(" ")
                valor = split[0]
                valor2 = float(valor)/1000
                totalValor+=valor2

            else:
                split = valor.split(',')
                valor = split[0]
                valor2 = int(valor)
                totalValor+=valor2
        aux+=1;

    mediaValor=totalValor/aux




    for i in pageSoup.find_all(lambda tag: tag.name == 'td' and tag.get('class') == ['zentriert']):

        if (len(i.text) > 3):
            edad=i.text[12:14]
            edad2=int(edad)
            totalEdad+=edad2

    mediaEdad=totalEdad/aux;


    for i in pageSoup.find_all(lambda tag: tag.name == 'div' and tag.get('class') == ['dataName']):
        equipo = i.text
        equipo = equipo.rstrip()
        resultado = equipo[2:len(equipo)]

    d = ({"Equipo": resultado,"Jugadores":aux, "Edad media": mediaEdad, "Valor total":totalValor, "Valor medio": mediaValor, "Actualizacion":actualizacion})

    df = pd.DataFrame(data=d, index=[0])


    print(df)

    pasarAdbMedias(resultado,aux,mediaEdad,totalValor,mediaValor,actualizacion,colls)

for clave in urlTeamsLaliga:

    scrapeo_medias(urlTransfermark + urlTeamsLaliga[clave])


#endregion