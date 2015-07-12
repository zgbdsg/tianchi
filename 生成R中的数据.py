f = open('result_0711.csv')
output = []
for line in f:
    arguments = line.strip().split(',')
    output.append('%s, %s, %s' % tuple(arguments))

print 'output = c(%s)' % ',\n'.join(output)

