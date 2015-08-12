# -*- coding: utf-8 -*-
__author__ = 'luckydonald'

import logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

import sys  # launch arguments


from sites.ponyFm import PonyFM
from sites.py_compatibility import input
from utilities.files import open_file_folder
import secret_logins

def main(argv):
	if argv is None:
		argv = sys.argv[1:]  # argv[0] is program name
	if argv:
		url = argv[0]
	else:
		url = input("Url to download:")
	if not url:
		print("no url given.")
		sys.exit(0)
	ponyfm = PonyFM(username=secret_logins.pony_fm[0], password=secret_logins.pony_fm[1])
	ponyfm.get_token()
	song_id = can_load(url)
	if song_id:
		file = download_song(song_id, cover_as_file=True)
		open_file_folder(file)
		print(file)
	else:
		print("Not valid url.")

if __name__ == "__main__":
	main(None)