import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("train.csv")

data = data.drop(columns=["Name", "Ticket", "Cabin"])

data["Age"] = data["Age"].fillna(data["Age"].mean())

data["Embarked"] = data["Embarked"].fillna(data["Embarked"].mode()[0])

data["Sex"] = data["Sex"].map({"male": 0, "female": 1})

data["Embarked"] = data["Embarked"].map({"S": 0, "C": 1, "Q": 2})


# survival count
data["Survived"].value_counts().plot(kind="bar")
plt.title("Survival Count")
plt.show()


data["Sex_label"] = data["Sex"].map({0: "Male", 1: "Female"})

data.groupby("Sex_label")["Survived"].mean().plot(kind="bar")

plt.title("Survival Rate by Gender")
plt.xlabel("Gender")
plt.ylabel("Survival Rate")

plt.show()
