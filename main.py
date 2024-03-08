import tkinter as tk
import customtkinter as ctk
import script
from tkinter import filedialog
from tkinter import messagebox


# fonction 
def Valider():
    try:
        # Récupérer l'année sélectionnée dans la Combobox
        Selctionner_annee = int(anne.get())
        # appel de la fonction pour archiver les fichiers dans le repertoire
        dossier_archive = "Archive"+str(Selctionner_annee)
        sortie = entry_sorti.get()+"\\"+ dossier_archive

        if entry_nomFichier.get():
            sortie = entry_sorti.get()+"\\"+ entry_nomFichier.get()

        script.archiver_fichiers(entry_entre.get(),sortie, Selctionner_annee)
        messagebox.showinfo("confirmation", "operation effectuée avec succes")
    except Exception:
        messagebox.showerror("Echec" ,"Veuillez verifier vos parametres entrés")
def parcourir_dossier():
    entry_entre.delete(0,tk.END)
    entry_entre.insert(0,filedialog.askdirectory())

def parcourir_dossier2():
    entry_sorti.delete(0,tk.END)
    entry_sorti.insert(0,filedialog.askdirectory())


root = ctk.CTk()
# changer le theme de la fenetre
# rajout des annees 
valeurs = ['2024', '2023', '2022', '2021', '2020', '2019', '2018', '2017', '2016', '2015', '2014', '2013', '2012',
           '2011', '2010'
           ]

ctk.set_appearance_mode("dark")

root.geometry("500x500")


frame = ctk.CTkFrame(root, width=480, height=350, fg_color="#444444")
# frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
frame.pack(ipady = 20 , pady = 30)

# Rajout du titre
titre = ctk.CTkLabel(frame, text="TRI FICHERS PAR DATE", fg_color="#444444", font=('arial black', 20))
titre.place(relx = 0.5 , rely = 0.06, anchor=tk.N )

entry_entre=ctk.CTkEntry(frame, placeholder_text="C:\\Users\\DELL\\Documents")
entry_entre.place(relx=0.1, rely=0.2, relwidth=0.85)

bouton = ctk.CTkButton(frame , text="parcourir...",command= parcourir_dossier)
bouton.place(relx=0.95, rely=0.28, anchor = tk.NE)


lbl_nomFichier = ctk.CTkLabel(frame, text="dossier sauvegarde", fg_color="#444444", font=('arial black', 13) )
lbl_nomFichier.place(relx=0.1, rely=0.4)

entry_nomFichier = ctk.CTkEntry(frame,placeholder_text="-- dossier de sauvegard --")
entry_nomFichier.place(relx=0.4, rely=0.4, relwidth=0.55)

entry_sorti=ctk.CTkEntry(frame, placeholder_text="C:\\Users\\DELL\\Documents\\Divers\\")
entry_sorti.place(relx=0.1, rely=0.6, relwidth=0.85)

bouton2 = ctk.CTkButton(frame , text="parcourir...",command= parcourir_dossier2)
bouton2.place(relx=0.95, rely=0.68, anchor = tk.NE)

anne = ctk.CTkComboBox(frame, values=valeurs)
anne.place(relx=0.1, rely=0.8, relwidth=0.85)
# rajout d'une frame pour stabiliser les bouton


footer = ctk.CTkFrame(root,width=480, height=50)
# footer.place(relx=0.5 , rely= 0.8 , anchor=tk.N) 
footer.pack(ipady = 30 , pady = 10)
btn_annuler = ctk.CTkButton(footer, text="Annuler",fg_color="#ff0033" , hover_color="#660033")
btn_annuler.place(relx=0.3, rely=0.8, anchor=tk.SE)

btn_valider = ctk.CTkButton(footer, text="Valider", command=Valider)
btn_valider.place(relx=0.98, rely=0.8, anchor=tk.SE)

root.mainloop()