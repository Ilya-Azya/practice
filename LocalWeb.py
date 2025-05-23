class Data:
    def __init__(self, data, ip):
        self.data = data
        self.ip = ip

    def __repr__(self):
        return f"Data(data={self.data!r}, ip={self.ip})"


class Server:
    _next_ip = 0

    def __init__(self):
        self.ip = Server._next_ip
        Server._next_ip += 1
        self.buffer = []
        self.router = None

    def get_ip(self):
        return self.ip

    def send_data(self, data):
        if self.router:
            self.router.send(data)

    def get_data(self):
        received = self.buffer[:]
        self.buffer.clear()
        return received


class Router:
    def __init__(self):
        self.buffer = []
        self._servers = {}

    def link(self, server):
        self._servers[server.get_ip()] = server
        server.router = self

    def unlink(self, server):
        ip = server.get_ip()
        if ip in self._servers:
            del self._servers[ip]
        server.router = None

    def send(self, data):
        self.buffer.append(data)
        ip = data.ip
        if ip in self._servers:
            self._servers[ip].buffer.append(data)