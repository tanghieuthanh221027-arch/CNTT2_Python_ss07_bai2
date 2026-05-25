transaction = "  nguyEN vAn a | PYTHON-01 | 15000000 | paid  "

clean_transaction = transaction.strip()

parts = transaction.split('|')

student_name = parts[0].strip().title()
course_code = parts[1].strip()
amount = parts[2].strip()
status = parts[3].upper().strip()

print(f'''
Họ tên : {student_name}
Khóa học : {course_code}
Số tiền : {amount} VND
Trạng thái : {status}
''')