import rpyc

def echo(string):
	print('echo:', repr(string))

if __name__ == '__main__':
	config = {'allow_public_attrs': True}
	proxy = rpyc.connect('localhost', 12358, config=config)
	fo = open('afile.txt')
	numlines = proxy.root.count_lines(fo, echo)
	print('Number of lines in file = ', numlines)


