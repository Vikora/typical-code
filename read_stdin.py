import sys

def read_matrix():
    """
        Read input from stdin.
        Input format:
        n m
        n lines of int-arrays of size m
        e.g.
        >>> 2 3
        >>> 9 8 7
        >>> 4 5 6
    """
    first_line = sys.stdin.readline()
    n, m = map(int, first_line.split())
    print(f"$ {n} {m}")
    for line in sys.stdin.readlines():
        m_array = list(map(int, line.split()))
        print(f"$ {m_array}")

def read_array():
    n = int(sys.stdin.readline())
    line = sys.stdin.readline().split()
    array = list(map(int, line))

if __name__ == "__main__":
    read_matrix()
