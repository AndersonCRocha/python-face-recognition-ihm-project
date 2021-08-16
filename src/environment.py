import simpy

from src.logger import Logger


class Environment:
    def __init__(self):
        self.env = simpy.Environment()

    def add_process(self, process):
        self.env.process(process)

    def run(self):
        Logger.info(self, "Starting all processes.")
        self.env.run(until=10000)

