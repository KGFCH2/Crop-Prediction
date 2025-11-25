import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import tkinter as tk
from tkinter import messagebox

# 1. Load CSV
data = pd.read_csv("crop_data.csv")

# 2. Separate features and labels
X = data[["moisture", "temperature", "humidity"]]
y = data["crop"]

# 3. Encode crop names as numbers
le = LabelEncoder()
y_encoded = le.fit_transform(y)

# 4. Split for testing (optional but good for report)
X_train, X_test, y_train, y_test = train_test_split(
    X, y_encoded, test_size=0.2, random_state=42
)

# 5. Train Random Forest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 6. Check accuracy (for Result & Discussion)
accuracy = model.score(X_test, y_test)
print("Model accuracy:", accuracy)

# 7. Function to predict crop from user input
def predict_crop(moisture, temperature, humidity):
  features = pd.DataFrame([[moisture, temperature, humidity]], columns=["moisture", "temperature", "humidity"])
  pred_encoded = model.predict(features)[0]
  crop_name = le.inverse_transform([pred_encoded])[0]
  return crop_name

# GUI Application
class CropPredictorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Crop Prediction System")
        self.root.geometry("400x300")

        # Accuracy Label
        self.accuracy_label = tk.Label(root, text=f"Model Accuracy: {accuracy:.2f}")
        self.accuracy_label.pack(pady=10)

        # Input Fields
        tk.Label(root, text="Soil Moisture (%):").pack()
        self.moisture_entry = tk.Entry(root)
        self.moisture_entry.pack()

        tk.Label(root, text="Temperature (°C):").pack()
        self.temp_entry = tk.Entry(root)
        self.temp_entry.pack()

        tk.Label(root, text="Humidity (%):").pack()
        self.humidity_entry = tk.Entry(root)
        self.humidity_entry.pack()

        # Predict Button
        self.predict_button = tk.Button(root, text="Predict Crop", command=self.predict)
        self.predict_button.pack(pady=10)

        # Result Label
        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

    def predict(self):
        try:
            moisture = float(self.moisture_entry.get())
            temperature = float(self.temp_entry.get())
            humidity = float(self.humidity_entry.get())
            crop = predict_crop(moisture, temperature, humidity)
            self.result_label.config(text=f"Recommended Crop: {crop}")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers for all fields.")

# Run the GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = CropPredictorApp(root)
    root.mainloop()
