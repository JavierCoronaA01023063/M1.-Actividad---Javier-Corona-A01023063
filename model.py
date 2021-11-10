from mesa import Model
from mesa.time import RandomActivation
from mesa.space import Grid
from agent import Agent_Vacuum, Agent_Floor

class RandomModel(Model):
    """ 
    Creates a new model with random agents.
    Args:
        N: Number of agents in the simulation
        height, width: The size of the grid to model
    """
    def __init__(self, Cleaner, width, height, density=0.6):
        self.num_agents = Cleaner
        self.grid = Grid(width,height,torus = False) 
        self.schedule = RandomActivation(self)
        self.running = True 

        for (contests, x, y) in self.grid.coord_iter():
            state = "Dirty"
            if self.random.random() < density:
                state = "Clean"
            

            agent = Agent_Floor((x, y), state, self)


            self.grid._place_agent((x, y), agent)
            self.schedule.add(agent)

        for i in range(self.num_agents):
            agent = Agent_Vacuum(i, (1, 1), self)
            self.grid.place_agent(agent, (1, 1))
            self.schedule.add(agent)


    def step(self):
        self.schedule.step()