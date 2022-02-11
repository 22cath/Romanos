gint = 'global'

'''
gint = 'local'
def cambiaVariable(n):
    gint = n

cambiaVariable(7)

print(gint) # imprime local
'''
def cambiaOtraVariable(n):
    gint = n
    print('gint es', gint)
    print('n es n')
   
cambiaOtraVariable('7 local')

print(gint)