from functools import wraps
from datetime import datetime

def duration(head):
    def real_decorator(func):
        @wraps(func)
        def inner(*args, **kwargs):
            st_time = datetime.utcnow()
            print("============ Start %s at %s ============"%(head, st_time.strftime("%H:%M:%S")))
            res = func(*args,**kwargs)
            print("============= Duration : %s ============="%(datetime.utcnow()-st_time))
            return res
        return inner
    return real_decorator
