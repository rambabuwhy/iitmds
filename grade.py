
class Grade:


  # term-1: Maths-1, Stats-1, English-1, CT 
  def get_grade_m1s1e1ct(self,m):
    t=  0.1*m[0] + max (((0.6*m[4]) + (0.2*max(m[1], m[2]))), ((0.4*m[4]) + (0.2*m[1]) + (0.3*m[2])))
    e= t+m[5]
    return e,self.cal_grade(e)


  #term-2: maths-2, English-2, Stats-2  
  def get_grade_m2s2e2(self,m):
    t= 0.1*m[0] + max ((0.6*m[4] + 0.2*max(m[1], m[2])),  (0.4*m[4] + 0.2*m[1] + 0.3*m[2])) 
    e=t+m[5]
    return e,self.cal_grade(e)

  #Python  
  def get_grade_python(self,m):
    t=0.1*m[0] + 0.1*m[1]+  max (0.5*m[4] + 0.2*max(m[2], m[3]),  0.4*m[4] + 0.3 *max(m[2],m[3]) + 0.1* min(m[2],m[3]))  
    e=t+ m[5]
    return e,self.cal_grade(e)

  def cal_grade(self, t):
    if 40<=t<50:
      return "E",4
    elif 50<=t<60:
      return "D",6
    elif 60<=t<70:
      return "C",7
    elif 70<=t<80:
      return "B",8
    elif 80<=t<90:
      return "A",9
    elif 90<=t<100:
      return "S",10
    elif t<40:
      return "F",0
    else:
        print("wrong total:",t)
      
  def cumulative_grade(self,g,t):
    sum=0
 
    for i in range(len(g)):
      sum =sum + g[i]

    return sum/t

  def min_max_grade(self,g):

    minl=[]
    maxl=[]
    ol=[]
    
    
    for k,v in g.items():
      
      if v[1] < 7 :
        minl.append((v,k))
        #min_c=k
      elif v[1] > 8 :
        maxl.append((v,k))
      else:
        ol.append((v,k))
        

    return minl,maxl,ol
        
            
    
