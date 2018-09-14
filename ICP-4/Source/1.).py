class classemp:
  "this is example of employee class"
  empcnt=0
  def __init__(self,ename, fam,dep,sal):
      self.ename=ename
      self.fam=fam
      self.sal=sal
      self.dep=dep
      classemp.empcnt+=1

  def display(self):
      print("name:",self.ename,"\tFamily name:",self.fam,"\tDepartment:",self.dep,"\tsalary:",self.sal)

class fulltimeemp(classemp):
    def __init__(self,n,f,d,s):
        classemp.__init__(self,n,f,d,s)

employee1=classemp("sai","K","cs",1000)
employee2=classemp("indra","K","it",1500)
employee3=classemp("kumar","K","ECE",2000)
employee4=fulltimeemp("nag","K","civil",3000)
employee1.display()
employee2.display()
employee3.display()
employee4.display()
average=((employee1.sal+employee2.sal+employee3.sal+employee4.sal)/classemp.empcnt)
print("Average salary is:",average)
print("total employees", classemp.empcnt)