from agency_swarm.agents import Agent
from .tools.util.selenium import set_selenium_config


class BrowsingAgent(Agent):
    def __init__(self, selenium_config=None):
        super().__init__(
            name="BrowsingAgent",
            description="This agent is designed to navigate and search web effectively.",
            instructions="./instructions.md",
            files_folder="./files",
            schemas_folder="./schemas",
            tools=[],
            tools_folder="./tools"
        )

        if selenium_config is not None:
            set_selenium_config(selenium_config)
