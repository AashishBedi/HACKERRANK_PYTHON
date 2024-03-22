#Note: Largest element may repeat
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    unique_arr = list(set(arr))   #Helps to remove duplicates 
    
    unique_arr.sort()
    print(unique_arr[-2])