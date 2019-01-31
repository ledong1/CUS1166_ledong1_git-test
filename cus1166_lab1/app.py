from mymodules.math_utils import average_grade
from mymodules.models import Student
def main():
    r=[0,1,2,3,4,5,6,7,8,9]
    r[0]=Student("a",100)
    r[1]=Student("b",94)
    r[2]=Student("c",45)
    r[3]=Student("d",97)
    r[4]=Student("e",76)
    r[5]=Student("f",86)
    r[6]=Student("g",96)
    r[7]=Student("h",99)
    r[8]=Student("i",85)
    r[9]=Student("g",89)
    for each in r:
        each.print_student_info()
    print(f"The average grade of the students is {average_grade(r)}")

if __name__ == "__main__":
    main()
