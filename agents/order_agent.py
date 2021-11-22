import logging

from agents import Agent

log = logging.getLogger(Agent.OrderAgent)


class OrderAgent:
    # publish = None # No need to assign it will automatically assigned by rakun

    def __init__(self, *args, **kwargs):
        self.selected_pair = ""

    async def execute(self, *args, **kwargs):
        log.info("RUN")
        while True:
            await self.publish({
                "name": "AgentOne"
            })
