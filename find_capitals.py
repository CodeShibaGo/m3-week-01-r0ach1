def find_capitals(word):
        if len(word) == 0:
            return ''

        ans = ''
        for char in word:
            #temp = ord(char)
            #if (temp >= 65 and temp <= 90):
            if char.isupper():
               ans += char
        return ans


