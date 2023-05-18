import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("room_dataset.csv")
print(data.head())

mean_sound_by_occupancy = data.groupby('Room_Occupancy_Count')['S1_Sound'].mean()
plt.figure(figsize=(10, 6))
mean_sound_by_occupancy.plot(kind='bar', color='steelblue')
plt.xlabel('Occupancy Count')
plt.ylabel('Mean Sound (Volts)')
plt.title('Mean Sound Levels by Occupancy Count (S1_Sound)')
plt.tight_layout()
plt.show()
print("Grouped bar plot of mean sound levels by occupancy count displayed.")

mean_sound_by_occupancy = data.groupby('Room_Occupancy_Count')['S2_Sound'].mean()
plt.figure(figsize=(10, 6))
mean_sound_by_occupancy.plot(kind='bar', color='steelblue')
plt.xlabel('Occupancy Count')
plt.ylabel('Mean Sound (Volts)')
plt.title('Mean Sound Levels by Occupancy Count (S2_Sound)')
plt.tight_layout()
plt.show()
print("Grouped bar plot of mean sound levels by occupancy count displayed.")

mean_sound_by_occupancy = data.groupby('Room_Occupancy_Count')['S3_Sound'].mean()
plt.figure(figsize=(10, 6))
mean_sound_by_occupancy.plot(kind='bar', color='steelblue')
plt.xlabel('Occupancy Count')
plt.ylabel('Mean Sound (Volts)')
plt.title('Mean Sound Levels by Occupancy Count (S3_Sound)')
plt.tight_layout()
plt.show()
print("Grouped bar plot of mean sound levels by occupancy count displayed.")

mean_sound_by_occupancy = data.groupby('Room_Occupancy_Count')['S4_Sound'].mean()
plt.figure(figsize=(10, 6))
mean_sound_by_occupancy.plot(kind='bar', color='steelblue')
plt.xlabel('Occupancy Count')
plt.ylabel('Mean Sound (Volts)')
plt.title('Mean Sound Levels by Occupancy Count (S4_Sound)')
plt.tight_layout()
plt.show()
print("Grouped bar plot of mean sound levels by occupancy count displayed.")