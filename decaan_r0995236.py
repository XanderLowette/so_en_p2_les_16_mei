import random
from verkiezing import Kandidaat, Stem, Kiezer

class DecaanKandidaat(Kandidaat):
    def __init__(self, naam, opleiding):
        super().__init__(naam)
        self.opleiding = opleiding

    def __str__(self):
        return f"{self.naam} ({self.opleiding})"
    
class DecaanStem(Stem):
    def __init__(self, kandidaat, opleiding):
        super().__init__(kandidaat)
        self.opleiding = opleiding

    def __str__(self):
        return f"Stem op {self.kandidaat} ({self.opleiding})"
    
class DecaanKiezer(Kiezer):
    def __init__(self, naam, opleiding):
        super().__init__(naam)
        self.opleiding = opleiding

    def stem(self, kandidaat):
        if kandidaat.opleiding == self.opleiding:
            stem = DecaanStem(kandidaat, self.opleiding)
            kandidaat.geef_stem(stem)
            print(f"{self.naam} heeft gestemd op {kandidaat} ({self.opleiding})")
        else:
            print(f"{self.naam} kan niet stemmen op {kandidaat} ({kandidaat.opleiding})")


lijst_van_kandidaten = [
    DecaanKandidaat("Nero", "Wiskunde"),
    DecaanKandidaat("Einstein", "Natuurkunde"),
    DecaanKandidaat("Openheimer", "Scheikunde"),
    DecaanKandidaat("Darwin", "Biologie"),
    DecaanKandidaat("Johannes", "Informatica")
]
lijst_kiezers = [
    DecaanKiezer("Kasper", "Wiskunde"),
    DecaanKiezer("Milan", "Natuurkunde")]

for kiezer in lijst_kiezers:
    kandidaatnummer = random.randint(0, len(lijst_van_kandidaten) - 1)
    kiezer.stem(lijst_van_kandidaten[kandidaatnummer])