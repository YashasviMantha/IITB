# Config Statements
from _DUMP import me
me.mark("D")
print("Start -- Debug Stat\n")

# class declarition
class matrix:

    def __init__(self, Lrows = 3, Lcols = 3):
        self.rows = Lrows
        self.cols = Lcols

        self.Matrix  = [[0 for x in range(self.rows)] for y in range(self.cols)]

        print(self.Matrix)

obj = matrix(2,2)
 print(obj.Matrix)



print("\nEnd -- Debug Stat")
