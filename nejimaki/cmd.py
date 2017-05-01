import sys
import logging
from dictknife import loading
from nejimaki import emitfiles, transform


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("src", nargs="?", type=argparse.FileType("r"), default=sys.stdin)
    parser.add_argument("--logging", default="INFO", choices=list(logging._nameToLevel.keys()))
    parser.add_argument("-f", "--format", default=None, choices=loading.get_formats())
    parser.add_argument("--position", default=None)

    args = parser.parse_args()
    loading.setup()
    logging.basicConfig(
        format="%(levelname)5s\t%(name)10s\t%(message)s",
        level=logging._nameToLevel[args.logging]
    )
    d = loading.load(args.src)
    emitfiles(transform(d), format=args.format, position=args.position or ".")
