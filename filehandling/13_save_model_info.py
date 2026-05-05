



import pickle

# Example model result dictionary
model_data = {
    "model_name": "Customer Churn Model",
    "accuracy": 0.91,
    "features": ["age", "salary", "usage"]
}

with open("model.pkl", "wb") as file:
    pickle.dump(model_data, file)

print("Model information saved")