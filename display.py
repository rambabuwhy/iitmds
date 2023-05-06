

import grade as gr
def display_init(marks):
    print('\n\n================================================== \n')
    print('\n        Provisional Certificate')
    
    print('      iit madras bs in data science'.upper())
    f=open('marks-sheet.text', 'r')

    marks=[]
    for line in f:
      sub,ga,q1,q2,q3,f,ex=line.rstrip('\n').split(',')
      #print(sub,ga,q1,q2,q3,f,ex)
      marks.append((sub,ga,q1,q2,q3,f,ex))




    print('\n\n----------------- Marks Summary ---------------------\n')
    for i in marks:
      print("\t\t",i)
    #f.close()
    print('\n-----------------------------------------------------\n')

def summary(c_sum, total_clear_courses, c_g_map):

    G=gr.Grade()
      
    print("\n\n\n------------------ SUMMARY -------------------")

    print('\n\t\tName: Rambabu, \n\t\tFrom: Aug 2021 \n\t\tEmailId:22f2001364@ds.study.iitm.ac.in')
    #print("----------------------------------------------")
    print("\n\t\tTotal grade:  ",G.cumulative_grade(c_sum,total_clear_courses))
    print("\t\tTotal cleared courses:   ", total_clear_courses)
    
    min_grade, max_grade, others=G.min_max_grade(c_g_map)
    print("\t\tMin grade:   ", min_grade)
    print("\t\tMax grade:   ", max_grade)
    print("\t\tOthers grade:   ", others)
    print("\n\n\n\t\tCGPA:   ***** ",G.cumulative_grade(c_sum,total_clear_courses),'  *****')
    print("----------------------------------------------")