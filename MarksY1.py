import grade as gr
import display as d


class Marks:
  marks={}



  
  def __init__(self,m):
    global marks
    marks=m

    
  def marks_data(self,c_sum, c_g_map, total_clear_courses):

    global marks
    G=gr.Grade()
      
    print(" \n\n\n-----------------  TERM 1  ------------------\n")

    #Stats -----------------------------------------------
    
    marks_details=marks[0]
    marks_details=marks_details[1:]
    
    marks_details=[int(marks_details[0]),int(marks_details[1]),int(marks_details[2]),int(marks_details[3]),int(marks_details[4]),int(marks_details[5])]
       
    t,g=G.get_grade_m1s1e1ct(marks_details)
    print("\t\tstats 1:    ",g,t)
    
    if g[1] >=4:
      total_clear_courses = total_clear_courses + 1
      c_sum.append(g[1])
      c_g_map['stats1']=g
    
    
    # CT---------------------------------------------------------
    
    marks_details=marks[1]
    marks_details=marks_details[1:]
    marks_details=[int(marks_details[0]),int(marks_details[1]),int(marks_details[2]),int(marks_details[3]),int(marks_details[4]),int(marks_details[5])]
    
    t,g=G.get_grade_m1s1e1ct(marks_details)
    print("\t\tCT :        ",g,t )
    if g[1] >=4:
      total_clear_courses = total_clear_courses + 1
      c_sum.append(g[1])
      c_g_map['ct']=g
    
    
    
    # maths 1---------------------------------------------------------------
    
    marks_details=marks[2]
    marks_details=marks_details[1:]
    
    marks_details=[int(marks_details[0]),int(marks_details[1]),int(marks_details[2]),int(marks_details[3]),int(marks_details[4]),int(marks_details[5])]
    t,g=G.get_grade_m1s1e1ct(marks_details)
    print("\t\tmaths 1:    ",g,t)
    
    if g[1] >=4:
      total_clear_courses = total_clear_courses + 1
      c_sum.append(g[1])
      c_g_map['math1']=g

    
    # english 1------------------------------------------------------------
    
    marks_details=marks[3]
    marks_details=marks_details[1:]
    
    marks_details=[int(marks_details[0]),int(marks_details[1]),int(marks_details[2]),int(marks_details[3]),int(marks_details[4]),int(marks_details[5])]
    t,g=G.get_grade_m1s1e1ct(marks_details)
    print("\t\tenglish 1:  ",g,t)
    
    if g[1] >=4:
      total_clear_courses = total_clear_courses + 1
      c_sum.append(g[1])
      c_g_map['english1']=g
    
    
    
    
    #--------sem 2------------------------------------------------------
    print(" \n\n\n-----------------  TERM 2  ------------------\n")


    
    # python--------------------------------------------------------------
    

    marks_details=marks[4]
    marks_details=marks_details[1:]
    
    marks_details=[int(marks_details[0]),int(marks_details[1]),int(marks_details[2]),int(marks_details[3]),int(marks_details[4]),int(marks_details[5])]
    t,g=G.get_grade_python(marks_details)
    print("\t\tpython:     ",g,t)
    
    if g[1] >=4:
      total_clear_courses = total_clear_courses + 1
      c_sum.append(g[1])
      c_g_map['python']=g
    
    
      
    # maths 2--------------------------------------------------------------------

    
    

    marks_details=marks[5]
    marks_details=marks_details[1:]
    
    marks_details=[int(marks_details[0]),int(marks_details[1]),int(marks_details[2]),int(marks_details[3]),int(marks_details[4]),int(marks_details[5])]
    t,g=G.get_grade_m2s2e2(marks_details)
    print("\t\tmaths 2:    ",g,t)
    
    if g[1] >=4:
      total_clear_courses = total_clear_courses + 1
      c_sum.append(g[1])
      c_g_map['maths2']=g
    
    # stats 2----------------------------------------------------------
      

    
    marks_details=marks[6]
    marks_details=marks_details[1:]
    
    marks_details=[int(marks_details[0]),int(marks_details[1]),int(marks_details[2]),int(marks_details[3]),int(marks_details[4]),int(marks_details[5])]
    
    t,g=G.get_grade_m2s2e2(marks_details)
    print("\t\tstats 2:    ",g,t)
    
    if g[1] >=4:
      total_clear_courses = total_clear_courses + 1
      c_sum.append(g[1])
      c_g_map['stats2']=g
    
    # english 2--------------------------------------------------------
    
    marks_details=marks[6]
    marks_details=marks_details[1:]
    
    marks_details=[int(marks_details[0]),int(marks_details[1]),int(marks_details[2]),int(marks_details[3]),int(marks_details[4]),int(marks_details[5])]
    t,g=G.get_grade_m2s2e2(marks_details)
    print("\t\tenglish 2:  ",g,t)
    
    if g[1] >=4:
      total_clear_courses = total_clear_courses + 1
      c_sum.append(g[1])
      c_g_map['english2']=g





      
    d.summary(c_sum,total_clear_courses, c_g_map)

