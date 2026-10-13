class Hewan:
    def makan(self):
        print("lagi makan ya?")
        
class Burung(Hewan):
    def terbang(self):
        print("burung terbang wak")
        
class Mamanyalia(Burung):
    def nyusuta(self):
        print("mamalia menyusui le")
        
Meowie = Mamanyalia()
Meowie.nyusuta()
Meowie.makan()
