from mesa.visualization.modules import CanvasGrid, ChartModule, PieChartModule
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.UserParam import UserSettableParameter
from agent import Agent_Vacuum, Agent_Floor
from model import RandomModel

colors = {"Clean": "#a8a3ef", "Dirty": "#aaaaaa"}

def agent_portrayal(agent):
    
    portrayal = {"Filled": "true"}

    if (isinstance(agent, Agent_Vacuum)):
        portrayal["Shape"] = "circle"
        portrayal["Color"] = "red"
        portrayal["r"] = 1
        portrayal["Layer"] = 1

    else:
        portrayal["Shape"] = "rect"
        portrayal["w"] = 1
        portrayal["h"] = 1
        portrayal["Color"] = colors[agent.condition]
        portrayal["Layer"] = 0


    return portrayal

tree_chart = ChartModule(
    [{"Label": label, "Color": color} for (label, color) in colors.items()]
)


model_params = {"Cleaner": UserSettableParameter("slider", "Number of Vacuum cleaners", 2, 1, 10, 1),
                "trash": UserSettableParameter ("slider", "Number of Cleaners", 5, 1, 10, 1),
                "width": 10,"height": 10,
                "density": UserSettableParameter("slider", "Density Dirty", 0.6, 0.1, 0.9, 0.1),
                "max_time": UserSettableParameter("slider", "Max Time", 200, 1, 400, 1)}

grid = CanvasGrid(agent_portrayal, 10, 10, 500, 500)
server = ModularServer(RandomModel, [grid, tree_chart], "Random Vacuum", model_params)
                       
server.port = 8521 # The default
server.launch()