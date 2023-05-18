import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv("room_dataset.csv")
print(data.head())
plt.figure(figsize=(10, 6))
sns.barplot(data=data, x='Time', y='S5_CO2', color='steelblue')
plt.xlabel('Time')
plt.ylabel('CO2 (PPM)')
plt.title('CO2 Concentration Change through the course of 4 Days (S5_CO2)')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()
