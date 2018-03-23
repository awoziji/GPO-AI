'''

    Simulate real script.

'''


def init():
    print('init complete.')


def get_similar_docs(text, title='Document Title 1'):

    results = [
        ('Document Number 1', title,              'http://bit.ly/DEADBEEF'),
        ('Document Number 2', 'Document Title 2', 'http://bit.ly/DEADBEEF'),
        ('Document Number 3', 'Document Title 3', 'http://bit.ly/DEADBEEF'),
        ('Document Number 4', 'Document Title 4', 'http://bit.ly/DEADBEEF'),
        ('Document Number 5', 'Document Title 5', 'http://bit.ly/DEADBEEF'),
    ]

    return results


if __name__ == '__main__':
    import sys
    from pprint import pprint

    print('results:\n')
    pprint(get_similar_docs(sys.argv[1], title=sys.argv[2]))

