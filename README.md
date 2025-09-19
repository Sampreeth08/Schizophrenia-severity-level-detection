# Schizophrenia-severity-level-detection
 This project aims at predicting the Schizophrenia severity level by analyzing a  dataset comprising of the above mentioned observable and Testable symptoms, using  decision Tree classification with different levels of depth. 

 This project is a mini application for storing, analyzing, and predicting schizophrenia symptoms using a GUI built with PyQt5 and machine learning models.

## Features

- **Observable Symptoms Input:** Enter observable symptoms via a GUI and store them in a SQLite database.
- **Testable Symptoms Input:** Enter testable symptoms via a GUI and store them in a SQLite database.
- **CSV Export:** Export database tables to CSV files for further analysis.
- **Decision Tree Analysis:** Run decision tree classifiers on the dataset to predict schizophrenia severity.
- **Data Visualization:** (Optional) Visualize results and predictions.

## Project Structure

- `Python/` — Python scripts for GUI, database operations, and ML models.
- `data/` — CSV datasets for training and testing.
- `ui/` — Qt Designer `.ui` files for GUI layouts.
- `schizo1` — SQLite database file.
- `generic_7040.txt` — SQL schema for database tables.

## How to Run

1. **Install Requirements:**
   - Python 3.x
   - PyQt5
   - scikit-learn
   - pandas
   - numpy

2. **Start the Main GUI:**
   ```sh
   python Python/schiz1.py
   ```

3. **Use the GUI to:**
   - Enter symptoms and store them in the database.
   - Export CSV files.
   - Run decision tree analysis.

## Main Scripts

- [`Python/schiz1.py`](Python/schiz1.py): Main application launcher.
- [`Python/obsymps1.py`](Python/obsymps1.py): Observable symptoms input.
- [`Python/testsymps1.py`](Python/testsymps1.py): Testable symptoms input.
- [`Python/createcsv1h.py`](Python/createcsv1h.py): Export database tables to CSV with headers.
- [`Python/dtc3.py`](Python/dtc3.py), [`Python/dtc4.py`](Python/dtc4.py): Decision tree classifiers.

## Data

- [`data/schizoset.csv`](data/schizoset.csv): Main dataset for ML analysis.
- [`data/obsymps1.csv`](data/obsymps1.csv), [`data/testsymps1.csv`](data/testsymps1.csv): Exported symptom data.
