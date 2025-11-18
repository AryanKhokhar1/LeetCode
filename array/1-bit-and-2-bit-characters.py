class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        
        # valid representation 0, 10, 11
        # invalid representation 1, 01
        if bits[-1] != 0:
            return False
        i = 1
        while(i<len(bits)):
            if bits[i-1] == 0:
                i+=1
            elif bits[i-1] == 1:
                if i < len(bits)-1:
                    if bits[i] == 1:
                        i+=2
                    else:
                        i+=2
                else:
                    return False
        
        return True