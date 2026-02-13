# Logistics-Optimization-Simulation-in-FlexSim
This repository contains a simulation model developed in FlexSim 25.2 to analyze and compare different route optimization strategies in logistics distribution systems in Ecuador. It functions as a configurable base in which parameters can be modified to evaluate different system scenarios.

Model Usage
• To use the FlexSim model, the following is required:
• Have FlexSim version 25.2
• Have Python version 3.10
• Keep the Python algorithms and the base .fm model in the same folder
• Have the Python libraries installed

To make changes, this must be done as follows:
Once the FlexSim model is open, go to the Tools section. In the Process Flow tab, select DemandDispatcher. 
In the Labels section under the function named getMinCostFlow, open “Edit this code.” 
In the part that says external Python, enter the name of the strategy, that is, the name of the desired algorithm to evaluate.

To use the simulation model, follow these steps:

1. Open FlexSim (version 25.2 or higher).

2. Load the model files in a single folder.

3. Select the strategy to evaluate in the model.

4. Run the simulation.

5. Analyze the results obtained during the execution of the model.
Run the simulation.

Analyze the results obtained during the execution of the model.

In the link, the FlexSim program is located.
https://drive.google.com/file/d/18yK_R4OLlU10gb-21rq5U0sGwChcUmYa/view?usp=drive_link
