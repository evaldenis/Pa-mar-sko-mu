import tkinter
import tkinter.messagebox
from main_game import *

langas = tkinter.Tk()
langas.title("Pa-mar-sko-mu")

titulinis = tkinter.Message(text="Žaidimas: Akmuo - Popierius - Žirklės", width=1000)

pasirinkimas = tkinter.Label(text="Pasirinkite vieną iš žemiau pateiktų variantų: ")
opcijos = tkinter.Listbox(bg="black",selectbackground="green")
opcijos.insert(1, "Akmuo")
opcijos.insert(2, "Popierius")
opcijos.insert(3, "Žirklės")

def mygtuko_paspaudimas():

    vartotojo_pasirinkimas = opcijos.get(opcijos.curselection())
    kompiuterio_pasirinkimas = random_pasirinkimas()
    laimingas_pasirinkimas = laimetojas(vartotojo_pasirinkimas, kompiuterio_pasirinkimas)

    message = "-------------------\n"
    message += f"\nJūs pasirinkote: {vartotojo_pasirinkimas}\n"
    message += f"\nKompiuteris pasirinko: {kompiuterio_pasirinkimas}\n"
    message += "\n-------------------\n"

    if laimingas_pasirinkimas:
        if laimingas_pasirinkimas == vartotojo_pasirinkimas:
            message += f"\n{'Valio! Jūs laimėjote!'}\n"
        elif laimingas_pasirinkimas == kompiuterio_pasirinkimas:
            message += f"\n{'Nepasisekė, bandyk dar kartą!'}\n"
    else:
        message += f"\n{'Lygiosios! Bandom dar?'}\n"

    message += "\n-------------------\n"
    message += "\nAčiū, kad žaidėte! Žaidžiam dar kartą?\n"

    tkinter.messagebox.showinfo("Rezultatas", message,)

mygtukas = tkinter.Button(text="Žaidžiam!", command=mygtuko_paspaudimas)

#### Supakuojam ####
titulinis.pack()
pasirinkimas.pack()
opcijos.pack()
mygtukas.pack()
langas.mainloop()
