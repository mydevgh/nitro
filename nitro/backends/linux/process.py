from nitro.backends.process import Process

class LinuxProcess(Process):
    """Class representing a Linux process"""

    __slots__ = (
        "task_struct",
        "name",
        "pid"
    )

    def __init__(self, libvmi, cr3, task_struct):
        super().__init__(libvmi, cr3)
        pid_offset = self.libvmi.get_offset("linux_pid")
        name_offset = self.libvmi.get_offset("linux_name")

        #: Kernel task_struct for the process
        self.task_struct = task_struct
        #: Proces PID
        self.pid = self.libvmi.read_32(self.task_struct + pid_offset, 0)
        #: Name of the processs
        self.name = self.libvmi.read_str_va(self.task_struct + name_offset, 0)
