import MarksY1 as my1
import display as d



c_sum=[]
c_g_map={}
total_clear_courses=0


f=open('https://raw.githubusercontent.com/rambabuwhy/iitmds/main/marks-sheet.txt', 'r')
marks=[]
for line in f:
  sub,ga,q1,q2,q3,f,ex=line.rstrip('\n').split(',')
  marks.append((sub,ga,q1,q2,q3,f,ex))



d.display_init(marks)
M=my1.Marks(marks)
M.marks_data(c_sum, c_g_map, total_clear_courses)



