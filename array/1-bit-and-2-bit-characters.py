class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        
        # valid representation 0, 10, 11
        # invalid representation 1, 01
        if bits[-1] != 0:
            return False
        valid = True
        both = True
        i = 1
        while(i<len(bits)):
            print("i: ",i,"length of bits: ",len(bits))
            if bits[i-1] == 0:
                print(bits[i-1])
                i+=1
            elif bits[i-1] == 1:
                print(bits[i-1])
                print("i: ",i,"length of bits: ",len(bits))
                if i < len(bits)-1:
                    if bits[i] == 1:
                        print(bits[i])
                        i+=2
                    else:
                        print(bits[i])
                        i+=2
                else:
                    return False
        
        return True