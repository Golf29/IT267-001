#สร้างฟัวก์ชั่น เปิด-ปิดไฟ
#เปิด
def turnon():
    global switch_status
    switch_status = True
#ปิด
def turnoff():
    global switch_status
    switch_status = False

switch_status = False

print(f'status = {switch_status}')
turnon()
print(f'status = {switch_status}')
turnoff()
print(f'status = {switch_status}')
turnoff()
print(f'status = {switch_status}')