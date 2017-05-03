
# FIXME:
# Maybe we should have OS specific Syscall classes
# Tests are currently broken as collect_args got removed
class Syscall:
    __slots__ = (
        "event",
        "name",
        "process",
        "nitro",
        "args",
        "hook"
    )

    def __init__(self, event, name, process, nitro, args):
        self.event = event
        self.name = name
        self.process = process
        self.nitro = nitro
        self.args = args
        self.hook = None

    def as_dict(self):
        info = {
            "name": self.name,
            "event": self.event.as_dict(),
        }
        if self.process:
            info['process'] = self.process.as_dict()
        if self.hook:
            info['hook'] = self.hook
        modified = self.args.modified
        if modified:
            info['modified'] = modified
        return info
