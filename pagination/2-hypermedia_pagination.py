#!/usr/bin/env python3
"""
    Task 2
"""
import csv
import math
from typing import List, Tuple, Dict


def index_range(page, page_size) -> Tuple[int, int]:
    """Return a start and end index"""
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)


class Server:
    """
        Server class to paginate a database of popular baby names.
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
        """adapt start_index and end_index at the dataset"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        dataset = self.dataset()
        start_index, end_index = index_range(page, page_size)
        if start_index > len(dataset):
            return []
        else:
            return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
            Return the correct page from the dataset.
        """
        dataset = self.dataset()
        data_page = self.get_page(page, page_size)
        total_pages = math.ceil(len(dataset) / page_size)

        return {
            'page_size': len(data_page),
            'page': page,
            'data': data_page,
            'next_page': page + 1 if page < total_pages else None,
            'prev_page': page - 1 if page > 1 else None,
            'total_pages': total_pages
        }
