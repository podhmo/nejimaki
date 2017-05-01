import sys
import logging
from diloading import loading
from nejimaki import emitfiles


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
        format="%(levelname)5s:%(name)30s:%(message)s",
        level=logging._nameToLevel[args.logging]
    )
    d = loading.loadfile(args.src)
    emitfiles(d, format=args.format, position=args.position or ".")
