import sys
import contextlib
from io import StringIO


@contextlib.contextmanager
def indent(n):
    buf = StringIO()
    with contextlib.redirect_stdout(buf):
        yield buf
    buf.seek(0)

    prefix = " " * n
    write = sys.stdout.write
    for line in buf:
        write(prefix)
        write(line)
    sys.stdout.flush()


@contextlib.contextmanager
def block(code):
    print("")
    print(".. code-block:: {}".format(code))
    print("")
    with indent(2) as buf:
        yield buf
    print("")
