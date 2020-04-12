
<img src="https://www.incimages.com/uploaded_files/image/970x450/rey-seven-nm-mZ4Cs2I-unsplash_397351.jpg">

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3749018.svg)](https://doi.org/10.5281/zenodo.3749018)

# Web-scraping
> UOC - Typology and life cycle of data - PRAC1

## Description
This project has been completed during the PRAC1 of the subject Typology and life cycle of the data of the master's degree in Data Science of the *Universitat Oberta de Catalunya* (UOC).

The objective of this PRAC was to complete a Web Scraping in Python of the website *"[Casa del Libro](https://www.casadellibro.com/)"*. From this website a list of all the books on the subject of "Literatura/Ciencia ficción" has been created and a data set with the created data has been generated.

---

## Source files

```bash
────Web-scraping
    │
    ├───data
    │       data.csv
    │
    ├───pdf
    │       respostes.Rmd
    │       respostes.pdf
    │
    └───src
            book.py
            main.py
            scraper.py
```
- **data/data.csv**: Output dataset. It contains a list of books.
- **pdf/respostes.Rmd**: Source file with the project answers.
- **pdf/respostes.pdf**: Delivery file with the project answers.
- **src/book.py**: It contains the implementation of Book class. It was created to easily manage the information of each book.
- **src/main.py**: Input. It starts the scraping process.
- **src/scraper.py**: It contains the implementation of Scraper class. Scraper class contains the necessary methods to generate the dataset with the data provided by *"Casa del Libro"*.

## Installation

### Clone

- Clone this repo to your local machine using `https://github.com/rascundampelcuf/Web-scraping.git`

### Setup

- In order to be able to run the code you should install the following packages:
> `selenium`
```shell
$ pip install selenium
```
> `csv`
```shell
$ pip install csv
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