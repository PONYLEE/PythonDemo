
print("test号")


seq1 = ['hello','good','boy','doiido']
sql=f'''{",".join(seq1+['aaa'])} || ccc'''

print(sql)
