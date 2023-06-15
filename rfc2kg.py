import os
import logging
import argparse
import sys

from text2kg import text2kg, plot_kg
import networkx as nx
from tqdm import tqdm


def setup_logging():
    """
    Util function to set up logging for this module
    :return: None; sets global logger config
    """
    loglevel = os.environ.get('LOGLEVEL', 'INFO').upper()
    logging.basicConfig(
        format='%(asctime)s - %(levelname)s: %(message)s',
        level=loglevel,
        handlers=[logging.StreamHandler(sys.stdout)]
    )


def parse_args():
    """
    Util function to parse our arguments
    :return: Parsed args
    """
    parser = argparse.ArgumentParser(
        description='CLI tool for cataloging markdown files in repos.'
    )
    parser.add_argument(
        'datafiles',
        help='Datafiles to process',
        nargs='+',
        metavar='DATAFILE'
    )


    return parser.parse_args()


def apply_config(args):
    """
    Util function to apply config from args and/or files
    """
    pass


def main():
    # Set up our environment
    setup_logging()
    args = parse_args()
    # logging.info(args)
    apply_config(args)

    # Iterate over provided datafiles, generate KG, and save as GraphML
    failed = {}
    for datafile in tqdm(args.datafiles):
        try:
            corpus = open(datafile, "rt").read()
            kg = text2kg(corpus)
            base, _ = os.path.splitext(datafile)
            kgfile = f"{base}.graphml"
            nx.write_graphml(kg, kgfile, named_key_ids=True)
        except Exception as e:
            failed[datafile] = str(e)

    if failed:
        for datafile, err in failed.items():
          logging.error(f"Failed on {datafile}: {err}")

if __name__ == '__main__':
    main()

