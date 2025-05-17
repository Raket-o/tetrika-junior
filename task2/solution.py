import csv
import logging
from typing import Any

import requests
import time

from bs4 import BeautifulSoup


BASE_URL = "https://ru.wikipedia.org"
CATEGORY_URL = f"{BASE_URL}/wiki/Категория:Животные_по_алфавиту"

logger = logging.getLogger(__name__)
logging.basicConfig(level="INFO", format='%(asctime)s - %(levelname)s - "%(message)s"')


class ParserAnimals:
    def __init__(self, url: str, parser: BeautifulSoup) -> None:
        """
        Initialization class function.
        """
        self.parser: BeautifulSoup
        self.url: str = url
        self.bs: BeautifulSoup = parser

    def parser_page(self) -> None:
        """
        A function of the parsing class.
        """
        self.parser = self.bs(requests.get(self.url).text, "lxml")

    def get_dict_name(self) -> dict[Any, Any]:
        """
        The class function parses the names. Returns a dictionary with names.
        """
        list_name = self.parser.find_all(class_="mw-category mw-category-columns")[
            0
        ].find_all(class_="mw-category-group")
        dict_name = dict()
        for i in list_name:
            for name in i.find_all("li"):
                name = name.text
                dict_name.setdefault(name[0], set())
                dict_name.get(name[0]).add(name)
        return dict_name

    def next_page(self) -> None:
        """
        The class function parses the url of the next page and assigns it to self.url
        """
        tags_a = self.parser.find(class_="mw-category-generated").find_all("a")
        for tag in tags_a:
            if tag.text == "Следующая страница":
                self.url = f"{BASE_URL}{tag.get('href')}"
                break


def count_animals_by_letter(dict_name: dict, dict_count: dict) -> dict:
    """
    The function of counting words by the first letter.
    """
    for k, v in dict_name.items():
        if not dict_count.get(k):
            dict_count[k] = len(v)
        else:
            dict_count[k] += len(v)
    return dict_count


def data_rec_file(file_name: str, dict_count: dict) -> None:
    """
    The function sorts and writes the data to a csv file.
    """
    with open(file_name, mode="w", encoding="utf-8") as file:
        writer = csv.writer(file)
        for letter, count in sorted(dict_count.items()):
            writer.writerow([letter, count])


def filter_rus_letter(word: str) -> bool:
    """
    The function filters the words.
    If the word begins with a Russian letter,
    it returns True, otherwise False.
    """
    if not word[0] in "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ":
        return False
    return True


if __name__ == "__main__":
    logger.info("I started parsing")

    dict_count_animals = dict()
    parser_animals = ParserAnimals(url=CATEGORY_URL, parser=BeautifulSoup)
    while True:
        logger.info("Please Wait")
        parser_animals.parser_page()
        dict_name_animals = parser_animals.get_dict_name()
        result_count = count_animals_by_letter(dict_name_animals, dict_count_animals)

        if result_count.get("A"):
            break

        parser_animals.next_page()
        time.sleep(0.2)

    filtered_result_count = {
        key: value for key, value in result_count.items() if filter_rus_letter(key)
    }
    data_rec_file("beasts.csv", filtered_result_count)
    logger.info("Work is complete")
