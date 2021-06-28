![Portada]( https://user-images.githubusercontent.com/64830147/123535463-2edd9480-d724-11eb-895e-d09953fb0d7e.png)
*Este repositorio contiene el tercer proyecto del Bootcamp: Data Analytics de Iron Hack. El objetivo es la identificación de la ubicación óptima de una nueva empresa dadas ciertas condiciones (por ejemplo, el 30% de los empleados tiene al menos un hijo). Usando para ello, una base de datos con mas de 18.000 empresas y la API de Foursquare, para acceder a la información de las diferentes localizaciones, a fin de establecer la ubicación que satisfaga tantas variables y empleados como sea posible.*

# Descripción 🏭
![Descripción](https://user-images.githubusercontent.com/64830147/123536767-8ed83900-d72c-11eb-950b-d4e07fec7f27.png)

La empresa **IronGames** cuya sede principal está en China quiere dar el salto internacional y expandir sus productos, abriendo una nueva oficina en un país donde la industria de los videojuegos este en auge y obtenga altos ingresos. 

Además, la empresa para facilitar y mantener contentos, a la plantilla destinada a la nueva sede (la cual se calcula que aproximadamente será de unos 85 empleados) ha realizado una encuesta para determinar la mejor ubicación de la oficina, en base a sus necesidades y preferencias en cuanto a sitios cercanos los cuales se resumen en:

-	Transporte: Aeropuertos o servicios de transporte a larga distancia para los Account Managers que realizan muchos viajes. Estaciones de autobuses para desplazamientos rutinarios.
-	Ocio: discotecas, Starbucks y restaurantes veganos. La edad de los trabajadores está entre 25 y 40 años. 
-	Colegios. El 30% de los empleados tiene al menos un hijo.
-	Veterinario. Para la mascota de la compañía.

# Índice de contenido 📎
-	3 jupyter notebooks diferenciados en la base de datos, api y visualización.
-	Documento py. con las funciones definidas para este proyecto.
-	Carpeta de imágenes.
-	Dataset de las oficinas seleccionadas.
- 2 jupyter notebooks con el contenido extra (api y visualización)

# Librerías utilizadas 📚
Durante este proyecto se emplearon las siguientes librerías:
-	Pandas
-	Requests
-	Os
-	Json
-	Math
-	Folium
-	Cartoframes
-	BeautifulSoup
-	Pymongo
-	Geopandas

*La documentación oficial se encuentra en el apartado de Link&Recursos*

# Metodología 🔎
A fin de seleccionar el país más adecuado, primero se realiza un análisis previo de los mercados que generan mayor ingreso y cubren más cuota en la industria de los videojuegos (para ello se ha empleado la técnica de webscrapping). Teniendo en cuenta que IronGames ya cuenta con sedes en China y quiere expandirse internacionalmente. 

Una vez seleccionado el país y la ciudad en este caso Nueva York, se procede al filtro y selección de las oficinas que se encuentran en la base de datos de “Companies”. Los criterios seguidos fueron:
-	País: USA
-	Ciudad: Nueva York
-	Categoría: Videojuegos
-	Capacidad: 80 a 150 empleados
-	Actual. Antigüedad mínima del año 2.000

Establecida la ubicación de la empresa, se realizan las pertinentes llamadas a la API de Foursquare en función a las variables anteriormente citadas.

Finalmente se procede a la visualización de la oficina y los 7 puntos extraídos del proceso anterior, mediante un mapa con Folium.

# Resultados ✅
*A continuación se procede al análisis de los resultados obtenidos; para la visualización de más gráficas véase el jupyter notebook 2 y 3.*

La oficina escogida es: **Livestream** situada en 636 Broadway, Nueva York.

![Mapa 1](https://user-images.githubusercontent.com/64830147/123536514-f7261b00-d72a-11eb-96fc-71c6d5bf0978.png)

La cual se encuentra:
-	A 4,69 kilómetros del servicio de transporte a larga distancia más cercano. “Bell Service”.
-	La estación de autobuses más cercanas se encuentra a 312 metros.
-	A 495 metros de la discoteca “Public Arts”.
-	El Starbucks más cercanos está a 485 metros y el restaurante vegano a “Beyond Sushi” a 470 metros.
-	Hay bastantes colegios, institutos y universidades por la zona el más cercano “Skillshare School” está a 403 metros.
-	Solo encontramos un veterinario en un radio de 500 metros “Cooper Square Veterinary Hospital” a 442 metros con respecto a la compañía.

![Mapa 2]( https://user-images.githubusercontent.com/64830147/123536721-59335000-d72c-11eb-9d73-23713d3a302f.png)

# Extra ⭐
*A continuación se procede a realizar el mismo estudio para la segunda opción barajeada por la empresa: las oficinas **Boonty**, siendo la distancia con respecto a LiveStream de 1,15 kilómetros*.

![Mapa 3](https://user-images.githubusercontent.com/64830147/123542555-7e36bb80-d74a-11eb-95fe-f93d62aa4792.png)

Las coordenadas de la oficina Boontys son las siguientes: 40.717248, -74.002662. Se encuentran a una distancia de:
- 4,43 kilómetros del servicio de transporte a larga distancia más cercano y 474 metros con respecto a la estación de autobuses.
- The Blond, la discoteca más cercana está a 311 metros.
- El Starbucks más cercano se encuentra a 383 metros y el restaurante vegano a 450 metros.
- A 417 metros se encuentra el colegio más cercano, aunque en un radio de 500 metros se encuentran bastantes.
- Encontramos dos veterinarios en la zona de los cuales el más próximo a las oficinas está a unos 259 metros.

![Mapa 4](https://user-images.githubusercontent.com/64830147/123596444-7cc0ce00-d7f2-11eb-83e8-fed64b341861.png)


# Links & Resources  🖇️
- [Pandas documentation](https://pandas.pydata.org)
- [Requests documentation](https://requests.readthedocs.io/en/master/)
- [Json documentation](https://docs.python.org/3/library/json.html)
- [Folium documentation](https://pypi.org/project/folium/)
- [List of video games markets by country](https://en.wikipedia.org/wiki/List_of_video_games_markets_by_country)
- [Función de la distancia](http://pythoninicios.blogspot.com/2016/03/como-calcular-la-distancia-entre-dos.html)
- [Foursquare API](https://developer.foursquare.com)