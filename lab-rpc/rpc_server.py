import rpyc

class RemoteService(rpyc.Service):
	def exposed_count_lines(self, fo, function):
		print('Client has remotely called exposed_count_lines()')
		for n, line in enumerate(fo):
			function(line)
		return n+1

if __name__ == '__main__':
	from rpyc.utils.server import ThreadedServer
	thr = ThreadedServer(RemoteService, port = 12358)
	thr.start()


