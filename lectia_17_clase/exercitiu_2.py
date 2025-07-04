nume_student = "ana"
varsta_student = 20
note_student = [2,9,7,6]

def calucleaza_media(note):
    return sum(note)/len(note)

def afiseaza_student(nume,varsta,note):
    print(f"student: {nume}")
    print(f"varsta: {varsta}")
    print(f"notele: {note}")

functia = (print(afiseaza_student("ion",18,[1,2,4,5])))