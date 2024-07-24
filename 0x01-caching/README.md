# Caching System

This project contains implementations of various caching algorithms, each inheriting from a base caching class.

## Classes

1. **BasicCache**
   - A simple caching system with no limit on the number of items.

2. **FIFOCache**
   - Implements a First-In-First-Out (FIFO) caching algorithm.

3. **LIFOCache**
   - Implements a Last-In-First-Out (LIFO) caching algorithm.

4. **LRUCache**
   - Implements a Least Recently Used (LRU) caching algorithm.

5. **MRUCache**
   - Implements a Most Recently Used (MRU) caching algorithm.

6. **LFUCache**
   - Implements a Least Frequently Used (LFU) caching algorithm, using LRU for tie-breaking.

## Files

- **base_caching.py**: Contains the `BaseCaching` class which is the base for all caching algorithms.
- **0-basic_cache.py**: Contains the implementation of `BasicCache`.
- **1-fifo_cache.py**: Contains the implementation of `FIFOCache`.
- **2-lifo_cache.py**: Contains the implementation of `LIFOCache`.
- **3-lru_cache.py**: Contains the implementation of `LRUCache`.
- **4-mru_cache.py**: Contains the implementation of `MRUCache`.
- **100-lfu_cache.py**: Contains the implementation of `LFUCache`.

## Usage

Each cache implementation can be tested using their respective main files:

- **0-main.py**: Tests `BasicCache`
- **1-main.py
