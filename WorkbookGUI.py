import tkinter as tk
import tkinter.ttk as ttk
import Workbook as Wb


class WorkbookGUI:
    # TODO change mainmenu to gerer films, gerer categorie, recherche, enregister (call save workbook), quitter
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

        btn_add_film = tk.Button(main_menu_frame, text="ajouter un film", command=self.add_film_frame,
                                 bd=0, activeforeground="#DCEED1", activebackground="#A18276",
                                 bg="#7A918D", fg="#AAC0AA")
        btn_add_film.pack(fill="both", expand="true")

        btn_search_film = tk.Button(main_menu_frame, text="chercher un/des film.s", command=self.seach_film_frame,
                                    bd=0, activeforeground="#DCEED1", activebackground="#A18276",
                                    bg="#7A918D", fg="#AAC0AA")
        btn_search_film.pack(fill="both", expand="true")

        btn_remove_film = tk.Button(main_menu_frame, text="supprimer un film", bd=0,
                                    activeforeground="#DCEED1", activebackground="#A18276", bg="#7A918D", fg="#AAC0AA")
        btn_remove_film.pack(fill="both", expand="true")

        btn_add_category = tk.Button(main_menu_frame, text="ajouter une catégorie", bd=0,
                                     activeforeground="#DCEED1", activebackground="#A18276", bg="#7A918D", fg="#AAC0AA")
        btn_add_category.pack(fill="both", expand="true")

        btn_manage_category = tk.Button(main_menu_frame, text="gérer les catégories", bd=0, #
                                        activeforeground="#DCEED1", activebackground="#A18276", bg="#7A918D",
                                        fg="#AAC0AA")
        btn_manage_category.pack(fill="both", expand="true")

        btn_create_list = tk.Button(main_menu_frame, text="créer une liste", bd=0,
                                    activeforeground="#DCEED1", activebackground="#A18276", bg="#7A918D", fg="#AAC0AA")
        btn_create_list.pack(fill="both", expand="true")

        btn_exit = tk.Button(main_menu_frame, text="quitter", command=self.exit_ap, bd=0, pady=20,
                             activeforeground="#DCEED1", activebackground="#A18276", bg="#7A918D", fg="#AAC0AA")
        btn_exit.pack(fill="both", expand="true")

        self.window.mainloop()

    def exit_ap(self):
        exit()

    def add_film_frame(self):
        AddFilmGUI(self.workbook)

    def seach_film_frame(self):
        SearchFilmGUI(self.workbook)

    @staticmethod
    def pop_up_msg(title, text):
        popup = tk.Tk(background='#7A918D')
        popup.wm_title(title)
        label = ttk.Label(popup, text=text)
        label.pack(side="top", fill="x", pady=10)
        b1 = ttk.Button(popup, text="Ok", command=popup.destroy)
        b1.pack()
        popup.mainloop()


class AddFilmGUI:
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
        self.category_combobox.current(0)
        self.category_combobox.place(relx=0.3, rely=0, relheight=0.5, relwidth=0.7)
        self.note_label = tk.Label(self.category_film_frame, bg="#7A918D", fg="#AAC0AA", text="Note : ")
        self.note_label.place(relx=0.3, rely=0.5, relheight=0.5, relwidth=0.7)
        self.rating_combobox = ttk.Combobox(self.category_film_frame, values=list(range(0, 11)), state='readonly')
        self.rating_combobox.place(relx=0.3, rely=0.5, relheight=0.5, relwidth=0.7)
        # frame pour les commentaires
        self.commentary_film_frame = tk.Frame(main_film_frame, background='#7A918D')
        self.commentary_film_frame.place(relx=0, rely=0.62, relheight=0.2, relwidth=1)
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
        self.workbook.add_film(self.category_combobox.get(),
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
        self.category_combobox.current(0)
        self.category_combobox.place(relx=0.3, rely=0, relheight=0.5, relwidth=0.7)
        self.note_label = tk.Label(self.category_film_frame, bg="#7A918D", fg="#AAC0AA", text="Note : ") # TODO Label not working
        self.note_label.place(relx=0, rely=0.5, relheight=0.5, relwidth=0.7)
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
            kwargs.update(year=self.tittle_entry.get())
        if self.director_entry.get():
            kwargs.update(name=self.tittle_entry.get())
        if self.actor1_entry.get() or self.actor2_entry.get() or self.actor3_entry.get():
            kwargs.update(actors=[self.actor1_entry.get(), self.actor2_entry.get(), self.actor3_entry.get()])
        if self.rating_combobox.get():
            kwargs.update(rating=self.rating_combobox.get())
        DisplayListResultGUI(self.workbook.find_films(kwargs))

    def exit_window(self):
        self.film_frame.destroy()

    def set_active(self):
        self.film_frame.lift()
        self.film_frame.focus_force()
        self.film_frame.grab_set()
        self.film_frame.grab_release()


class DisplayListResultGUI:
    def __init__(self, results):  # TODO implement listbox treeview or grid, implement save to csv option
        self.result_frame = tk.Tk()
        self.result_frame.title("Recherche de film")
        self.result_frame.overrideredirect(1)
        w = 600
        h = 500
        ws = self.result_frame.winfo_screenwidth()  # width of the screen
        hs = self.result_frame.winfo_screenheight()  # height of the screen
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        self.result_frame.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.result_frame.configure(background='#AAC0AA')
        main_result_frame = tk.Frame(self.result_frame, background='#AAC0AA')
        main_result_frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
        cols = ('Nom', 'Année', 'Catégorie', 'Réalisateur', 'Acteurs', 'Note', 'Commentaire')
        result_table = ttk.Treeview(main_result_frame, columns=cols, show='headings')
        for col in cols:
            result_table.heading(col, text=col)
        result_table.grid(row=1, column=0, columnspan=2)
        for k, v in results.items():
            result_table.insert("", "end", values=(k, v.get('year'),v.get('category'),
                                                   v.get('director'),v.get('director'),
                                                   v.get('actors'), v.get('comment')))
        self.set_active()

    def exit_window(self):
        self.result_frame.destroy()

    def set_active(self):
        self.result_frame.lift()
        self.result_frame.focus_force()
        self.result_frame.grab_set()
        self.result_frame.grab_release()





class GestionCategGUI:
    # TODO implement add film, edit film, delete film
    def __init__(self):
        pass


class GestionFilmsGUI:
    # TODO implement add categ, delete categ, display categ (will use find film)
    def __init__(self):
        pass



if __name__ == "__main__":
    debug_workbook_gui = WorkbookGUI(Wb.Workbook())
