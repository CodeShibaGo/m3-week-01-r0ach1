def array_diff(a, b):
     arr = []

     for num in a:
         if num in b:
             continue

         arr.append(num)
     return arr