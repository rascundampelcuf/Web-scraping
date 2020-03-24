<a><img src="https://www.rd.com/wp-content/uploads/2017/10/This-Is-How-Long-It-Takes-To-Read-The-Whole-Dictionary_509582812-Billion-Photos_FB-e1574101045824-768x434.jpg"></a>

# Web-scraping
> UOC - Typology and life cycle of data - PRAC1

## Descripció
This project has been completed during the PRAC1 of the subject Typology and life cycle of the data of the master's degree in Data Science of the *Universitat Oberta de Catalunya* (UOC).

The objective of this PRAC was to complete a Web Scraping in Python of the website *"[Casa del Libro](https://www.casadellibro.com/)"*. From this website a list of all the books on the subject of "Literature" has been extended and a data set with the extended data has been generated.

---

## Source files

```bash
────Web-scraping
    │   README.md
    │
    ├───data
    │       data.csv
    │
    └───src
            book.py
            main.py
            scraper.py
```
- **data/data.csv**: Output dataset. It contains a list of books.
- **src/book.py**: It contains the implementation of Book class. It was created to easily manage the information of each book.
- **src/main.py**: Input. It starts the scraping process.
- **src/scraper.py**: It contains the implementation of Scraper class. Scraper class contains the necessary methods to generate the dataset with the data provided by *"Casa del Libro"*.

## Installation

### Clone

- Clone this repo to your local machine using `https://github.com/rascundampelcuf/Web-scraping.git`

### Setup

- In order to be able to run the code you should install the following packages:
> `requests`
```shell
$ pip install requests
```
> `bs4`
```shell
$ pip install bs4
```

- Once installed, move to `src` folder and run:
```shell
$ python main.py
```

---

## Team

| **Gabriel Izquierdo** | **Mireia Olivella** |
| :---: | :---: |
| [<img src="https://avatars.githubusercontent.com/rascundampelcuf" width="200" height="200">](http://github.com/rascundampelcuf) | [<img src="https://avatars.githubusercontent.com/MIREIAOLIVELLA" width="200" height="200">](http://github.com/MIREIAOLIVELLA) |
| <a href="http://github.com/rascundampelcuf" target="_blank">`github.com/rascundampelcuf`</a> | <a href="http://github.com/MIREIAOLIVELLA" target="_blank">`github.com/MIREIAOLIVELLA`</a> |

## Resources
1. Subirats Maté, L., Calvo González, M. (2019). *Web scraping*. Oberta UOC Publishing, SL.