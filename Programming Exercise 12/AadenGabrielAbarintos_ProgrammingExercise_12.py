# AadenGabrielAbarintos_ProgrammingExercise_12.py
# This program uses a CSV file of students' exam grades
# and loads the data into a numpy array. The program then
# prints and calculates the mean, median, standard deviation,
# minimum, and maximum of the students' grades for each exam.
# The program then does the same for all exams combined.
# Then the program determines and prints the total 
# number of students who failed and passed each exam. 
# Finally, the program then calculates and prints the overall 
# pass percentage across all exams.


# Import the numpy module.
import numpy as np


# Create the load_grades function.
def load_grades(file):
    return np.loadtxt(
        file, delimiter=",", skiprows = 1, usecols = (2, 3, 4)
        )


# Create the exam_stats function.
def exam_stats(data):

    # Give the number of exams
    num_exams = data.shape[1]

    # Loop through each exam
    # to check for data.
    for exam in range(num_exams):

        # Get all scores from this specific exam.
        exam_scores = data[:, exam]

        # Calculate the data.
        print(f"Exam {exam + 1} Statistics")
        print("Mean:", np.mean(exam_scores))
        print("Median:", np.median(exam_scores))
        print("Standard Deviation:", np.std(exam_scores))
        print("Minimum:", np.min(exam_scores))
        print("Maximum:", np.max(exam_scores))
        
        # Calculate how many students passed and failed.
        passed = np.sum(exam_scores >= 60)
        failed = np.sum(exam_scores < 60)
        print("Passed:", passed)
        print("Failed:", failed)
        print()


# Create the overall_stats function.
def overall_stats(data):

    # Make the array into a single column.
    flattened = data.flatten()

    # Display the overall data across all exams.
    print("Overall Class Statistics")
    print("Mean:", np.mean(flattened))
    print("Median:", np.median(flattened))
    print("Standard Deviation:", np.std(flattened))
    print("Minimum:", np.min(flattened))
    print("Maximum:", np.max(flattened))
    print()

    # Give the overall pass percentage.
    passed = np.sum(flattened >= 60)
    total = len(flattened)
    pass_percentage = (passed / total) * 100

    print("Overall Pass Percentage:", round(pass_percentage, 2), "%")


# Create the main function.
def main():
    file = "grades.csv"

    # Print the first few rows of data.
    data = load_grades(file)
    print(data[:5])

    # Calculate the data.
    exam_stats(data)
    overall_stats(data)


# Run the main function.
main()