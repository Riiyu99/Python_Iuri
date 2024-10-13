class FizzBuzzs: 

    def __init__(self,nom):
        self.nom = nom 


    def affiche(self, n1, n2):
        result=""
        for i in range(1,n +1):
            if i % 15 == 0:
                result+="FrisBee"
            elif i % 5 == 0:
                result+="Buzz"
            elif i % 3 == 0:
                result+="Fizz"
            else:
                result+=str(i)

        print(result)
        return result




    