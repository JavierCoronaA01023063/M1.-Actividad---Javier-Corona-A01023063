from mesa import Agent

class Agent_Vacuum(Agent):
    """
    Obstacle agent. Just to the grid. (La Aspiradora)
    """
    def __init__(self, unique_id, pos, model):
        super().__init__(pos, model)
        self.pos = pos 
        self.unique_id = unique_id
        self.condition = "cleaning"
        self.cleaned = 0

    def cleaning(self):
        (x, y) = self.pos
        cell = self.model.grid.get_cell_list_contents([self.pos])
        if (cell[0].condition == "Dirty"):
            cell[0].condition = "Clean"
            self.cleaned += 1
            return False
        return True

    def move(self):
        possible_steps = self.model.grid.get_neighborhood(
            self.pos, moore = True, include_center = False)

        self.direction = self.random.randint(0, len(possible_steps)-1)
        self.model.grid.move_agent(self, possible_steps[self.direction])
        
    def step(self):
        self.cleaning()
        self.move()

class Agent_Floor(Agent):
    """
    Obstacle agent. Just to add obstacles to the grid. (El piso)
    """ 
    def __init__(self, pos, model):
        super().__init__(pos, model)
        self.pos = pos 
        self.condition = "Dirty"
    def step(self):
        pass