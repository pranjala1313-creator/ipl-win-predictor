

# 🏏 IPL Win Predictor

A Machine Learning web application that predicts the **winning probability of an IPL team during a run chase** based on the current match situation.

The project uses historical IPL match data to train a classification model and provides an interactive interface built with **Streamlit**.

## 🚀 Live Demo

👉 **[https://ipl-win-predictor-ml-model.streamlit.app](#)**

## 📌 Project Overview

The IPL Win Predictor estimates the probability of the chasing team winning a match based on factors such as:

* Batting Team
* Bowling Team
* Venue/City
* Runs Left
* Balls Left
* Wickets Remaining
* Current Run Rate (CRR)
* Required Run Rate (RRR)
* Target Score

The model returns the probability of:

* 🟢 **Winning**
* 🔴 **Losing**

The prediction is updated based on the current match situation.

## 🧠 Machine Learning Approach

This project follows a complete machine learning pipeline:

```text
Raw IPL Dataset
      ↓
Data Cleaning & Preprocessing
      ↓
Feature Engineering
      ↓
Train/Test Split
      ↓
Machine Learning Model
      ↓
Model Evaluation
      ↓
Pickle Model Pipeline
      ↓
Streamlit Application
      ↓
Win Probability Prediction
```

### Feature Engineering

Several match-specific features were derived from the raw ball-by-ball data:

| Feature        | Description                    |
| -------------- | ------------------------------ |
| `runs_left`    | Runs still required to win     |
| `balls_left`   | Number of deliveries remaining |
| `wickets`      | Wickets remaining              |
| `crr`          | Current Run Rate               |
| `rrr`          | Required Run Rate              |
| `total_runs_x` | Target score                   |
| `batting_team` | Team currently batting         |
| `bowling_team` | Team currently bowling         |
| `city`         | Match venue/city               |

## 🤖 Model

The project uses a **classification model** to estimate the probability of the chasing team winning.

A Scikit-learn pipeline is used to combine preprocessing and model prediction:

```python
pipe.predict_proba(input_data)
```

The trained pipeline is serialized using **Pickle** and loaded by the Streamlit application for real-time predictions.

## 🖥️ Streamlit Application

The Streamlit interface allows the user to enter/select the current match situation.

### Inputs

* Batting Team
* Bowling Team
* City
* Target Score
* Current Score
* Overs Completed
* Wickets Lost

The application then calculates the relevant features and displays the predicted:

```text
Winning Probability
Losing Probability
```

## 📊 Match Progression

The application also visualizes how the predicted win probability changes as the innings progresses.

This provides a graphical representation of the match situation and shows how factors such as runs scored and wickets lost influence the prediction.

## 🛠️ Technologies Used

* **Python**
* **Pandas** – Data manipulation
* **NumPy** – Numerical computations
* **Scikit-learn** – Machine Learning
* **Matplotlib** – Data visualization
* **Streamlit** – Web application
* **Pickle** – Model serialization
* **Jupyter Notebook** – Model development and experimentation

## 📂 Project Structure

```text
IPL-Win-Predictor/
│
├── app.py
├── pipe.pkl
├── requirements.txt
├── README.md
│
├── notebooks/
│   └── IPL_Win_Predictor.ipynb
│
└── data/
    └── deliveries.csv
```

> File and folder names can be modified according to the actual project structure.

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/IPL-Win-Predictor.git
cd IPL-Win-Predictor
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
```

### 3. Activate the environment

**Mac/Linux:**

```bash
source .venv/bin/activate
```

**Windows:**

```bash
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Streamlit application

```bash
streamlit run app.py
```

The application will be available at:

```text
http://localhost:8501
```

## 📈 Example Prediction

For a hypothetical match situation:

```text
Batting Team: Mumbai Indians
Bowling Team: Chennai Super Kings

Target: 190
Current Score: 120
Overs: 15
Wickets Lost: 3
```

The application processes the current match state and produces an estimated:

```text
Winning Probability: XX%
Losing Probability: XX%
```

*The probabilities depend on the trained model and the input match situation.*

## 🔍 Key Learning Outcomes

Through this project, I worked with:

* Ball-by-ball cricket data
* Data preprocessing
* Feature engineering
* Classification
* Scikit-learn pipelines
* Probability prediction using `predict_proba()`
* Model serialization using Pickle
* Pandas and NumPy
* Data visualization
* Streamlit application development
* Deploying a Machine Learning model as an interactive web application

## 🔮 Future Improvements

Potential improvements include:

* Incorporating player-level statistics
* Including toss and innings information
* Adding player form and historical performance
* Using more advanced models
* Improving probability calibration
* Adding live match data
* Deploying the application publicly
* Adding model performance metrics and prediction confidence

## 👨‍💻 Author

**Pranjal Awasthi**

Aspiring Machine Learning Engineer | IIT Delhi

---

⭐ If you found this project interesting, feel free to star the repository!

