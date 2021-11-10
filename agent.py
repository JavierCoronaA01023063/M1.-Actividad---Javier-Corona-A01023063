from mesa import Agent

class Agent_Vacuum(Agent):
    """
    Obstacle agent. Just to the grid. (La Aspiradora)
    """
    def __init__(self, unique_id, pos, model):
        super().__init__(pos, model)
        self.pos = pos 
        self.unique_id = unique_id

    def cleaning(self):
        (x, y) = self.pos

        if (isinstance(self.model.grid[x][y], Agent_Floor)):
            if (self.model.grid[x][y].state == "Dirty"):
                self.model.grid[x][y].state = "Clean"
            pass

    def move(self):
        possible_steps = self.model.grid.get_neighborhood(
            self.pos, moore = True, include_center = False)

        freeSpaces = []
        for pos in possible_steps:
            freeSpaces.append(self.model.grid.is_cell_empty(pos))

        if freeSpaces[self.direction]:
            self.model.grid.move_agent(self, possible_steps[self.direction])
        
        pass

    def step(self):
        self.direction = self.random.randint(0,8)
        self.cleaning()
        self.move()

class Agent_Floor(Agent):
    """
    Obstacle agent. Just to add obstacles to the grid. (El piso)
    """ 
    def __init__(self, pos, state, model):
        super().__init__(pos, model)
        self.pos = pos 
        self.state = state 
    def step(self):
        pass