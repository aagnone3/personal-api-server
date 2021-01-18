import os
import json
import pickle
import dateutil.parser
import datetime
from json import JSONEncoder


class DateTimeEncoder(JSONEncoder):
        #Override the default method
        def default(self, obj):
            if isinstance(obj, (datetime.date, datetime.datetime)):
                return obj.isoformat()


def memoize(func):
    out_file = 'fills.json'

    def memoized_func(*args, **kwargs):
        if os.path.isfile(out_file):
            with open(out_file, 'r') as fp:
                return pickle.load(fp)
        result = func(*args, **kwargs)
        with open(out_file, 'w') as fp:
            pickle.dump(result, fp)
        return result

    return memoized_func
