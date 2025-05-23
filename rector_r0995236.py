from verkiezing import Kandidaat, Stem, Kiezer

class RectorKandidaat(Kandidaat):
    def __init__(self, naam, opleiding):
        super().__init__(naam)
        self.opleiding = opleiding

    def __str__(self):
        return f"{self.naam} ({self.opleiding})"
    
class RectorStem(Stem):
    def __init__(self, kandidaat, opleiding):
        super().__init__(kandidaat)
        self.opleiding = opleiding

    def __str__(self):
        return f"Stem op {self.kandidaat} ({self.opleiding})"
    
class RectorKiezer(Kiezer):
    def __init__(self, naam, opleiding):
        super().__init__(naam)
        self.opleiding = opleiding

    def stem(self, kandidaat):
        if kandidaat.opleiding == self.opleiding:
            stem = RectorStem(kandidaat, self.opleiding)
            kandidaat.geef_stem(stem)
            print(f"{self.naam} heeft gestemd op {kandidaat} ({self.opleiding})")
        else:
            print(f"{self.naam} kan niet stemmen op {kandidaat} ({kandidaat.opleiding})")


lijst_van_kandidaten = [
    RectorKandidaat("Laura", "Bafi"),
    RectorKandidaat("Emma", "engels"),
    RectorKandidaat("Raf", "frans"),
    RectorKandidaat("Jacky", "sport"),
    RectorKandidaat("Paul", "geneeskunde")
]
lijst_kiezers = [
    RectorKiezer("Milan", "engels"),
    RectorKiezer("Mia", "geneeskunde")]

for kiezer in lijst_kiezers:
    for kandidaat in lijst_van_kandidaten:
        kiezer.stem(kandidaat)