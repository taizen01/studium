exam_details= [
{'student_id' : 1, "midterm" : 70, "endterm" : 82},
{'student_id' : 2, "midterm" : 73, "endterm" : 74},
{'student_id' : 3, "midterm" : 75, "endterm" : 86}
]


def get_averages(list_of_dicts):
    for i in list_of_dicts:
        final = (i["midterm"]+i["endterm"])/2
        i['final'] = final
        i.pop('midterm')
        i.pop('endterm')
    return list_of_dicts


print(get_averages(exam_details))