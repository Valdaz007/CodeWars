class RomanNumerals:
    romnum = {"M":1000, "CM":900, "D":500, "CD":400, "C":100, "XC":90, "L":50, "XL":40, "X":10, "IX":9, "V":5, "IV":4, "I": 1}
    
    @staticmethod
    def to_roman(val : int) -> str:
        romlist=[]
        while val != 0:
            for i in RomanNumerals.romnum: 
                if RomanNumerals.romnum[i] <= val: 
                    val-=RomanNumerals.romnum[i]
                    romlist.append(i)
                    break
        return "".join(romlist)
    
    @staticmethod
    def from_roman(roman_num : str) -> int:
        rom_sum = RomanNumerals.romnum[roman_num[-1]]
        
        for i,j in zip(roman_num[1:],roman_num[:-1]):
            if RomanNumerals.romnum[i] <= RomanNumerals.romnum[j]:
                rom_sum+=RomanNumerals.romnum[j]
            else:
                rom_sum-=RomanNumerals.romnum[j]
        return rom_sum
    
print(RomanNumerals.from_roman("MCMI"))