import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("churn_data.csv")

# Show first rows
print(data.head())

# Churn count
churn_counts = data['Churn'].value_counts()
print(churn_counts)

# Plot churn distribution
churn_counts.plot(kind='bar')
plt.title("Customer Churn Distribution")
plt.xlabel("Churn")
plt.ylabel("Count")
plt.show()
