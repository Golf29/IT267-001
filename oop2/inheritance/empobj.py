from empit import EmpIT
from empmkt import EmpMKT

#create object empolyee IT
mike = EmpIT("001","Mike",60000)
mike.add_skill("Python,Javasrcipt")
mike.add_experience(5)
mike.emp_detail()
mike.it_salary()


#create object empolyee MKT
anna = EmpMKT("002","Anna",35000)
anna.emp_detail()
anna.mkt_salary()

#พนักงานเเผนการตลาดชื่อ Paul มีเงินเดือน 45000 ได้รับคอมมิชชั่น 35% โดยทำงานอยู่จังหวัดเชียงใหม่
paul = EmpMKT("003","Paul",45000)
paul.add_commision(35)
paul.add_location("Chiang Mai")
paul.emp_detail()
paul.mkt_salary()