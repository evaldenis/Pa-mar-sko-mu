import random
import codecs
codecs.encode("A strange character","utf-8")


def random_pasirinkimas(options=["Akmuo", "Popierius", "Žirklės"]):
    return random.choice(options)

def laimetojas(pasirinkimas_1, pasirinkimas_2):

    if pasirinkimas_1 == pasirinkimas_2:
       nugalejo = None 
    else:
       pasirinkimai = [pasirinkimas_1, pasirinkimas_2]
       pasirinkimai.sort()

       if pasirinkimai == ["Akmuo", "Popierius"]:
           nugalejo = "Popierius"
       elif pasirinkimai == ["Popierius", "Žirklės"]:
           nugalejo = "Žirklės"
       elif pasirinkimai == ["Akmuo", "Žirklės"]:
           nugalejo = "Akmuo"
       else:
           print("Klaida!")

    return nugalejo