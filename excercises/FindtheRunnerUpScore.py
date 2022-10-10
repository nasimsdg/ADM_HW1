if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr_list = sorted(list(dict.fromkeys(list(arr))))
    print(arr_list[-2])   
    
    
    #for i in range(n):
        
        
