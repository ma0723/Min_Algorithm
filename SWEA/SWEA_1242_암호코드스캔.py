import sys
sys.stdin = open("1242.txt", "r")

code_dic = {
    '0001101' : 0,
    '0011001' : 1,
    '0010011' : 2,
    '0111101' : 3,
    '0100011' : 4,
    '0110001' : 5,
    '0101111' : 6,
    '0111011' : 7,
    '0110111' : 8,
    '0001011' : 9,
}

hex_lst = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

decode = {'112':0, '122':1, '221':2,'114':3, '231':4,'132':5, '411':6, '213':7, '312':8, '211':9}
hex_to_bin = {'0':'0000', '1':'0001', '2':'0010','3':'0011','4':'0100','5':'0101','6':'0110','7':'0111','8':'1000','9':'1001','A':'1010','B':'1011','C':'1100','D':'1101','E':'1110','F':'1111'}

def examine(arr): #검증조건 맞는지
    if ((arr[7]+arr[5]+arr[3]+arr[1])*3 + arr[0]+arr[2]+arr[4]+arr[6]) % 10:
        return False
    return True

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    big_code = [input()[:M] for _ in range(N)]
    visited = []
    ans = 0
    for n in range(N):
        binarified = ''
        for char in big_code[n]:
            binarified += hex_to_bin[char]
        big_code[n] = binarified
    res = []
    for n in range(N):
        f1 = f2 = f3 = 0
        if '1' not in big_code[n]:
            continue
        for m in range(M*4-1,-1,-1):
            if f2 == 0 and f3 == 0 and big_code[n][m] =='1': #첫 1
                f1 += 1
            elif f1 and f3 == 0 and big_code[n][m] == '0': #10
                f2 += 1
            elif f1 and f2 and big_code[n][m] == '1': #101
                f3 += 1
            elif f3 and big_code[n][m] == '0':
                mul = min(f1, f2, f3)
                res.append(decode[str(f1//mul)+str(f2//mul)+str(f3//mul)])
                f1 = f2 = f3 = 0
                if len(res) == 8:
                    if res not in visited:
                        if examine(res):
                            ans += sum(res)
                        visited.append(res)
                    res = []
    print('#{} {}'.format(test_case, ans))