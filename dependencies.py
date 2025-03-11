class binary_tree:
    def __init__(self, freq: int, left, right):
        """Initialises binary tree with data fields required for a huff tree

        Args:
            freq (int): int huff frequency value
            left (binary_tree/str): Left pointer or string value
            right (binary_tree/str): Right pointer or string value
        """
        self._tree = [freq, left, right]

    def freq_update(self, value: int):
        """Allows for frequency update

        Args:
            value (int): _description_
        """
        self._tree[0] = value

    @property
    def frequency(self):
        return self._tree[0]

    @property
    def left(self):
        return self._tree[1]

    @property
    def right(self):
        return self._tree[2]

    def leaf(self, left: int):
        """Checks if next node is a leaf

        Args:
            left (int): 0 or 1, 0 = left, 1 = right

        Returns:
            bool: true or false (depending on if leaf node)
        """
        if left == '0':
            left = True
        else:
            left = False

        if left:
            return not type(self._tree[1]) == binary_tree
        else:
            return not type(self._tree[2]) == binary_tree

    def __str__(self, depth=0, freq=0):
        """Creates graphic representation of tree

        Args:
            depth (int, optional): used in recursive call. Defaults to 0.
            freq (int, optional): used in recursive call. Defaults to 0.

        Returns:
            str: string representation of tree using ascii graphics
        """
        depth += 1
        temp_tree = self._tree.copy()
        return_string = ''

        # Various spacing used to format growing tree correctly
        # Gets quite complex below (and a little verbose), but works!
        if freq == 0:
            freq = len(str(temp_tree[0]))

        diff = freq - len(str(temp_tree[0]))

        if depth > 1:
            pad = ' ' * (depth - 1)
            pad_2 = ' ' * ((depth - 1) - diff)
        else:
            pad = ''

        if type(temp_tree[1]) == binary_tree:
            temp_tree[1] = temp_tree[1].__str__(depth, freq)
        else:
            temp_tree[1] = '\n' + (' ' * diff) + pad + \
                (' ' * (depth-1)) + temp_tree[1] + ' '

        if type(temp_tree[2]) == binary_tree:
            temp_tree[2] = temp_tree[2].__str__(depth, freq)
        else:
            temp_tree[2] = pad_2 + temp_tree[2] + ' '

        temp_tree[0] = '  ' + (' ' * diff) + str(temp_tree[0]) + \
            '\n' + (' ' * depth) + pad + (' ' * diff) + '/' + \
            (len(str(temp_tree[0])) * ' ') + '\\'

        for i in temp_tree:
            return_string += i

        return return_string


class queue:
    def __init__(self):
        """Initialised generic queue (really a stack)
        Only named queue, as this is expected for huffman encoding
        """
        self._queue = []

    def __len__(self):
        return len(self._queue)

    def enqueue(self, data: str):
        self._queue.append(data)

    @property
    def dequeue(self):
        return self._queue.pop()

    @property
    def peek(self):
        # Peeks last item in queue
        return self._queue[-1]
