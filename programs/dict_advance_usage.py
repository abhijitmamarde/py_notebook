'''
Program to show usage of dict

Reads the i/p from file in below format/stucture:

dates,abhi,score-card,prakash,score-card,vishal,score-card,steve,score-card
20/09/2017,Y,100,Y,80,N,96,Y,40
21/09/2017,Y,80,N,81,Y,56,Y,50
22/09/2017,Y,90,Y,85,N,36,Y,60

which tell whether the student was present (Y/N) on a particular date
and is how many marks he has scored for the day.

The o/p for above sample input:

Student name: abhi
Total days present: 3 i.e. 100.00%
Total score: 270
------------------------------
Student name: prakash
Total days present: 2 i.e. 66.67%
Total score: 246
------------------------------
Student name: vishal
Total days present: 1 i.e. 33.33%
Total score: 188
------------------------------
Student name: steve
Total days present: 3 i.e. 100.00%
Total score: 150
------------------------------
'''

# Reading data from file

# on Window's enter path with '\\' or '/' seprator
# f = open("C:\\Users\\amamarde\\notes\\input.txt", "r")
f = open("C:/Users/amamarde/notes/input.txt", "r")
d = f.read()

recs = d.split('\n')[1:]

st_dict = {}
students = d.split('\n')[0].split(',')[1::2]

for rec in recs:
    actual_fields = rec.split(",")
    fields = actual_fields[1::2]
    tot_fields = actual_fields[2::2]
    for index, field in enumerate(fields):
        if students[index] not in st_dict:
            st_dict[students[index]] = {}
        if field == 'Y':
            st_dict[students[index]]['count'] = st_dict[students[index]].get('count', 0) + 1

        st_dict[students[index]]['total'] = st_dict[students[index]].get('total', 0) + int(tot_fields[index])


for student in students:
    count = st_dict[student]['count']
    total_score = st_dict[student]['total']
    present_pcntg = count / len(recs) * 100
    print('''Student name: %s
Total days present: %d i.e. %.2f%%
Total score: %d''' % (student, count, present_pcntg, total_score))
    print('-'*30)