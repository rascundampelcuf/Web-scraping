---
title: "Dataset: Repositori de llibres de Ciència-Ficció de butxaca de la Casa del Libro"
author: "Gabriel Izquierdo i Mireia Olivella"
date: "10 d'abril del 2020"


## Context
L'objectiu d'aquesta pràctica es aconseguir un repositori de tots els llibres de Ciència-Ficció de butxaca que es troben a la pàgina Web: la Casa del Libro.  
Hem seleccionat de cada llibre la informació més rellevant. 


## Imatge identificativa
[LA CASA DEL LIBRO]
<a><img src="https://github.com/rascundampelcuf/Web-scraping/pdf/library.jpg"></a>


## Descripció
A continuació trobareu el projecte corresponent a la PRAC1 de l'assignatura de Tipologia i Cicle de Vida de les Dades. L'objectiu de l'activitat és la creació d'un dataset a partir de la web la Casa del Libro. 

El conjunt de dades escollit té com a finalitat doncs recollir informació de tots els llibres de Ciència-Ficció de butxaca de la pàgina la casadellibro.com, concretament dels llibres que es troben dins de la secció de literatura i narrativa en bolsillo, en l'apartat de Ciencia-Ficción en bolsillo. 
Les variables seleccionades han sigut: el títol del llibre, l'autor, la disponibilitat, la puntuació, el preu, i finalment el tipus de tapa. 



\newpage
## Contingut

Per cada llibre de la secció de Ciència-Ficció s'ha recollit la següent informació: 

* **Title**: títol del llibre.
* **Autor**: autor del llibre.  
* **Rate**: puntuació rebuda pels lectors.   
* **bookType**: tipus de llibre, segons el format podem trobar: llibres de tapa dura, tapa blanda i eBooks.
* **Price**: preu del llibre.  
* **Availability**: indica si el llibre està disponible mitjançant un operador booleà.

FALTA periode de temps de les dades + com s'ha recollit. 



## Agraïments
Les dades han estat recollides des de la pròpia pàgina de la Casa del Libro: https://www.casadellibro.com/libros/literatura/narrativa-en-bolsillo/ciencia-ficcion-en-bolsillo/121005001/p
Hem usat el llenguatge de programació Python i tècniques de *web Scraping usant Selenium*, per tal de poder extreure la informació. 


## Inspiració
El conjunt de dades extret ens permet obtenir un llistat de tots els llibres que té la web, on a més a més, podem accedir als diferents preus que té cada llibre segons el format en el qual es ven, entre altre informació rellevant com, la disponibilitat i la puntuació que han obtingut dels lectors. 

Aquesta informació podria usar-se dins la mateixa empresa per poder obtenir un major control dels seus llibres, per poder saber els que tenen majors puntuacions, les disponibilitats... I d'aquesta manera elaborar també models predictius, com ara arbres de decisió, per tal de predir el tipus de llibre que més agrada, que més es venen, i en definitiva, oferir als clients productes més personalitzats. 


## Licència
La llicència escollida pel conjunt de dades ha sigut CC BY-SA 4.0 License. Els motius de l'elecció són els següents:
- S'ha de mantenir el nom del creador del conjunt de dades, i especificar els canvis fets respecte a la versió original.
-Es permet un ús comercial. Això permetria que una empresa utilitzes les dades generades per crear projectes que reconeixessin l'autor original. 
-Les contribucions es distribuiran segons els paràmetres que el propi autor hagi plantejat.



## Còdi i dataset
Tan el codi per poder obtenir el dataset com el propi CSV generat, els podeu trobar accedint al següent enllaç (https://github.com/rascundampelcuf/Web-scraping).


## Recursos
Subirats Maté, L., Calvo González, M. (2019). Web scraping. Oberta UOC Publishing, SL.

Selenium-python.readthedocs.io. 2020. Selenium With Python — Selenium Python Bindings 2 Documentation. [online] Available at: <https://selenium-python.readthedocs.io> [Accessed 9 April 2020].