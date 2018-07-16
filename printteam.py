print('2017~2018赛季NBA西部联盟前8名')
l = ['火箭','勇士','开拓者','雷霆','爵士','鹈鹕','马刺','森林狼']
for a,b in enumerate(l):
    if a%2 == 0:
        print('')
        print('%s'%b,end='\t')
    else:
        print('%s'%b)
    
