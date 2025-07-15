
import matplotlib.pyplot as plt 
import csv
from collections import defaultdict

genes = ["APP", "BACE1",  "PSEN1", "amyloid", "Tau", "Neuron_function"]

state = {
    "APP":4.33,
    "BACE1": 5.2,
    "PSEN1": 3.9,
    "amyloid": 2.533,
    "Tau": 3.43,
    "Neuron_function": 8
}

regulatory_Network = {
    "APP":{"amyloid": "activate"},
    "BACE1":{"amyloid": "activate"},
    "PSEN1":{"amyloid": "activate"},
    "amyloid":{"Tau": "activate"},
    "Tau":{"Neuron_function": "inhibit", "amyloid" : "activate"}
}

def update_state(state, Network): 
    new_state = state.copy()    # copy state
    influence = {gene: [] for gene in genes} # make an empty dict for genes 
    
    for regulator, target in Network.items():
        amyloid = target.get('amyloid', False)
        Tau = target.get('Tau', False)

        if amyloid:
            if target["amyloid"] == "activate":
                influence[regulator].append(1)
            elif target["amyloid"] == "inhibit":
                influence[regulator].append(-1)
        if Tau:
            if target["Tau"] == "activate":
                influence[regulator].append(1)
            elif target["Tau"] == "inhibit":
                influence[regulator].append(-1)

    for gene in genes:
      influence_sum = sum(influence[gene])
      new_state[gene] = max(0, min(10, new_state[gene] + influence_sum))
    return new_state 

history = {gene: [state[gene]] for gene in genes }
########################################################################################################################
data = []
a = r'C:\Users\Hmr13\OneDrive\Desktop\datastuff.csv'
with open(a, mode='r', newline='') as file:
    reader = csv.DictReader(file, delimiter=',')  # Use DictReader for header-to-value mapping
    data = list(reader)  # Convert to list of dictionaries
grouped = defaultdict(list)
for entry in data:
    for key, value in entry.items():
        grouped[key].append(float(value))
grouped_dict = dict(grouped)
averages = {key: sum(values) / len(values) for key, values in grouped_dict.items()}
########################################################################################################################

print(averages) # this is the value you want, if you want to modifiy it, modify the csv file and it will refelect here.


for i in range(25):
     averages = update_state(averages, regulatory_Network)
     for gene in genes:
          history[gene].append(averages[gene])
     

plt.figure(figsize=(10, 8))
plt.plot(history["amyloid"], color ='red', label ='Amyloid (plaques)')
plt.plot(history["Neuron_function"], color ='purple', label ='Neuroal function')
plt.plot(history["Tau"], color ='green', label ='Tau')
plt.plot(history["BACE1"], color ='blue', label ='BACE1')
plt.plot(history["PSEN1"], color ='black', label ='PSEN1')
plt.plot(history["APP"], color ='gray', label ='APP')
plt.xlabel("Time step")
plt.ylabel("activity level")
plt.title("simulation of Alzheimer's in Gene net work")
plt.legend()
plt.grid(True)
plt.show()

