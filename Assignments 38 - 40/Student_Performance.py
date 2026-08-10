import pandas as pd
import matplotlib.pyplot as plt

def main():
    df = pd.read_csv(r"C:\Users\patil\Desktop\Marvellous Infosystem\Machine_Learning\Datasets\student_performance_ml.csv")

    # Q1: Basic Dataset Information
    print("First 5 records:")
    print(df.head())
    print("*" * 50)
    print("Last 5 records:")
    print(df.tail())
    print("*" * 50)
    print("Dataset Shape (Rows, Columns):")
    print(df.shape)
    print("*" * 50)
    print("List of Column Names:")
    print(df.columns)
    print("*" * 50)
    print("Dataset Info (Data Types and Non-Null Counts):")
    print(df.info())
    print("*" * 50)

    # Q2 & Q3: Summary Statistics & Counts
    print("Total number of students:")
    print(len(df))
    print("*" * 50)
    print("Total number of Passed students (FinalResult = 1):")
    print(len(df[df["FinalResult"] == 1]))
    print("*" * 50)
    print("Total number of Failed students (FinalResult = 0):")
    print(len(df[df["FinalResult"] == 0]))
    print("*" * 50)
    print("Average Study Hours:")
    print(df["StudyHours"].mean())
    print("*" * 50)
    print("Average Attendance (%):")
    print(df["Attendance"].mean())
    print("*" * 50)
    print("Maximum Previous Score:")
    print(df["PreviousScore"].max())
    print("*" * 50)
    print("Minimum Sleep Hours:")
    print(df["SleepHours"].min())
    print("*" * 50)

    # Q4: Distribution and Balance Check
    print("Percentage of Passed students (FinalResult = 1):")
    print(df[df["FinalResult"] == 1].value_counts().sum() / df["FinalResult"].value_counts().sum() * 100)
    print("*" * 50)
    print("Percentage of Failed students (FinalResult = 0):")
    print(df[df["FinalResult"] == 0].value_counts().sum() / df["FinalResult"].value_counts().sum() * 100)
    print("*" * 50)
    print("Dataset Balance Analysis:")
    print("Yes, the dataset is reasonably balanced with a ~60% Pass to 40% Fail ratio.")
    print("*" * 50)

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
    print("*" * 50)
    print("Average Attendance of Failed Students (%):")
    print(df[df["FinalResult"] == 0] [["Attendance"]].mean())
    print("*" * 50)

    # Secondary Study Hours Histogram
    plt.hist(df["StudyHours"], bins=10, color="red", edgecolor="black")
    plt.title("Study Hours Histogram Breakdown")
    plt.xlabel("Study Hours per Day")
    plt.ylabel("Frequency")
    plt.show()
    print("*" * 50)

    # Q7: Scatter Plot - Passed Students (StudyHours vs PreviousScore / Target)
    plt.scatter(df[df["FinalResult"] == 1] [["StudyHours"]], df[df["FinalResult"] == 1] [["StudyHours"]], marker="x", color="green", edgecolor="green", label="Pass (1)")
    plt.title("Study Hours Analysis - Passed Students")
    plt.xlabel("Study Hours")
    plt.ylabel("Study Hours Benchmark")
    plt.legend()
    plt.show()
    print("*" * 50)

    # Q7: Scatter Plot - Failed Students (StudyHours vs PreviousScore / Target)
    plt.scatter(df[df["FinalResult"] == 0] [["StudyHours"]], df[df["FinalResult"] == 0] [["StudyHours"]], marker="o", color="red", edgecolor="green", label="Fail (0)")
    plt.title("Study Hours Analysis - Failed Students")
    plt.xlabel("Study Hours")
    plt.ylabel("Study Hours Benchmark")
    plt.legend()
    plt.show()
    print("*" * 50)

    # Q8: Boxplot for Attendance
    plt.boxplot(df['Attendance'])
    plt.title("Boxplot of Student Attendance")
    plt.xlabel("Attendance Variable")
    plt.ylabel("Attendance Percentage (%)")
    plt.show()
    print("*" * 50)

    # Q9: Assignments Completed vs Final Result
    plt.scatter(df['FinalResult'], df['AssignmentsCompleted'], color='blue', alpha=0.7)
    plt.title("Assignments Completed vs Final Result")
    plt.xlabel("Final Result (0 = Fail, 1 = Pass)")
    plt.ylabel("Assignments Completed")
    plt.xticks([0, 1], ['Fail (0)', 'Pass (1)'])
    plt.show()
    print("*" * 50)

    # Q10: Sleep Hours vs Final Result
    plt.scatter(df['FinalResult'], df['SleepHours'], color='purple', alpha=0.7)
    plt.title("Sleep Hours vs Final Result")
    plt.xlabel("Final Result (0 = Fail, 1 = Pass)")
    plt.ylabel("Sleep Hours per Day")
    plt.xticks([0, 1], ['Fail (0)', 'Pass (1)'])
    plt.show()
    print("*" * 50)

if __name__ == "__main__":
    main()