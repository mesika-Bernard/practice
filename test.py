class Person():
    def __init__(self,name,age,job):
        self.name = name
        self.age = age
        self.job = job
        return
        

    def describeperson(self):
        return "Your name is " + self.name + " ," + str(self.age) + " years of age"

bernard = Person("Bernard",25,"Engineer")

print(bernard.describeperson())