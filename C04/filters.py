import sys

def filter_files(name, function):
    with open(name, 'r') as input, open(name + '.out', 'w') as output:
        for line in input:
            output.write(function(line))


def filter_stream(function):
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        print(function(line), end = '')


if __name__ == '__main__':
    filter_stream(lambda line: line)