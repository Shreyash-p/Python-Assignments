import pandas as pd
import matplotlib.pyplot as plt

def main():
    border = "*" * 50
    df = pd.read_csv(r"C:\Users\patil\Desktop\Marvellous Infosystem\Machine_Learning\Datasets\student_performance_ml.csv")

    # Q1: Basic Dataset Information
    print("First 5 records:")
    print(df.head())
    print(border)
    print("Last 5 records:")
    print(df.tail())
    print(border)
    print("Dataset Shape (Rows, Columns):")
    print(df.shape)
    print(border)
    print("List of Column Names:")
    print(df.columns)
    print(border)
    print("Dataset Info (Data Types and Non-Null Counts):")
    print(df.info())
    print(border)

    # Q2 & Q3: Summary Statistics & Counts
    print("Total number of students:")
    print(len(df))
    print(border)
    print("Total number of Passed students (FinalResult = 1):")
    print(len(df[df["FinalResult"] == 1]))
    print(border)
    print("Total number of Failed students (FinalResult = 0):")
    print(len(df[df["FinalResult"] == 0]))
    print(border)
    print("Average Study Hours:")
    print(df["StudyHours"].mean())
    print(border)
    print("Average Attendance (%):")
    print(df["Attendance"].mean())
    print(border)
    print("Maximum Previous Score:")
    print(df["PreviousScore"].max())
    print(border)
    print("Minimum Sleep Hours:")
    print(df["SleepHours"].min())
    print(border)

    # Q4: Distribution and Balance Check
    print("Percentage of Passed students (FinalResult = 1):")
    print(df[df["FinalResult"] == 1].value_counts().sum() / df["FinalResult"].value_counts().sum() * 100)
    print(border)
    print("Percentage of Failed students (FinalResult = 0):")
    print(df[df["FinalResult"] == 0].value_counts().sum() / df["FinalResult"].value_counts().sum() * 100)
    print(border)
    print("Dataset Balance Analysis:")
    print("Yes, the dataset is reasonably balanced with a ~60% Pass to 40% Fail ratio.")
    print(border)

    # Q6: Histogram of Study Hours
    plt.figure(figsize=(5, 6))
    # plt.plt(df["StudyHours"].col, df["StudyHours"], width=0.8)
    plt.hist(df["StudyHours"], bins=10, color="orange", edgecolor="black")
    plt.title("Distribution of Study Hours")
    plt.xlabel("Study Hours per Day")
    plt.ylabel("Number of Students")
    plt.show()

    # Q5: Analyzing Impact of Attendance on Final Result
    print("Average Attendance of Passed Students (%):")
    print(df[df["FinalResult"] == 1] [["Attendance"]].mean())
    print(border)
    print("Average Attendance of Failed Students (%):")
    print(df[df["FinalResult"] == 0] [["Attendance"]].mean())
    print(border)

    # Secondary Study Hours Histogram
    plt.hist(df["StudyHours"], bins=10, color="red", edgecolor="black")
    plt.title("Study Hours Histogram Breakdown")
    plt.xlabel("Study Hours per Day")
    plt.ylabel("Frequency")
    plt.show()
    print(border)

    # Q7: Scatter Plot - Passed Students (StudyHours vs PreviousScore / Target)
    plt.scatter(df[df["FinalResult"] == 1] [["StudyHours"]], df[df["FinalResult"] == 1] [["StudyHours"]], marker="x", color="green", edgecolor="green", label="Pass (1)")
    plt.title("Study Hours Analysis - Passed Students")
    plt.xlabel("Study Hours")
    plt.ylabel("Study Hours Benchmark")
    plt.legend()
    plt.show()
    print(border)

    # Q7: Scatter Plot - Failed Students (StudyHours vs PreviousScore / Target)
    plt.scatter(df[df["FinalResult"] == 0] [["StudyHours"]], df[df["FinalResult"] == 0] [["StudyHours"]], marker="o", color="red", edgecolor="green", label="Fail (0)")
    plt.title("Study Hours Analysis - Failed Students")
    plt.xlabel("Study Hours")
    plt.ylabel("Study Hours Benchmark")
    plt.legend()
    plt.show()
    print(border)

    # Q8: Boxplot for Attendance
    plt.boxplot(df['Attendance'])
    plt.title("Boxplot of Student Attendance")
    plt.xlabel("Attendance Variable")
    plt.ylabel("Attendance Percentage (%)")
    plt.show()
    print(border)

    # Q9: Assignments Completed vs Final Result
    plt.scatter(df['FinalResult'], df['AssignmentsCompleted'], color='blue', alpha=0.7)
    plt.title("Assignments Completed vs Final Result")
    plt.xlabel("Final Result (0 = Fail, 1 = Pass)")
    plt.ylabel("Assignments Completed")
    plt.xticks([0, 1], ['Fail (0)', 'Pass (1)'])
    plt.show()
    print(border)

    # Q10: Sleep Hours vs Final Result
    plt.scatter(df['FinalResult'], df['SleepHours'], color='purple', alpha=0.7)
    plt.title("Sleep Hours vs Final Result")
    plt.xlabel("Final Result (0 = Fail, 1 = Pass)")
    plt.ylabel("Sleep Hours per Day")
    plt.xticks([0, 1], ['Fail (0)', 'Pass (1)'])
    plt.show()
    print(border)

if __name__ == "__main__":
    main()