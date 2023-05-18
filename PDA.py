import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
data = pd.read_csv("room_dataset.csv")
features_room = data[['S1_Temp','S2_Temp','S3_Temp','S4_Temp','S1_Light', 'S2_Light', 'S3_Light', 'S4_Light' ,'S1_Sound',
                 'S2_Sound','S3_Sound','S4_Sound' ,'S5_CO2','S5_CO2_Slope','S6_PIR','S7_PIR','Room_Occupancy_Count']]
target_data = data['Room_Occupancy_Count']
accuracy_scores = []
for i in range(7):
        X_train, X_test, y_train, y_test = train_test_split(features_room, target_data, test_size=0.2, random_state=i)
        clf = RandomForestClassifier()
        clf.fit(X_train, y_train)
        y_pred = clf.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        accuracy_scores.append(accuracy)
        print(f"Accuracy for Set", i + 1, ":", accuracy)
plt.bar(range(1, 8), accuracy_scores)
plt.xlabel("Set")
plt.ylabel("Accuracy")
plt.title("Accuracy Scores for Different Sets")
plt.show()
