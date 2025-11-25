# 🌾 Crop Prediction System 🌾

A simple GUI-based application that predicts the best crop to plant based on soil moisture, temperature, and humidity data using machine learning.

## 📋 Features

- **Machine Learning Model**: Uses Random Forest Classifier trained on crop data.
- **GUI Interface**: User-friendly Tkinter-based interface for easy input and prediction.
- **Real-time Prediction**: Enter sensor values and get instant crop recommendations.
- **Accuracy Display**: Shows model accuracy for transparency.

## 🛠️ Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/KGFCH2/Crop-Prediction.git
   cd Crop-Prediction
   ```

2. **Install dependencies**:
   Make sure you have Python installed. Then install required packages:
   ```bash
   pip install pandas scikit-learn
   ```

3. **Prepare data**:
   Place your `crop_data.csv` file in the project directory. The CSV should have columns: `moisture`, `temperature`, `humidity`, `crop`.

## 🚀 Usage

1. Run the application:
   ```bash
   python test.py
   ```

2. The GUI window will open, displaying model accuracy.

3. Enter values for:
   - Soil Moisture (%)
   - Temperature (°C)
   - Humidity (%)

4. Click **"Predict Crop"** to get the recommended crop.

## 📊 Example

- Input: Moisture=34%, Temperature=20°C, Humidity=57%
- Output: Recommended crop: Paddy 🌱

## 📁 Project Structure

- `test.py`: Main application script with model training and GUI.
- `crop_data.csv`: Dataset for training the model (not included; provide your own).
- `README.md`: This file.

## 🤝 Contributing

Feel free to fork and contribute! Open issues for bugs or feature requests.

## 📄 License

This project is open-source. Use it freely for educational purposes.

---

Made with ❤️ for smart farming! 🌱