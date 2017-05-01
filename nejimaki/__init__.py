import logging
import os.path
from collections import OrderedDict
from dictknife import loading
logger = logging.getLogger(__name__)


def setup():
    loading.setup()
    loading.dispather.dumper.add_format(loading.unknown, loading.raw.dump)


def transform(data):
    if hasattr(data, "keys"):
        d = OrderedDict()
        for k, v in data.items():
            if k.startswith("./"):
                merge(d, k, transform(v))
            else:
                d[k] = transform(v)
        return d
    elif isinstance(data, (list, tuple)):
        return [transform(x) for x in data]
    else:
        return data


def merge(d, k, v):
    if hasattr(v, "keys"):
        for sk, sv in v.items():
            d[os.path.join(k, sk)] = sv
    else:
        d[k] = v


def emitfiles(d, format=None, position="."):
    if isinstance(d, (list, tuple)):
        for x in d:
            emitfiles(x, format=format, position=position)
    else:
        for name, data in d.items():
            fpath = os.path.join(position, name)
            logger.info("emit:%s", os.path.normpath(fpath))
            loading.dumpfile(data, fpath, format=format)
