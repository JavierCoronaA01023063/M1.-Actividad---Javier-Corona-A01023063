from mesa import Model
from mesa.time import RandomActivation
from mesa.space import Grid
from mesa.datacollection import DataCollector
from mesa.space import MultiGrid
from agent import Agent_Vacuum, Agent_Floor


class RandomModel(Model):
    """ 
    Creates a new model with random agents.
    Args:
        N: Number of agents in the simulation
        height, width: The size of the grid to model
    """
    def __init__(self, trash, Cleaner=10, width=10, height=10, density=0.6, max_time=400):
        self.num_agents = Cleaner
        self.grid = MultiGrid(width, height, torus = False) 
        self.schedule = RandomActivation(self)
        self.running = True
        self.num_floor = trash
        self.max_time = max_time

        self.datacollector = DataCollector(
            {
                "Clean": lambda m: self.count_type(m, "Clean"), 
                "Dirty": lambda m: self.count_type(m, "Dirty")
            }
        )
         

        for (contents, x, y) in self.grid.coord_iter():
            if self.random.random() < density:
                # Create a tree
                dirty = Agent_Floor((x, y), self)
                self.grid.place_agent(dirty, (x, y))
                self.schedule.add(dirty)




        for i in range(self.num_agents):
            agent = Agent_Vacuum(i, (1, 1), self)
            self.grid.place_agent(agent, (1, 1))
            self.schedule.add(agent)

        self.datacollector = DataCollector(
            {
                "Dirty": lambda m: self.count_type(m, "Dirty"),
                "Clean": lambda m: self.count_type(m, "Clean")   
            }
        )

        self.datacollector.collect(self)


    def step(self):
        '''Advance the model by one step.'''
        self.datacollector.collect(self)

        if self.count_type(self, "Dirty") == 0 or self.max_time <= 0:
            self.running = False
            cleaned = (self.count_type(self, "Clean")
                        * 100) / self.num_floor
        self.max_time -= 1
        self.schedule.step()
        self.datacollector.collect(self)


    @staticmethod
    def count_type(model, condition):
        """
        Helper method to count the number of agents in a given condition.
        """
        count = 0
        for agent in model.schedule.agents:
            if agent.condition == condition:
                count += 1
        return count