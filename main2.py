class india():
    def capitial(self):
        print("Delhi")
    def language(self):
        print("Hindi")
    def type(self):
        print("Developing country")
class USA():
    def capitial(self):
        print("Washington DC")
    def language(self):
        print("English")
    def type(self):
        print("Developed country")
oi = india()
ou = USA()
for c in [oi, ou]:
    c.capitial()
    c.language()
    c.type()