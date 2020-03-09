#!/usr/bin/env python3
"""
    bibtex2md
    ~~~~~~~~~

    bibtex2md translates bibtex files to plaintext reference lists.

    Author  : Eddy van den Aker
    License : MIT
"""
import os
import sys
import bibtexparser
import argparse

from formats import formats_list, APA6

description = 'BibTex2Md translates bibtex files to plaintext reference lists.'
description += '\n\nAvailable Reference Styles:\n'
for f in formats_list:
    description += f'- {f}\n'

parser = argparse.ArgumentParser(description=description,
    formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument('input_file', metavar='file', type=str,
    help='The bibtex file to translate')
parser.add_argument('ref_style', metavar='reference style', type=str,
    help='The reference style to format the references in.')
parser.add_argument('-o', '--output', action='store',
    help='File to output the reference list to.')

if __name__ == '__main__':
    args = parser.parse_args()

    # Parse input path
    input_path = os.path.abspath(args.input_file)
    if not os.path.exists(input_path):
        print('Bibtex file does not exist', file=sys.stderr)
        sys.exit(1)
    
    with open(input_path) as f:
        bib_db = bibtexparser.load(f)
        bib_db.entries
    
    # Parse reference style
    if args.ref_style in formats_list:
        references_txt = formats_list[args.ref_style].generate_reference_list(
            bib_db.entries)
    else:
        print('Invalid reference style')
        sys.exit(1)

    # Parse output path
    if args.output and os.path.exists(os.path.dirname(
            os.path.abspath(args.output))):
        ouput_path = os.path.abspath(args.output)
        with open(ouput_path, 'w') as f:
            f.write(references_txt)
    elif not args.output:
        print(references_txt)
    else:
        print('Output folder not found')
        sys.exit(1)
