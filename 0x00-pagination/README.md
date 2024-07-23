# Pagination Project

This repository contains a series of tasks designed to implement and demonstrate pagination techniques in a Python-based server. The project uses a dataset of popular baby names and provides functionalities for simple pagination, hypermedia pagination, and deletion-resilient pagination.

## Table of Contents

- [Description](#description)
- [Learning Objectives](#learning-objectives)
- [Requirements](#requirements)
- [Setup](#setup)
- [Tasks](#tasks)
  - [Task 0: Simple helper function](#task-0-simple-helper-function)
  - [Task 1: Simple pagination](#task-1-simple-pagination)
  - [Task 2: Hypermedia pagination](#task-2-hypermedia-pagination)
  - [Task 3: Deletion-resilient hypermedia pagination](#task-3-deletion-resilient-hypermedia-pagination)
- [Usage](#usage)
- [Author](#author)

## Description

This project demonstrates various pagination techniques in a backend server context using Python. It includes:

1. Simple helper function to calculate pagination ranges.
2. Simple pagination to paginate a dataset with specified page and page size.
3. Hypermedia pagination to include metadata in pagination responses.
4. Deletion-resilient pagination to ensure consistency when items are deleted from the dataset.

## Learning Objectives

At the end of this project, you should be able to explain the following concepts without using Google:

- How to paginate a dataset with simple `page` and `page_size` parameters.
- How to paginate a dataset with hypermedia metadata.
- How to paginate in a deletion-resilient manner.

## Requirements

- All files will be interpreted/compiled on Ubuntu 18.04 LTS using Python 3 (version 3.7).
- All files should end with a new line.
- The first line of all files should be exactly `#!/usr/bin/env python3`.
- A `README.md` file, at the root of the folder of the project, is mandatory.
- Your code should use the `pycodestyle` style (version 2.5.*).
- The length of your files will be tested using `wc`.
- All modules should have documentation.
- All functions should have documentation.
- All functions and coroutines must be type-annotated.

## Setup

Download the dataset file `Popular_Baby_Names.csv` and place it in the root of the project directory.

## Tasks

### Task 0: Simple helper function

Create a function `index_range` that takes two integer arguments `page` and `page_size`, and returns a tuple containing the start and end index for pagination.

File: `0-simple_helper_function.py`

### Task 1: Simple pagination

Implement a `Server` class with a `get_page` method that paginates the dataset based on `page` and `page_size`.

File: `1-simple_pagination.py`

### Task 2: Hypermedia pagination

Enhance the `Server` class with a `get_hyper` method that returns a dictionary with pagination metadata.

File: `2-hypermedia_pagination.py`

### Task 3: Deletion-resilient hypermedia pagination

Further enhance the `Server` class with a `get_hyper_index` method to handle pagination in a deletion-resilient manner.

File: `3-hypermedia_del_pagination.py`

## Usage

Clone the repository and navigate to the project directory. To run the examples and test the functionalities, execute the main files for each task:

```bash
$ ./0-main.py
$ ./1-main.py
$ ./2-main.py
$ ./3-main.py

