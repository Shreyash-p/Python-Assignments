import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay

def main():
    border = "*" * 50
    # ==========================================
    # 1. Dataset Loading & Exploration
    # ==========================================
    df = pd.read_csv(r"C:\Users\patil\Desktop\Marvellous Infosystem\Machine_Learning\Datasets\student_performance_ml.csv")

    print("First 5 records of the dataset:")
    print(df.head())
    print(border)
    print()

    print("Dataset Shape (Rows, Columns):")
    print(df.shape)
    print(border)
    print()

    print("Class Distribution of Target Variable (FinalResult):")
    print(df["FinalResult"].value_counts())
    print(border)
    print()

    # ==========================================
    # 2. Data Analysis & Visualization
    # ==========================================
    # Scatter Plot: StudyHours vs PreviousScore colored by FinalResult
    plt.figure(figsize=(7, 5))
    pass_students = df[df["FinalResult"] == 1]
    fail_students = df[df["FinalResult"] == 0]

    plt.scatter(pass_students["StudyHours"], pass_students["PreviousScore"], color="green", marker="x", label="Pass (1)")
    plt.scatter(fail_students["StudyHours"], fail_students["PreviousScore"], color="red", marker="o", label="Fail (0)")
    
    plt.title("Study Hours vs Previous Score by Result")
    plt.xlabel("Study Hours per Day")
    plt.ylabel("Previous Score")
    plt.legend()
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.show()
    print(border)
    print()

    # ==========================================
    # 3. Train-Test Split
    # ==========================================
    # Separate Features (X) and Target (y)
    X = df[["StudyHours", "Attendance", "PreviousScore", "AssignmentsCompleted", "SleepHours"]]
    y = df["FinalResult"]

    # Split dataset into 80% training and 20% testing
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=42)

    print("Training set size:")
    print(X_train.shape[0])
    print(border)
    print()

    print("Testing set size:")
    print(X_test.shape[0])
    print(border)
    print()

    # ==========================================
    # 4. Model Training & Basic Prediction (Q1 & Q2)
    # ==========================================
    # Create Decision Tree Classifier instance
    model = DecisionTreeClassifier(random_state=42)
    model.fit(X_train, y_train)

    # Predict on test set
    y_pred = model.predict(X_test)

    print("Predicted Values for X_test:")
    print(y_pred)
    print(border)
    print()

    print("Actual Values for X_test:")
    print(y_test.values)
    print(border)
    print()

    # ==========================================
    # 5. Model Accuracy & Evaluation (Q3 & Q5)
    # ==========================================
    test_acc = accuracy_score(y_test, y_pred)
    print("Testing Accuracy (%):")
    print(f"{test_acc * 100:.2f}%")
    print(border)
    print()

    train_acc = accuracy_score(y_train, model.predict(X_train))
    print("Training Accuracy (%):")
    print(f"{train_acc * 100:.2f}%")
    print(border)
    print()

    print("Model Fit Observations (Overfitting / Underfitting):")
    if train_acc == 1.0 and test_acc < train_acc:
        print("Observation: The default decision tree achieves 100% training accuracy. If test accuracy is significantly lower, it indicates overfitting because the unconstrained tree memorized the training noise.")
    else:
        print("Observation: The training and testing accuracies are close, indicating a well-balanced fit.")
    print()

    # ==========================================
    # 6. Confusion Matrix Generation (Q4)
    # ==========================================
    cm = confusion_matrix(y_test, y_pred)
    print("Confusion Matrix:")
    print(cm)
    print(border)
    print()

    # Display visual confusion matrix
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=["Fail (0)", "Pass (1)"])
    disp.plot(cmap=plt.cm.Blues)
    plt.title("Confusion Matrix for Decision Tree")
    plt.show()
    print(border)
    print()

    # ==========================================
    # 7. Hyperparameter Tuning Comparison (max_depth) (Q6)
    # ==========================================
    depths = [1, 3, None]
    print("Comparing Decision Tree Models with Different Max Depths:")
    for depth in depths:
        dt = DecisionTreeClassifier(max_depth=depth, random_state=42)
        dt.fit(X_train, y_train)
        acc = accuracy_score(y_test, dt.predict(X_test))
        print(f"max_depth = {depth} | Test Accuracy: {acc * 100:.2f}%")
    print()
    print("Observation on max_depth:")
    print("- max_depth = 1 (Decision Stump): Often underfits as it splits on only one feature.")
    print("- max_depth = 3: Captures key feature interactions while preventing over-complexity.")
    print("- max_depth = None: Expands tree fully, which risks overfitting on small datasets.")
    print(border)
    print()

    # ==========================================
    # 8. Single Sample Prediction (Q7)
    # ==========================================
    # Student Profile: StudyHours=6, Attendance=85, PreviousScore=66, AssignmentsCompleted=7, SleepHours=7
    custom_student = pd.DataFrame([[6, 85, 66, 7, 7]], columns=X.columns)
    custom_pred = model.predict(custom_student)[0]

    print("Prediction for Custom Student Sample:")
    print(f"Features: StudyHours=6, Attendance=85%, PreviousScore=66, AssignmentsCompleted=7, SleepHours=7")
    print("Predicted Class Code (0 = Fail, 1 = Pass):")
    print(custom_pred)
    print("Final Output Verdict:")
    if custom_pred == 1:
        print("The student is predicted to PASS.")
    else:
        print("The student is predicted to FAIL.")
    print()


if __name__ == "__main__":
    main()