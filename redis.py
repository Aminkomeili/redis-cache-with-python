import redis

class RedisCache:
    def __init__(self, host='localhost', port=6379, db=0):
        self.redis = redis.Redis(host=host, port=port, db=db)

    def get(self, key):
        """
        بازیابی مقدار از کش Redis با استفاده از کلید
        """
        result = self.redis.get(key)
        if result is None:
            return None
        return pickle.loads(result)

    def set(self, key, value, expire=None):
        """
        ذخیره مقدار در کش Redis با استفاده از کلید و زمان انقضا
        """
        pickled_value = pickle.dumps(value)
        if expire is None:
            self.redis.set(key, pickled_value)
        else:
            self.redis.setex(key, pickled_value, expire)

    def delete(self, key):
        """
        حذف مقدار از کش Redis با استفاده از کلید
        """
        self.redis.delete(key)

    def lrange(self, key, start=0, end=-1):
        """
        بازیابی لیست از کش Redis با استفاده از کلید
        """
        result = self.redis.lrange(key, start, end)
        return [pickle.loads(x) for x in result]

    def lpush(self, key, value):
        """
        افزودن مقدار به لیست در کش Redis با استفاده از کلید
        """
        pickled_value = pickle.dumps(value)
        self.redis.lpush(key, pickled_value)

    def hget(self, key, field):
        """
        بازیابی مقدار از دیکشنری در کش Redis با استفاده از کلید و فیلد
        """
        result = self.redis.hget(key, field)
        if result is None:
            return None
        return pickle.loads(result)

    def hset(self, key, field, value):
        """
        ذخیره مقدار در دیکشنری در کش Redis با استفاده از کلید و فیلد
        """
        pickled_value = pickle.dumps(value)
        self.redis.hset(key, field, pickled_value)

    def hdel(self, key, field):
        """
        حذف مقدار از دیکشنری در کش Redis با استفاده از کلید و فیلد
        """
        self.redis.hdel(key, field)

        
####test####

cache = RedisCache()

# ذخیره کردن یک مقدار در کش Redis با استفاده از کلید و زمان انقضا
cache.set('my_key', {'name': 'John', 'age': 30}, expire=60)

# بازیابی یک مقدار از کش Redis با استفاده از کلید
value = cache.get('my_key')
print(value)

# افزودن یک مورد به یک لیست در کش Redis با استفاده از کلید
cache.lpush('my_list', {'name': 'Jane', 'age': 25})

# بازیابی لیست از کش Redis با استفاده از کلید
my_list = cache.lrange('my_list')
print(my_list)

# ذخیره یک مقدار در دیکشنری در کش Redis با استفاده از کلید و فیلد
cache.hset('my_dict', 'name', 'Bob')

# بازیابی مقدار یک فیلد از دیکشنری در کش Redis با استفاده از کلید و فیلد
name = cache.hget('my_dict', 'name')
print(name)

# حذف یک مقدار از دیکشنری در کش Redis با استفاده از کلید و فیلد
cache.hdel('my_dict', 'name')
