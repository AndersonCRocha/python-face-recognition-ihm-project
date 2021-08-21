import simpy

from src.logger import Logger


class Environment:
    def __init__(self):
        self.env = simpy.Environment()

    def add_process(self, name, process):
        Logger.info(self, f"Adding process: {name}")
        self.env.process(process)

    def timeout(self, timeout):
        return self.env.timeout(timeout)

    def run(self):
        Logger.info(self, "Starting all processes.")
        self.env.run(until=500)
