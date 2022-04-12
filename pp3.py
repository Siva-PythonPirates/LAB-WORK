print('Can attend the exam' if ((1-int(input('Absent days :'))/int(input('Working days :'))))*100 >75 else 'Cannot attend the exam')
