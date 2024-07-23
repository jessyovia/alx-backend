#!/usr/bin/env python3
"""Defines the index_range func for pagination"""


from typing import Tuple, List
import csv


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Calculate the start and end indexes for a pagination range."""
    begin, end = 0, 0
    for u in range(page):
        begin = end
        end += page_size
    return (begin, end)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Gets a page of info"""
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0

        begin, end = index_range(page, page_size)
        data = self.dataset()
        if begin > len(data):
            return []
        return data[begin:end]
