from kivy.app import App
from kivy.uix.button import Button
import random

verbes = [
("mordre", "beißen", "beißt", "biss", "hat gebissen", "Ich beiße in den Apfel."),
("rester", "bleiben", "bleibt", "blieb", "ist geblieben", "Er bleibt zu Hause."),
("prospérer", "gedeihen", "gedeiht", "gedieh", "ist gediehen", "Die Pflanzen gedeihen gut."),
("ressembler", "gleichen", "gleicht", "glich", "hat geglichen", "Er gleicht seinem Bruder."),
("glisser", "gleiten", "gleitet", "glitt", "hat geglitten", "Das Boot gleitet ruhig."),
("saisir", "greifen", "greift", "griff", "hat gegriffen", "Er greift den Ball."),
("pincer", "kneifen", "kneift", "kniff", "hat gekniffen", "Sie kneift mich."),
("endurer", "leiden", "leidet", "litt", "hat gelitten", "Er leidet viel."),
("prêter", "leihen", "leiht", "lieh", "hat geliehen", "Ich leihe dir Geld."),
("éviter", "meiden", "meidet", "mied", "hat gemieden", "Er meidet Stress."),

("jeter", "schmeißen", "schmeißt", "schmiss", "hat geschmissen", "Er schmeißt den Ball."),
("écrire", "schreiben", "schreibt", "schrieb", "hat geschrieben", "Ich schreibe einen Brief."),
("crier", "schreien", "schreit", "schrie", "hat geschrien", "Das Kind schreit."),
("monter", "steigen", "steigt", "stieg", "ist gestiegen", "Er steigt hoch."),
("se_disputer", "streiten", "streitet", "stritt", "hat gestritten", "Sie streiten oft."),

("tourner", "biegen", "biegt", "bog", "hat gebogen", "Er biegt links ab."),
("offrir", "bieten", "bietet", "bot", "hat geboten", "Er bietet Hilfe."),
("voler_en_avion", "fliegen", "fliegt", "flog", "ist geflogen", "Wir fliegen nach Berlin."),
("couler", "fließen", "fließt", "floss", "ist geflossen", "Der Fluss fließt."),

("manger", "essen", "isst", "aß", "hat gegessen", "Ich esse."),
("donner", "geben", "gibt", "gab", "hat gegeben", "Ich gebe dir das."),
("lire", "lesen", "liest", "las", "hat gelesen", "Ich lese."),
("voir", "sehen", "sieht", "sah", "hat gesehen", "Ich sehe dich."),

("mourir", "sterben", "stirbt", "starb", "ist gestorben", "Er stirbt."),
("aider", "helfen", "hilft", "half", "hat geholfen", "Ich helfe."),

("commencer", "beginnen", "beginnt", "begann", "hat begonnen", "Es beginnt."),
("gagner", "gewinnen", "gewinnt", "gewann", "hat gewonnen", "Er gewinnt."),
("nager", "schwimmen", "schwimmt", "schwamm", "ist geschwommen", "Ich schwimme."),

("trouver", "finden", "findet", "fand", "hat gefunden", "Ich finde es."),
("chanter", "singen", "singt", "sang", "hat gesungen", "Sie singt."),
("boire", "trinken", "trinkt", "trank", "hat getrunken", "Ich trinke."),

("conduire", "fahren", "fährt", "fuhr", "ist/hat gefahren", "Ich fahre."),
("porter", "tragen", "trägt", "trug", "hat getragen", "Er trägt."),
("grandir", "wachsen", "wächst", "wuchs", "ist gewachsen", "Es wächst."),

("tomber", "fallen", "fällt", "fiel", "ist gefallen", "Er fällt."),
("tenir", "halten", "hält", "hielt", "hat gehalten", "Er hält."),
("dormir", "schlafen", "schläft", "schlief", "hat geschlafen", "Er schläft."),

("courir", "laufen", "läuft", "lief", "ist gelaufen", "Ich laufe."),
("être_assis", "sitzen", "sitzt", "saß", "hat gesessen", "Er sitzt."),
("appeler", "rufen", "ruft", "rief", "hat gerufen", "Sie ruft mich.")
]

class VerbeApp(App):

    def build(self):
        self.button = Button(text="Clique pour voir un verbe")
        self.button.bind(on_press=self.nouveau_verbe)
        return self.button

    def nouveau_verbe(self, instance):
        verbe = random.choice(verbes) 
        self.button.text = f"{verbe[0]} - {verbe[1]} - {verbe[2]}"

VerbeApp().run()
