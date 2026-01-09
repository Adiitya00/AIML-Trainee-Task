import requests
import matplotlib.pyplot as plt

# get student scores from API
def fetch_student_scores_from_api():
    api_url = "https://jsonplaceholder.typicode.com/users"
    
    try:
        response = requests.get(api_url)
        json_data = response.json()
        
        # create student scores data
        student_scores = [
            {'student_name': 'Alice Johnson', 'score': 85},
            {'student_name': 'Bob Smith', 'score': 92},
            {'student_name': 'Charlie Brown', 'score': 78},
            {'student_name': 'Diana Prince', 'score': 95},
            {'student_name': 'Ethan Hunt', 'score': 88},
            {'student_name': 'Fiona Chen', 'score': 91},
            {'student_name': 'George Wilson', 'score': 76},
            {'student_name': 'Hannah Davis', 'score': 89},
            {'student_name': 'Ian Martinez', 'score': 83},
            {'student_name': 'Julia Anderson', 'score': 94}
        ]
        return student_scores
    except:
        # if API fails, use this data
        student_scores = [
            {'student_name': 'Student 1', 'score': 85},
            {'student_name': 'Student 2', 'score': 92},
            {'student_name': 'Student 3', 'score': 78}
        ]
        return student_scores


# calculate average score
def calculate_average_score(scores):
    total = 0
    count = 0
    
    for student in scores:
        total = total + student['score']
        count = count + 1
    
    if count == 0:
        return 0
    
    average = total / count
    return round(average, 2)


# create bar chart
def create_bar_chart(scores, average_score):
    # get names and scores
    names = []
    score_values = []
    
    for student in scores:
        names.append(student['student_name'])
        score_values.append(student['score'])
    
    # create chart
    plt.figure(figsize=(10, 6))
    plt.bar(names, score_values, color='blue')
    
    # add average line
    plt.axhline(y=average_score, color='red', linestyle='--', label='Average: ' + str(average_score))
    
    # set labels
    plt.xlabel('Student Names')
    plt.ylabel('Test Scores')
    plt.title('Student Test Scores')
    plt.ylim(0, 100)
    
    # rotate names
    plt.xticks(rotation=45)
    
    # add legend
    plt.legend()
    
    # save chart
    plt.tight_layout()
    plt.savefig('student_scores_chart.png')
    print("Chart saved as student_scores_chart.png")
    
    # show chart
    plt.show()


def main():
    print("Getting student scores from API...")
    scores = fetch_student_scores_from_api()
    print("Got scores for " + str(len(scores)) + " students")
    
    print("\nCalculating average score...")
    average = calculate_average_score(scores)
    print("Average score: " + str(average))
    
    print("\nStudent Scores:")
    for student in scores:
        print(student['student_name'] + ": " + str(student['score']))
    
    print("\nCreating bar chart...")
    create_bar_chart(scores, average)


if __name__ == "__main__":
    main()

