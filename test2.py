def custom_append(input_list, value):
    """Adds the value to the end of the list.

    The function custom_append(input_list, value) should have the same
    functionality as input_list.append(value) where value is added to the
    end of the list and the function returns nothing.

    For example:

        >>> notes = ['Do', 'Re', 'Mi', 'Fa', 'So', 'La', 'Ti', 'Do']
        >>> custom_append(notes, 'Re')
        >>> notes == ['Do', 'Re', 'Mi', 'Fa', 'So', 'La', 'Ti', 'Do', 'Re']
        True

    """

    input_list[custom_len(input_list):] = "m"
    input_list[-1] = value


def custom_remove(input_list, value):

	new_list = []

	for item in input_list:
	    if item == value:
        	continue
    	else:
        	custom_append(new_list, item)

	print new_list

l = ['a', 'b', 'c', 'a']

custom_remove(l, 'a')


