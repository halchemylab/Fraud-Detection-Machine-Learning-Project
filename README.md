# Fraud Detection Machine Learning Project

## Overview
This project is a machine learning-based solution for detecting fraudulent financial transactions. It includes:
- Data analysis and visualization in a Jupyter notebook (`analysis.ipynb`)
- A trained fraud detection model
- An interactive Streamlit web app for real-time fraud prediction

## Dataset
**Source:** [Kaggle - Fraud Detection Dataset](https://www.kaggle.com/datasets/amanalisiddiqui/fraud-detection-dataset?resource=download)

**Note:** The dataset is too large to be included in this repository. **Please download `fraud_dataset.csv` manually from the link above and place it in the project root directory.**

## Project Structure

```
├── analysis.ipynb                # Data exploration, visualization, and model training
├── data_utils.py                 # Utility functions for data processing
├── fraud_dataset.csv             # (User-provided) Transaction dataset
├── fraud_detection_app.py        # Streamlit web application for fraud prediction
├── fraud_detection_model.pkl     # Trained machine learning model
├── README.md                     # Project documentation
```

## Setup Instructions

1. **Clone the repository:**
   ```sh
   git clone https://github.com/halchemylab/Fraud-Detection-Machine-Learning-Project.git
   cd Fraud-Detection-Machine-Learning-Project
   ```

2. **Download the dataset:**
   - Go to the [Kaggle dataset page](https://www.kaggle.com/datasets/amanalisiddiqui/fraud-detection-dataset?resource=download)
   - Download `fraud_dataset.csv` and place it in the project root directory.

3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
   If `requirements.txt` is missing, install the following packages manually:
   ```sh
   pip install pandas numpy matplotlib seaborn scikit-learn streamlit joblib
   ```

4. **Run the Streamlit app:**
   ```sh
   streamlit run fraud_detection_app.py
   ```

## Usage

### Data Analysis
- Open `analysis.ipynb` in Jupyter or VS Code to explore the data, visualize trends, and see the model training process.

### Fraud Detection Web App
- Launch the app as described above.
- Enter transaction details in the web interface to get a fraud prediction and probability.
- The app also compares your input to dataset averages for context.

## Model
- The model is trained using logistic regression with preprocessing pipelines.
- Features include transaction type, amount, sender/receiver balances, and engineered features.
- The trained model is saved as `fraud_detection_model.pkl`.

## File Descriptions
- `analysis.ipynb`: Full EDA, feature engineering, and model training notebook.
- `fraud_detection_app.py`: Streamlit app for user-friendly fraud prediction.
- `data_utils.py`: Helper functions for data statistics and preprocessing.
- `fraud_detection_model.pkl`: Serialized trained model (required for the app).

## Notes
- The dataset is highly imbalanced; model metrics and thresholds should be interpreted accordingly.
- For best results, ensure all dependencies are installed and the dataset is in the correct location.

## License
This project is for educational purposes. Please check the dataset's license on Kaggle for usage restrictions.