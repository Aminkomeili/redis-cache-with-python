# Redis Cache with Python

This is a Python project that demonstrates how to use Redis as a cache server for storing structured data such as dictionaries and lists. The project uses the redis library to connect to a Redis server and provides a RedisCache class for interacting with the Redis cache.


## Requirements

1. Python 3.x
1. redis library

You can install the redis library using pip:

pip install redis

## Usage

To use the RedisCache class in your Python program, you can import it and create an instance:

from redis_cache import RedisCache

cache = RedisCache()

## Storing Data

To store a value in Redis cache, you can use the set method with a key and value:

cache.set('my_key', {'name': 'Amin', 'age': 30}, expire=60)

The expire parameter specifies the time-to-live (TTL) for the key, in seconds. After the TTL expires, the key will be automatically deleted from the cache.
## Retrieving Data

To retrieve a value from Redis cache, you can use the get method with a key:

value = cache.get('my_key')
print(value)

If the key does not exist in the cache, get will return None.
## Lists

To add an item to a list in Redis cache, you can use the lpush method with a key and value:


cache.lpush('my_list', {'name': 'Ali', 'age': 25})

To retrieve a list from Redis cache, you can use the lrange method with a key:


my_list = cache.lrange('my_list')
print(my_list)

## Dictionaries

To set a field in a dictionary in Redis cache, you can use the hset method with a key, field, and value:


cache.hset('my_dict', 'name', 'Reza')

To retrieve a field from a dictionary in Redis cache, you can use the hget method with a key and field:

name = cache.hget('my_dict', 'name')
print(name)

To delete a field from a dictionary in Redis cache, you can use the hdel method with a key and field:

cache.hdel('my_dict', 'name')

## Contributing

If you would like to contribute to this project, please open an issue or pull request on GitHub.
