if __name__ == '__main__':
    info = list()
    grade = list()
    grade_wmin = list()
    info_dict = dict()
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        info.append([name,score])
        grade.append(score)
        
    minimum_grade = min(grade)
    for i in grade:
        if i != minimum_grade:
           grade_wmin.append(i)
            
    info_dict = dict(info)
    grade_wmin = sorted(grade_wmin)
    
    for k,v in sorted(info_dict.items()):
        if v == grade_wmin[0]:
            print(k)

    
    
 
