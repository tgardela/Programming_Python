def scanner(name, function):
    for line in open(name, 'r'):
        function(line)


#minimalistic versions:
# def scanner(name, function):
#     list(map(function, open(name, 'r')))
#
# def scanner(name, function):
#     [function(line) for line in open(name, 'r')]
#
# def scanner(name, function):
#     list(function(line) for line in open(name, 'r'))