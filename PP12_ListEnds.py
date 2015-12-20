a = [5, 10, 15, 20, 25]


def list_ends(list1):
	list_begin = list1[0]
	list_end = list1[len(list1)-1]
	new_list = [list_begin, list_end]
	print ("The first number in the list is " + str(list_begin) + " and the last number in the list is " + str(list_end))
	print (new_list)


if __name__ == "__main__":
	list_ends(a)
