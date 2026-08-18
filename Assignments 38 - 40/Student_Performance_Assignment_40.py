import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score

def main():
    border = "*" * 50
    
    # Load dataset
    csv_path = r"C:\Users\patil\Desktop\Marvellous Infosystem\Machine_Learning\Datasets\student_performance_ml.csv"
    df = pd.read_csv(csv_path)
    
    # Preparing data for initial training
    # Standard features: StudyHours, Attendance, PreviousScore, AssignmentsCompleted, SleepHours
    X = df[["StudyHours", "Attendance", "PreviousScore", "AssignmentsCompleted", "SleepHours"]]
    y = df["FinalResult"]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    
    # Base Model Training
    base_model = DecisionTreeClassifier(random_state=42)
    base_model.fit(X_train, y_train)
    y_pred_base = base_model.predict(X_test)
    base_accuracy = accuracy_score(y_test, y_pred_base)

    print(border)    
    # Q1: Feature Importances
    print("Q1: Feature Importance Scores:")
    importances = base_model.feature_importances_
    for col, imp in zip(X.columns, importances):
        print(f"{col}: {imp:.4f}")
    print(border)
    
    # Q2: Remove SleepHours and Retrain
    X_no_sleep = X.drop(columns=["SleepHours"])
    X_train_ns, X_test_ns, y_train_ns, y_test_ns = train_test_split(X_no_sleep, y, test_size=0.3, random_state=42)
    
    model_no_sleep = DecisionTreeClassifier(random_state=42)
    model_no_sleep.fit(X_train_ns, y_train_ns)
    acc_no_sleep = accuracy_score(y_test_ns, model_no_sleep.predict(X_test_ns))
    
    print("Q2: Performance without 'SleepHours' feature:")
    print(f"Base Model Accuracy (with SleepHours): {base_accuracy * 100:.2f}%")
    print(f"New Model Accuracy (without SleepHours): {acc_no_sleep * 100:.2f}%")
    print(border)
    
    # Q3: Train using only StudyHours and Attendance
    X_limited = df[["StudyHours", "Attendance"]]
    X_train_lim, X_test_lim, y_train_lim, y_test_lim = train_test_split(X_limited, y, test_size=0.3, random_state=42)
    
    model_limited = DecisionTreeClassifier(random_state=42)
    model_limited.fit(X_train_lim, y_train_lim)
    acc_limited = accuracy_score(y_test_lim, model_limited.predict(X_test_lim))
    
    print("Q3: Performance with only StudyHours and Attendance:")
    print(f"Limited Feature Model Accuracy: {acc_limited * 100:.2f}%")
    print(border)
    
    # Q4: Predict for 5 new students
    print("Q4: Predictions for 5 New Students:")
    new_students = pd.DataFrame({
        "StudyHours": [4.5, 2.0, 6.0, 1.5, 5.0],
        "Attendance": [85, 60, 95, 45, 78],
        "PreviousScore": [75, 50, 88, 40, 65],
        "AssignmentsCompleted": [4, 1, 5, 0, 3],
        "SleepHours": [7, 5, 8, 6, 7]
    })
    new_predictions = base_model.predict(new_students)
    new_students["PredictedResult"] = new_predictions
    print(new_students)
    print(border)
    
    # Q5: Manual Accuracy Calculation
    print("Q5: Manual Accuracy Verification:")
    correct_predictions = (y_test == y_pred_base).sum()
    manual_accuracy = correct_predictions / len(y_test)
    print(f"Manual Accuracy Calculation: {manual_accuracy * 100:.2f}%")
    print(f"Sklearn Accuracy Score: {base_accuracy * 100:.2f}%")
    print(border)
    
    # Q6: Misclassified Students Analysis
    print("Q6: Misclassified Rows in Testing Set:")
    misclassified_mask = y_test != y_pred_base
    misclassified_rows = X_test[misclassified_mask].copy()
    misclassified_rows["ActualResult"] = y_test[misclassified_mask]
    misclassified_rows["PredictedResult"] = y_pred_base[misclassified_mask]
    
    print(misclassified_rows)
    print(f"Total misclassified students: {misclassified_mask.sum()}")
    print(border)
    
    # Q7: Compare Testing Accuracy across different random states
    print("Q7: Random State Comparison:")
    for state in [0, 10, 42]:
        X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.3, random_state=state)
        m = DecisionTreeClassifier(random_state=state)
        m.fit(X_tr, y_tr)
        acc = accuracy_score(y_te, m.predict(X_te))
        print(f"Testing Accuracy with random_state={state}: {acc * 100:.2f}%")
    print(border)
    
    # Q8: Decision Tree Visualization
    print("Q8: Generating Decision Tree Visualization...")
    plt.figure(figsize=(15, 10))
    plot_tree(base_model, feature_names=X.columns, class_names=["Fail", "Pass"], filled=True, max_depth=3)
    plt.title("Decision Tree Structure Breakdown")
    plt.show()
    print(border)
    
    # Q9: PerformanceIndex feature
    print("Q9: Evaluation with engineered PerformanceIndex:")
    df["PerformanceIndex"] = (df["StudyHours"] * 2) + df["Attendance"]
    X_engineered = df[["StudyHours", "Attendance", "PreviousScore", "AssignmentsCompleted", "SleepHours", "PerformanceIndex"]]
    
    X_train_eng, X_test_eng, y_train_eng, y_test_eng = train_test_split(X_engineered, y, test_size=0.3, random_state=42)
    model_engineered = DecisionTreeClassifier(random_state=42)
    model_engineered.fit(X_train_eng, y_train_eng)
    acc_engineered = accuracy_score(y_test_eng, model_engineered.predict(X_test_eng))
    print(f"Accuracy with PerformanceIndex included: {acc_engineered * 100:.2f}%")
    print(border)
    
    # Q10: Unconstrained depth model evaluation (max_depth = None)
    print("Q10: Overfitting Evaluation (max_depth=None):")
    overfit_model = DecisionTreeClassifier(max_depth=None, random_state=42)
    overfit_model.fit(X_train, y_train)
    
    train_acc = accuracy_score(y_train, overfit_model.predict(X_train))
    test_acc = accuracy_score(y_test, overfit_model.predict(X_test))
    
    print(f"Training Accuracy: {train_acc * 100:.2f}%")
    print(f"Testing Accuracy: {test_acc * 100:.2f}%")
    print("Explanation: If Training Accuracy is 100% and Testing Accuracy is significantly lower, the tree has overfitted the training data by creating highly specific rules that do not generalize well to unseen test data.")
    print(border)


if __name__ == "__main__":
    main()

