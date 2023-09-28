#!/usr/bin/python3


def find_peak(list_of_integers):
	if len(list_of_integers) == 0:
		return None
	if len(list_of_integers) == 1:
		return list_of_integers[0]
	if list_of_integers[0] > list_of_integers[1]:
		return list_of_integers[0]
	if list_of_integers[-1] > list_of_integers[-2]:
		return list_of_integers[-1]
	for s in range(1, len(list_of_integers) - 1):
		if list_of_integers[s] >= list_of_integers[s-1]:
			if list_of_integers[s] >= list_of_integers[s+1]:
				return list_of_integers[s]
	return None
