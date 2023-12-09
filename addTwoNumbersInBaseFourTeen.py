def getNumeralValue(num) :
 
    if( num >= '0' and num <= '9') :
        return ord(num) - ord('0')
    if( num >= 'A' and num <= 'D') :
        return ord(num ) - ord('A') + 10
 
def getNumeral(val):
 
    if( val >= 0 and val <= 9):
        return chr(val + ord('0'))
    if( val >= 10 and val <= 14) :
        return chr(val + ord('A') - 10)
 def sumBase14(num1, num2):
 
    l1 = len(num1)
    l2 = len(num2)
    carry = 0
         
    if(l1 != l2) :
     
        print("Function doesn't support numbers of different"
                " lengths. If you want to add such numbers then"
                " prefix smaller number with required no. of zeroes")
     
    res = [0]*(l1 + 1)
             
    for i in range(l1 - 1, -1, -1):
        nml1 = getNumeralValue(num1[i])
        nml2 = getNumeralValue(num2[i])
        res_nml = carry + nml1 + nml2;
        if(res_nml >= 14) :
            carry = 1
            res_nml -= 14
        else:
            carry = 0
        res[i+1] = getNumeral(res_nml)
    if(carry == 0):
        return (res + 1)
    res[0] = '1'
    return res
 
if __name__ == "__main__":
     
    num1 = "DC2"
    num2 = "0A3"
 
    print("Result is ",end="")
    res = sumBase14(num1, num2)
    for i in range(len(res)):
        print(res[i],end="")