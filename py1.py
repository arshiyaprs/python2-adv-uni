import requests

class DataStudent:
    def __init__(self):
        response = requests.get("https://cdn.ituring.ir/ex/users.json")
        self._student = response.json()

    def nerdss(self):
        list_student_awill_score = set()
        for stdn in self._student:
            if stdn["score"] > 18.5:
                full_name = f"{stdn["name"]} {stdn["last_name"]}"
                list_student_awill_score.add(full_name)
        return list_student_awill_score

    def sultans(self):
        highest_score = max(stdn["score"] for stdn in self._student)
        highest_scorer_students = tuple(
            f"{stdn["name"]} {stdn["last_name"]}" for stdn in self._student if stdn["score"] == highest_score
        )
        return highest_scorer_students

    def mean(self):
        total_score = sum(stdn["score"] for stdn in self._student)
        number_of_students = len(self._student)
        average_score = total_score / number_of_students if number_of_students > 0 else 0
        return average_score

    def get_students(self):
        student_list = []
        for stdn in self._student:
            student_info = {
                "name": stdn["name"],
                "last_name": stdn["last_name"],
                "score": stdn["score"]
            }
            student_list.append(student_info)
        return student_list