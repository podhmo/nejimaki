import logging
import os.path
from dictknife import loading
logger = logging.getLogger(__name__)


def emitfiles(d, format=None, position="."):
    for name, data in d.items():
        fpath = os.path.join(position, name)
        logger.info("emit [F] %s", fpath)
        loading.dumpfile(data, fpath, format=format)
