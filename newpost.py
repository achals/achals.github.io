from __future__ import absolute_import

from datetime import datetime
import sys

TEMPLATE_FILE = "_template.md"
DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"
DATE_FORMAT = "%Y-%m-%d"

import argparse

parser = argparse.ArgumentParser(description='Create a new post.')
parser.add_argument('--title', type=str, help='Title for the post', required=True)


def main():
    args = parser.parse_args()
    title = args.title

    with open(TEMPLATE_FILE, 'r') as f:
        contents = f.read()

    now = datetime.now()
    formatted_now = now.strftime(DATETIME_FORMAT)
    today = now.strftime(DATE_FORMAT)
    contents = contents.replace('$TITLE', title)
    contents = contents.replace('$DATE', formatted_now)

    title_in_path = title.replace(' ', '-').lower()

    destination = "_posts/{}-{}.markdown".format(today, title_in_path)

    with open(destination, 'w') as f:
        f.write(contents)


if __name__ == '__main__':
    main()




    