from dependencies import binary_tree, queue  # type: ignore


class huffman_coding:
    def __init__(self):
        pass

    def __codes_update__(self, codes: dict, left: str):
        """Helper function that builds huffman codes from huffman tree

        Args:
            codes (dict): dictionary of part-built codes
            left (str): if 0 left, if not right

        Returns:
            dict: huffman codes as dictionary
        """
        for key in codes:
            if key == left:
                codes[key] = '0' + codes[key]
            else:
                codes[key] = '1' + codes[key]
        return codes

    def __queue_gen__(self, values: dict):
        """Helper function to generate queues and initialise

        Args:
            values (dict): dictionary containing frequency analysis

        Returns:
            queue: queue data structures initialised as necessary
        """
        priority_queue = queue()
        freq = queue()

        length = len(values)

        while len(priority_queue) != length:
            temp_max = 0
            temp_key = ''

            for key in values:
                if values[key] > temp_max:
                    temp_max = values[key]
                    temp_key = key

            priority_queue.enqueue(temp_key)
            freq.enqueue(temp_max)
            values.pop(temp_key)

        return priority_queue, freq

    def huffman_tree(self, values: dict):
        """Creates huffman tree based off frequency of characters

        Args:
            values (dict): dictionary containing character frequencies

        Returns:
            binary_tree: binary tree representing huffman encoding
            dict: dictionary of huffman codes
        """
        codes = {}
        priority_queue, freq = self.__queue_gen__(values)

        while len(priority_queue) > 1:
            node_1 = priority_queue.dequeue
            node_2 = priority_queue.dequeue

            if type(node_1) == binary_tree and type(node_2) == binary_tree:
                frequency = node_1.frequency + node_2.frequency
                internal_node = binary_tree(frequency, node_2, node_1)

            elif type(node_1) == binary_tree:
                frequency = node_1.frequency + freq.dequeue
                internal_node = binary_tree(frequency, node_2, node_1)
                codes.update({node_2: ''})

            elif type(node_2) == binary_tree:
                frequency = node_2.frequency + freq.dequeue
                internal_node = binary_tree(frequency, node_2, node_1)
                codes.update({node_1: ''})

            else:
                frequency = freq.dequeue + freq.dequeue
                internal_node = binary_tree(frequency, node_2, node_1)
                codes.update({node_2: '', node_1: ''})

            codes = self.__codes_update__(codes, node_2)
            priority_queue.enqueue(internal_node)

        # print(priority_queue.peek)
        # print()

        return priority_queue.peek, codes

    def huffman_encode(self, data: str):
        """Encodes string data to huffman coding format

        Args:
            data (str): text data for encoding

        Returns:
            str: encoded data as numeric string
            binary_tree: huff tree represented as binary tree
        """
        values = {}
        return_data = ''

        for letter in data:
            if letter in values.keys():
                num = values[letter] + 1
                values.update({letter: num})
            else:
                values.update({letter: 1})

        huff_tree, codes = self.huffman_tree(values)

        for letter in data:
            return_data += codes[letter]

        return return_data, huff_tree

    def huffman_decode(self, encoded_data: str, huff_tree: binary_tree):
        """Decodes huffman encoded data using huff tree

        Args:
            encoded_data (str): numeric encoded data
            huff_tree (binary_tree): binary tree representation of huff tree

        Returns:
            str: decoded data
        """
        current = huff_tree
        data = ''

        for i in encoded_data:
            leaf = current.leaf(i)

            if i == '0':
                current = current.left
            elif i == '1':
                current = current.right

            if leaf:
                data += current
                current = huff_tree

        return data

    def main(self):
        """Used to run tests on code
        """
        print('Full Encode & Decode Test:\n')

        encoded, huff_tree = (self.huffman_encode('hello'))
        print('Encoded Data: ' + encoded)
        print('Decoded Data: ' + self.huffman_decode(encoded, huff_tree))
        print(print('\nTree:\n' + str(huff_tree)))

        print('\n----------------------------\nTests Of Tree Generation:\n')

        values = {'a': 4, 'b': 2, 'c': 1, 'd': 1}
        huff_tree, codes = self.huffman_tree(values)
        print('Huffman Codes: ' + str(codes))
        print('\nTree 1:\n' + str(huff_tree))

        print()

        # values = {'x': 3, 'y': 2, 'z': 1, 'w': 1}
        # huff_tree, codes = self.huffman_tree(values)
        # print(codes)
        # print(huff_tree)

        # print()

        values = {'a': 10, 'b': 8, 'c': 6, 'd': 4, 'e': 2}
        huff_tree, codes = self.huffman_tree(values)
        print('Huffman Codes 2: ' + str(codes))
        print('\nTree 2:\n' + str(huff_tree))

        # More tests
        # values = {'m': 6, 'n': 3, 'o': 2, 'p': 1}
        # huff_tree, codes = self.huffman_tree(values)
        # print(huff_tree)

        # print()

        # values = {'q': 7, 'r': 5, 's': 3, 't': 2, 'u': 1}
        # huff_tree, codes = self.huffman_tree(values)
        # print(huff_tree)

        # print()

        # values = {'v': 4, 'w': 3, 'x': 2, 'y': 1}
        # huff_tree, codes = self.huffman_tree(values)
        # print(huff_tree)

        # print()

        print('\n----------------------------\nDecode Test:\n')

        data = '00100110111010'
        print('Pre-set Huffman Coded Data: ' + data)
        print('Decoded Data: ' + self.huffman_decode(data, huff_tree))


test = huffman_coding()
test.main()
