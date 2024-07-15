class Solution:
    def numberToWords(self,num):
        if num == 0:
            return "Zero"

        digits = {
            1: "One", 
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",
            10: "Ten",
            11: "Eleven",
            12: "Twelve",
            13: "Thirteen",
            14: "Fourteen",
            15: "Fifteen",
            16: "Sixteen",
            17: "Seventeen",
            18: "Eighteen",
            19: "Nineteen"
        }
        tens = {
            20: "Twenty",
            30: "Thirty",
            40: "Forty",
            50: "Fifty",
            60: "Sixty",
            70: "Seventy",
            80: "Eighty",
            90: "Ninety"
        }
        places = {
            0: "",
            1: "Thousand",
            2: "Million",
            3: "Billion",
            4: "Trillion"
        }

        
        def chunk_name(num):
            name = []
            if num//100:
                name.append(digits[num//100])
                name.append("Hundred")
                num = num%100
            
            if num < 20 and num >0:
                name.append(digits[num])
                return name
                
            elif num>=20:
                name.append(tens[num//10 * 10])
                num = num % 10

            if num:
                name.append(digits[num])
            
            return name

        numbers = []
        while num:
            numbers.append(num%1000)
            num = num//1000
        # numbers.reverse()


        name = list(map(chunk_name, numbers))

        for i in range(len(name)):
            if name[i]:
                name[i].append(places[i])

        name.reverse()
        name  = [item for sublist in name for item in sublist if item]
        name = " ".join(name)
        
        return name
