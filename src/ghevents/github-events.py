#!/usr/bin/env python3

import os
import json
import requests

GHUSER = os.getenv('GITHUB_USER')
url = f'https://api.github.com/users/{GHUSER}/events'

def retrieve_events(url):
	"""Download data from url and return a Python object."""
	response = requests.get(url).text
	events = json.loads(response)
	return events

def print_events(events, n=5):
	"""Loop over first n items in events and print type and repo of each event"""
	for x in events[:n]:
		event = x['type'] + ' :: ' + x['repo']['name']
		print(event)
def main():
	"""Prints the value of GHUSER and url, and calls retrieve_events(url) and print_events(...)"""
	print(GHUSER)
	print(url)
	events = retrieve_events(url)
	print_events(events)
	
if __name__ == "__main__":
	main()
