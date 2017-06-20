from nitro.listener import Listener
from nitro.backends import get_backend

class Nitro:

    def __init__(self, domain, introspection=True):
        self.listener = Listener(domain)
        self.introspection = introspection
        self.backend = None
        if self.introspection:
            self.backend = get_backend(domain)

    def listen(self):
        yield from self.listener.listen()

    def __enter__(self):
        return self

    def __exit__(self, *_):
        self.stop()

    def stop(self):
        if self.backend is not None:
            self.backend.stop()
        self.listener.stop()