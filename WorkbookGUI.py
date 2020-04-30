import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog
from Workbook import Workbook


class WorkbookGUI:
    def __init__(self, workbook):
        self.workbook = workbook
        self.window = tk.Tk()
        self.window.title("Gestionnaire de films")
        self.window.overrideredirect(1)
        w = 500  # width for the Tk root
        h = 600  # height for the Tk root
        ws = self.window.winfo_screenwidth()  # width of the screen
        hs = self.window.winfo_screenheight()  # height of the screen
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        self.window.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.window.configure(background='#AAC0AA')
        main_menu_frame = tk.Frame(self.window)
        main_menu_frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
        btn_add_film = tk.Button(main_menu_frame, text="films", command=self.add_film_frame,
                                 bd=0, activeforeground="#DCEED1", activebackground="#A18276",
                                 bg="#7A918D", fg="#AAC0AA")
        btn_add_film.pack(fill="both", expand="true")
        btn_search_film = tk.Button(main_menu_frame, text="catégories",
                                    bd=0, activeforeground="#DCEED1", activebackground="#A18276",
                                    bg="#7A918D", fg="#AAC0AA")
        btn_search_film.pack(fill="both", expand="true")
        btn_remove_film = tk.Button(main_menu_frame, text="recherche", bd=0, command=self.search_film_frame,
                                    activeforeground="#DCEED1", activebackground="#A18276", bg="#7A918D", fg="#AAC0AA")
        btn_remove_film.pack(fill="both", expand="true")
        btn_add_category = tk.Button(main_menu_frame, text="enregistrer", bd=0,
                                     activeforeground="#DCEED1", activebackground="#A18276", bg="#7A918D", fg="#AAC0AA")
        btn_add_category.pack(fill="both", expand="true")
        btn_exit = tk.Button(main_menu_frame, text="quitter", command=self.exit_ap, bd=0, pady=20,
                             activeforeground="#DCEED1", activebackground="#A18276", bg="#7A918D", fg="#AAC0AA")
        btn_exit.pack(fill="both", expand="true")
        self.window.mainloop()

    def exit_ap(self):
        exit()

    def add_film_frame(self):
        AddFilmGUI(self.workbook)

    def search_film_frame(self):
        SearchFilmGUI(self.workbook)


class AddFilmGUI:  # TODO break down in 3 class : InputFilmGUI, InputFilmGUIAdd, InputFilmGUIEdit (from categ_frame and on)
    def __init__(self, workbook):
        self.workbook = workbook
        self.film_frame = tk.Tk()
        self.film_frame.title("Ajout d'un film")
        self.film_frame.overrideredirect(1)
        w = 500
        h = 700
        ws = self.film_frame.winfo_screenwidth()  # width of the screen
        hs = self.film_frame.winfo_screenheight()  # height of the screen
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        self.film_frame.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.film_frame.configure(background='#AAC0AA')
        main_film_frame = tk.Frame(self.film_frame, background='#AAC0AA')
        main_film_frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
        # frame pour la saisie du titre
        self.title_film_frame = tk.Frame(main_film_frame, background='#7A918D')
        self.title_film_frame.place(relx=0, rely=0, relheight=0.08, relwidth=1)
        self.tittle_label = tk.Label(self.title_film_frame, bg="#7A918D", fg="#AAC0AA", text="Titre : ")
        self.tittle_label.place(relx=0, rely=0, relheight=1, relwidth=0.3)
        self.tittle_entry = tk.Entry(self.title_film_frame, bg="#7A918D", fg="#AAC0AA")
        self.tittle_entry.place(relx=0.3, rely=0, relheight=1, relwidth=0.7)
        # frame pour la saisie de la date de création
        self.year_film_frame = tk.Frame(main_film_frame, background='#7A918D')
        self.year_film_frame.place(relx=0, rely=0.08, relheight=0.08, relwidth=1)
        self.year_label = tk.Label(self.year_film_frame, bg="#7A918D", fg="#AAC0AA", text="Année : ")
        self.year_label.place(relx=0, rely=0, relheight=1, relwidth=0.3)
        self.year_entry = tk.Entry(self.year_film_frame, bg="#7A918D", fg="#AAC0AA")
        self.year_entry.place(relx=0.3, rely=0, relheight=1, relwidth=0.7)
        # frame pour le réalisateur
        self.director_film_frame = tk.Frame(main_film_frame, background='#7A918D')
        self.director_film_frame.place(relx=0, rely=0.18, relheight=0.08, relwidth=1)
        self.director_label = tk.Label(self.director_film_frame, bg="#7A918D", fg="#AAC0AA", text="Réalisateur : ")
        self.director_label.place(relx=0, rely=0, relheight=1, relwidth=0.3)
        self.director_entry = tk.Entry(self.director_film_frame, bg="#7A918D", fg="#AAC0AA")
        self.director_entry.place(relx=0.3, rely=0, relheight=1, relwidth=0.7)
        # frame pour la saisie de trois noms d'acteurs
        self.actors_film_frame = tk.Frame(main_film_frame, background='#7A918D')
        self.actors_film_frame.place(relx=0, rely=0.28, relheight=0.22, relwidth=1)
        self.actors_label = tk.Label(self.actors_film_frame, bg="#7A918D", fg="#AAC0AA", text="Acteurs")
        self.actors_label.place(relx=0, rely=0, relheight=1, relwidth=0.3)
        self.actor1_entry = tk.Entry(self.actors_film_frame, bg="#7A918D", fg="#AAC0AA")
        self.actor1_entry.place(relx=0.3, rely=0, relheight=0.333, relwidth=0.7)
        self.actor2_entry = tk.Entry(self.actors_film_frame, bg="#7A918D", fg="#AAC0AA")
        self.actor2_entry.place(relx=0.3, rely=0.333, relheight=0.333, relwidth=0.7)
        self.actor3_entry = tk.Entry(self.actors_film_frame, bg="#7A918D", fg="#AAC0AA")
        self.actor3_entry.place(relx=0.3, rely=0.666, relheight=0.333, relwidth=0.7)
        # frame pour la catégorie
        self.category_film_frame = tk.Frame(main_film_frame, background='#AAC0AA')
        self.category_film_frame.place(relx=0, rely=0.52, relheight=0.16, relwidth=1)
        self.category_label = tk.Label(self.category_film_frame, bg="#7A918D", fg="#AAC0AA", text="Categorie : ")
        self.category_label.place(relx=0, rely=0, relheight=0.4, relwidth=0.3)
        self.category_combobox = ttk.Combobox(self.category_film_frame, values=list(self.workbook.category_dict.keys()),
                                              state='readonly')
        self.category_combobox.current(0)
        self.category_combobox.place(relx=0.3, rely=0, relheight=0.4, relwidth=0.7)
        self.category_combobox.place(relx=0.3, rely=0, relheight=0.4, relwidth=0.7)
        self.note_label = tk.Label(self.category_film_frame, bg="#7A918D", fg="#AAC0AA", text="Note : ")
        self.note_label.place(relx=0, rely=0.5, relheight=0.4, relwidth=0.3)
        self.rating_combobox = ttk.Combobox(self.category_film_frame, values=list(range(0, 11)), state='readonly')
        self.rating_combobox.place(relx=0.3, rely=0.5, relheight=0.4, relwidth=0.7)
        # frame pour les commentaires
        self.commentary_film_frame = tk.Frame(main_film_frame, background='#7A918D')
        self.commentary_film_frame.place(relx=0, rely=0.68, relheight=0.2, relwidth=1)
        self.commentary_label = tk.Label(self.commentary_film_frame, bg="#7A918D", fg="#AAC0AA", text="commentaires : ")
        self.commentary_label.place(relx=0, rely=0, relheight=0.2, relwidth=1)
        self.commentary_text = tk.Text(self.commentary_film_frame, bg="#7A918D", fg="#AAC0AA")
        self.commentary_text.place(relx=0, rely=0.2, relheight=0.8, relwidth=1)
        # frame pour fermeture de la saisie
        self.buttons_film_frame = tk.Frame(main_film_frame, background='#7A918D')
        self.buttons_film_frame.place(relx=0, rely=0.9, relheight=0.1, relwidth=1)
        self.add_button = tk.Button(self.buttons_film_frame, bg="#7A918D",
                                    fg="#AAC0AA", text="ajouter",
                                    command=self.add_film_ctr)
        self.add_button.place(relx=0, rely=0, relheight=1, relwidth=0.5)
        self.cancel_button = tk.Button(self.buttons_film_frame, bg="#7A918D",
                                       fg="#AAC0AA", text="annuler",
                                       command=self.exit_window)
        self.cancel_button.place(relx=0.5, rely=0, relheight=1, relwidth=0.5)
        self.set_active()

    def add_film_ctr(self):
        self.workbook.add_film(self.category_combobox.get(),  # TODO implement pop up if missing name or year
                               self.tittle_entry.get(),
                               self.year_entry.get(),
                               director=self.director_entry.get(),
                               actors=[self.actor1_entry.get(), self.actor2_entry.get(), self.actor3_entry.get()],
                               rating=self.rating_combobox.get(),
                               comment=self.commentary_text.get('1.0', tk.END))
        self.exit_window()

    def exit_window(self):
        self.film_frame.destroy()

    def set_active(self):
        self.film_frame.lift()
        self.film_frame.focus_force()
        self.film_frame.grab_set()
        self.film_frame.grab_release()


class SearchFilmGUI:
    def __init__(self, workbook):
        self.workbook = workbook
        self.film_frame = tk.Tk()
        self.film_frame.title("Recherche de film")
        self.film_frame.overrideredirect(1)
        w = 500
        h = 700
        ws = self.film_frame.winfo_screenwidth()  # width of the screen
        hs = self.film_frame.winfo_screenheight()  # height of the screen
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        self.film_frame.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.film_frame.configure(background='#AAC0AA')
        main_film_frame = tk.Frame(self.film_frame, background='#AAC0AA')
        main_film_frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
        # frame pour la saisie du titre
        self.title_film_frame = tk.Frame(main_film_frame, background='#7A918D')
        self.title_film_frame.place(relx=0, rely=0, relheight=0.08, relwidth=1)
        self.tittle_label = tk.Label(self.title_film_frame, bg="#7A918D", fg="#AAC0AA", text="Titre : ")
        self.tittle_label.place(relx=0, rely=0, relheight=1, relwidth=0.3)
        self.tittle_entry = tk.Entry(self.title_film_frame, bg="#7A918D", fg="#AAC0AA")
        self.tittle_entry.place(relx=0.3, rely=0, relheight=1, relwidth=0.7)
        # frame pour la saisie de la date de création
        self.year_film_frame = tk.Frame(main_film_frame, background='#7A918D')
        self.year_film_frame.place(relx=0, rely=0.08, relheight=0.08, relwidth=1)
        self.year_label = tk.Label(self.year_film_frame, bg="#7A918D", fg="#AAC0AA", text="Année : ")
        self.year_label.place(relx=0, rely=0, relheight=1, relwidth=0.3)
        self.year_entry = tk.Entry(self.year_film_frame, bg="#7A918D", fg="#AAC0AA")
        self.year_entry.place(relx=0.3, rely=0, relheight=1, relwidth=0.7)
        # frame pour le réalisateur
        self.director_film_frame = tk.Frame(main_film_frame, background='#7A918D')
        self.director_film_frame.place(relx=0, rely=0.18, relheight=0.08, relwidth=1)
        self.director_label = tk.Label(self.director_film_frame, bg="#7A918D", fg="#AAC0AA", text="Réalisateur : ")
        self.director_label.place(relx=0, rely=0, relheight=1, relwidth=0.3)
        self.director_entry = tk.Entry(self.director_film_frame, bg="#7A918D", fg="#AAC0AA")
        self.director_entry.place(relx=0.3, rely=0, relheight=1, relwidth=0.7)
        # frame pour la saisie de trois noms d'acteurs
        self.actors_film_frame = tk.Frame(main_film_frame, background='#7A918D')
        self.actors_film_frame.place(relx=0, rely=0.26, relheight=0.24, relwidth=1)
        self.actors_label = tk.Label(self.actors_film_frame, bg="#7A918D", fg="#AAC0AA", text="Acteurs")
        self.actors_label.place(relx=0, rely=0, relheight=1, relwidth=0.3)
        self.actor1_entry = tk.Entry(self.actors_film_frame, bg="#7A918D", fg="#AAC0AA")
        self.actor1_entry.place(relx=0.3, rely=0, relheight=0.333, relwidth=0.7)
        self.actor2_entry = tk.Entry(self.actors_film_frame, bg="#7A918D", fg="#AAC0AA")
        self.actor2_entry.place(relx=0.3, rely=0.333, relheight=0.333, relwidth=0.7)
        self.actor3_entry = tk.Entry(self.actors_film_frame, bg="#7A918D", fg="#AAC0AA")
        self.actor3_entry.place(relx=0.3, rely=0.666, relheight=0.333, relwidth=0.7)
        # frame pour la catégorie
        self.category_film_frame = tk.Frame(main_film_frame, background='#7A918D')
        self.category_film_frame.place(relx=0, rely=0.52, relheight=0.08, relwidth=1)
        self.category_label = tk.Label(self.category_film_frame, bg="#7A918D", fg="#AAC0AA", text="Categorie : ")
        self.category_label.place(relx=0, rely=0, relheight=0.5, relwidth=0.3)
        self.category_combobox = ttk.Combobox(self.category_film_frame, values=list(self.workbook.category_dict.keys()),
                                              state='readonly')
        self.category_combobox.place(relx=0.3, rely=0, relheight=0.5, relwidth=0.7)
        self.note_label = tk.Label(self.category_film_frame, bg="#7A918D", fg="#AAC0AA", text="Note : ")
        self.note_label.place(relx=0, rely=0.5, relheight=0.5, relwidth=0.3)
        self.rating_combobox = ttk.Combobox(self.category_film_frame, values=list(range(0, 11)), state='readonly')
        self.rating_combobox.place(relx=0.3, rely=0.5, relheight=0.5, relwidth=0.7)
        # frame pour fermeture de la saisie
        self.buttons_film_frame = tk.Frame(main_film_frame, background='#7A918D')
        self.buttons_film_frame.place(relx=0, rely=0.9, relheight=0.1, relwidth=1)
        self.add_button = tk.Button(self.buttons_film_frame, bg="#7A918D",
                                    fg="#AAC0AA", text="Chercher",
                                    command=self.search_film_ctr)
        self.add_button.place(relx=0, rely=0, relheight=1, relwidth=0.5)
        self.cancel_button = tk.Button(self.buttons_film_frame, bg="#7A918D",
                                       fg="#AAC0AA", text="Annuler",
                                       command=self.exit_window)
        self.cancel_button.place(relx=0.5, rely=0, relheight=1, relwidth=0.5)
        self.set_active()

    def search_film_ctr(self):
        kwargs = dict()
        if self.tittle_entry.get():
            kwargs.update(name=self.tittle_entry.get())
        if self.year_entry.get():
            kwargs.update(year=self.year_entry.get())
        if self.director_entry.get():
            kwargs.update(name=self.director_entry.get())
        if self.actor1_entry.get() or self.actor2_entry.get() or self.actor3_entry.get():
            kwargs.update(actors=[entry.get() for entry in
                                  [self.actor1_entry,
                                   self.actor2_entry,
                                   self.actor3_entry] if entry.get()])
        if self.category_combobox.get():
            kwargs.update(category=self.category_combobox.get())
        if self.rating_combobox.get():
            kwargs.update(rating=self.rating_combobox.get())
        if not kwargs:  # TODO popup
            pass
        else:
            DisplayListResultGUISave(self.workbook.find_films(**kwargs))  # TODO Pop-up if no result

    def exit_window(self):
        self.film_frame.destroy()

    def set_active(self):
        self.film_frame.lift()
        self.film_frame.focus_force()
        self.film_frame.grab_set()
        self.film_frame.grab_release()


class DisplayListResultGUI:
    def __init__(self, results_dict):
        self.results_dict = results_dict
        self.result_frame = tk.Tk()
        self.result_frame.title("Recherche de film")
        self.result_frame.overrideredirect(1)
        self.result_frame.geometry('900x300')
        self.result_frame.configure(background='#AAC0AA')
        self.main_result_frame = tk.Frame(self.result_frame, background='#AAC0AA')
        self.main_result_frame.pack(fill=tk.BOTH, padx=15, pady=15, side=tk.TOP)
        cols = ('year', 'category', 'director', 'actors', 'rating', 'comment')
        self.result_table = ttk.Treeview(self.main_result_frame, columns=cols)
        self.result_table.place(relx=0, rely=0, relheight=1, relwidth=1)
        self.result_table.column('#0', width=105, minwidth=105)
        self.result_table.column('year', width=55, minwidth=55)
        self.result_table.column('category', width=105, minwidth=105)
        self.result_table.column('director', width=105, minwidth=105)
        self.result_table.column('actors', width=150, minwidth=105)
        self.result_table.column('rating', width=55, minwidth=105)
        self.result_table.column('comment', width=150, minwidth=105)
        self.result_table.heading('#0', text="Nom", anchor=tk.W)
        self.result_table.heading('year', text="Année", anchor=tk.W)
        self.result_table.heading('category', text="Catégorie", anchor=tk.W)
        self.result_table.heading('director', text="Réalisateur", anchor=tk.W)
        self.result_table.heading('actors', text="Acteurs", anchor=tk.W)
        self.result_table.heading('rating', text="Note", anchor=tk.W)
        self.result_table.heading('comment', text="Commentaire", anchor=tk.W)
        for k, v in results_dict.items():
            self.result_table.insert('', "end", text=k, values=[v.get('year'), v.get('category'),
                                                                v.get('director'),
                                                                list(filter(lambda actor: actor, v.get('actors'))),
                                                                v.get('rating'), v.get('comment')])
        self.result_table.pack(side=tk.TOP, fill=tk.X)

    def set_active(self):
        self.result_frame.lift()
        self.result_frame.focus_force()
        self.result_frame.grab_set()
        self.result_frame.grab_release()

    def exit_window(self):
        self.result_frame.destroy()


class DisplayListResultGUISave(DisplayListResultGUI):  # TODO Pop-up if no result (if not results_dict: popup else: rest of the init)
    def __init__(self, results_dict):
        super().__init__(results_dict)
        self.button_frame = tk.Frame(self.result_frame, background='#AAC0AA')
        self.button_frame.place(relx=0, rely=0.9, relheight=0.1, relwidth=1)
        self.save_button = tk.Button(self.button_frame, bg="#7A918D",
                                     fg="#AAC0AA", text="Sauvegarder",
                                     command=self.save_search)
        self.save_button.place(relx=0.1, rely=0, relheight=.7, relwidth=0.4)
        self.cancel_button = tk.Button(self.button_frame, bg="#7A918D",
                                       fg="#AAC0AA", text="Fermer",
                                       command=self.exit_window)
        self.cancel_button.place(relx=0.5, rely=0, relheight=.7, relwidth=0.4)
        self.set_active()

    def save_search(self):  # TODO implement confirmation pop-up
        path = filedialog.asksaveasfile(initialdir="/", filetypes=[("Fichier CSV", "*.csv")])
        if path:
            Workbook.save_search(path.name + '.csv', self.results_dict)
            self.exit_window()


class DisplayListResultGUIManage(DisplayListResultGUI):  # TODO Pop-up if no result (if not results_dict: popup else: rest of the init),
    def __init__(self, results_dict, workbook):
        super().__init__(results_dict)
        self.button_frame = tk.Frame(self.result_frame, background='#AAC0AA')
        self.button_frame.place(relx=0, rely=0.9, relheight=0.1, relwidth=1)
        self.edit_button = tk.Button(self.button_frame, bg="#7A918D",
                                     fg="#AAC0AA", text="Modifier",
                                     command=self.edit_film)
        self.edit_button.place(relx=0.05, rely=0, relheight=.7, relwidth=0.3)
        self.delete_button = tk.Button(self.button_frame, bg="#7A918D",
                                       fg="#AAC0AA", text="Suprimer",
                                       command=self.delete_film)
        self.delete_button.place(relx=0.35, rely=0, relheight=.7, relwidth=0.3)
        self.cancel_button = tk.Button(self.button_frame, bg="#7A918D",
                                       fg="#AAC0AA", text="Fermer",
                                       command=self.exit_window)
        self.cancel_button.place(relx=0.65, rely=0, relheight=.7, relwidth=0.3)
        self.set_active()

    def edit_film(self):  # TODO implement edit window after AddFilmGUI refactor, will use InputFilmGUIEdit
        pass

    def delete_film(self):  # TODO implement confirmation pop-up Implement
        pass  # TODO Write the thing
        #selected = self.result_table.focus()
        #self.result_table.item(selected).get('text')

class GestionCategGUI:
    # TODO implement add film, edit film, delete film
    def __init__(self):
        pass


class GestionFilmsGUI:
    # TODO implement add categ, delete categ, display categ (will use find film)
    def __init__(self):
        pass


if __name__ == "__main__":
    debug_workbook_gui = WorkbookGUI(Workbook())
