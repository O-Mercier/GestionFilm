import tkinter as tk, Workbook as wb


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

        btn_add_film = tk.Button(main_menu_frame, text="ajouter un film", command=self.add_film_frame,
                                 bd=0, activeforeground="#DCEED1", activebackground="#A18276",
                                 bg="#7A918D", fg="#AAC0AA")
        btn_add_film.pack(fill="both", expand="true")

        btn_search_film = tk.Button(main_menu_frame, text="chercher un/des film.s", bd=0,
                                    activeforeground="#DCEED1", activebackground="#A18276", bg="#7A918D", fg="#AAC0AA")
        btn_search_film.pack(fill="both", expand="true")

        btn_remove_film = tk.Button(main_menu_frame, text="supprimer un film", bd=0,
                                    activeforeground="#DCEED1", activebackground="#A18276", bg="#7A918D", fg="#AAC0AA")
        btn_remove_film.pack(fill="both", expand="true")

        btn_add_category = tk.Button(main_menu_frame, text="ajouter une catégorie", bd=0,
                                     activeforeground="#DCEED1", activebackground="#A18276", bg="#7A918D", fg="#AAC0AA")
        btn_add_category.pack(fill="both", expand="true")

        btn_manage_category = tk.Button(main_menu_frame, text="gérer les catégories", bd=0,
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


class AddFilmGUI:
    # TODO rating /10
    def __init__(self, workbook):
        self.workbook = workbook
        self.film_frame = tk.Tk()
        self.film_frame.title("ajout d'un film")
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
        title_film_frame = tk.Frame(main_film_frame, background='#7A918D')
        title_film_frame.place(relx=0, rely=0, relheight=0.08, relwidth=1)
        tittle_label = tk.Label(title_film_frame, bg="#7A918D", fg="#AAC0AA", text="titre : ")
        tittle_label.place(relx=0, rely=0, relheight=1, relwidth=0.3)
        tittle_entry = tk.Entry(title_film_frame, bg="#7A918D", fg="#AAC0AA")
        tittle_entry.place(relx=0.3, rely=0, relheight=1, relwidth=0.7)

        # frame pour la saisie de la date de création
        year_film_frame = tk.Frame(main_film_frame, background='#7A918D')
        year_film_frame.place(relx=0, rely=0.08, relheight=0.08, relwidth=1)
        year_label = tk.Label(year_film_frame, bg="#7A918D", fg="#AAC0AA", text="année : ")
        year_label.place(relx=0, rely=0, relheight=1, relwidth=0.3)
        year_entry = tk.Entry(year_film_frame, bg="#7A918D", fg="#AAC0AA")
        year_entry.place(relx=0.3, rely=0, relheight=1, relwidth=0.7)

        # frame pour le réalisateur
        director_film_frame = tk.Frame(main_film_frame, background='#7A918D')
        director_film_frame.place(relx=0, rely=0.18, relheight=0.08, relwidth=1)
        director_label = tk.Label(director_film_frame, bg="#7A918D", fg="#AAC0AA", text="réalisateur : ")
        director_label.place(relx=0, rely=0, relheight=1, relwidth=0.3)
        director_entry = tk.Entry(director_film_frame, bg="#7A918D", fg="#AAC0AA")
        director_entry.place(relx=0.3, rely=0, relheight=1, relwidth=0.7)

        # frame pour la saisie de trois noms d'acteurs
        actors_film_frame = tk.Frame(main_film_frame, background='#7A918D')
        actors_film_frame.place(relx=0, rely=0.26, relheight=0.24, relwidth=1)
        actors_label = tk.Label(actors_film_frame, bg="#7A918D", fg="#AAC0AA", text="acteurs")
        actors_label.place(relx=0, rely=0, relheight=1, relwidth=0.3)
        actor1_entry = tk.Entry(actors_film_frame, bg="#7A918D", fg="#AAC0AA")
        actor1_entry.place(relx=0.3, rely=0, relheight=0.333, relwidth=0.7)
        actor2_entry = tk.Entry(actors_film_frame, bg="#7A918D", fg="#AAC0AA")
        actor2_entry.place(relx=0.3, rely=0.333, relheight=0.333, relwidth=0.7)
        actor3_entry = tk.Entry(actors_film_frame, bg="#7A918D", fg="#AAC0AA")
        actor3_entry.place(relx=0.3, rely=0.666, relheight=0.333, relwidth=0.7)

        # frame pour la catégorie
        category_film_frame = tk.Frame(main_film_frame, background='#7A918D')
        category_film_frame.place(relx=0, rely=0.52, relheight=0.08, relwidth=1)
        category_label = tk.Label(category_film_frame, bg="#7A918D", fg="#AAC0AA", text="categorie : ")
        category_label.place(relx=0, rely=0, relheight=1, relwidth=0.3)
        category_entry = tk.Entry(category_film_frame, bg="#7A918D", fg="#AAC0AA")
        category_entry.place(relx=0.3, rely=0, relheight=1, relwidth=0.7)

        # frame pour les commentaires
        commentary_film_frame = tk.Frame(main_film_frame, background='#7A918D')
        commentary_film_frame.place(relx=0, rely=0.62, relheight=0.2, relwidth=1)
        commentary_label = tk.Label(commentary_film_frame, bg="#7A918D", fg="#AAC0AA", text="commentaires : ")
        commentary_label.place(relx=0, rely=0, relheight=0.2, relwidth=1)
        commentary_text = tk.Text(commentary_film_frame, bg="#7A918D", fg="#AAC0AA")
        commentary_text.place(relx=0, rely=0.2, relheight=0.8, relwidth=1)

        # frame pour fermeture de la saisie
        buttons_film_frame = tk.Frame(main_film_frame, background='#7A918D')
        buttons_film_frame.place(relx=0, rely=0.9, relheight=0.1, relwidth=1)
        add_button = tk.Button(buttons_film_frame, bg="#7A918D", fg="#AAC0AA", text="ajouter")
        add_button.place(relx=0, rely=0, relheight=1, relwidth=0.5)
        add_button.bind("<Button-1>", lambda e: self.add_film_ctr())
        cancel_button = tk.Button(buttons_film_frame, bg="#7A918D", fg="#AAC0AA", text="annuler",
                                  command=self.exit_window)
        cancel_button.place(relx=0.5, rely=0, relheight=1, relwidth=0.5)

        self.setActive()

    def add_film_ctr(self):
        category = self.category_entry.get()
        name = self.tittle_entry.get()
        year = self.year_entry.get()
        add_film_kwargs = dict()
        add_film_kwargs.update('director', self.director_entry.get())
        add_film_kwargs.update('actors', [
            self.actor1_entry.get(),
            self.actor2_entry.get(),
            self.actor3_entry.get()
        ])
        # add_film_kwargs.update('rating', ) TODO: Add rating drop down menu (1-10)
        add_film_kwargs.update('comment', self.commentary_text.get())

        self.workbook.add_film(category, name, year, add_film_kwargs)

    def exit_window(self):
        self.film_frame.destroy()

    def setActive(self):
        self.film_frame.lift()
        self.film_frame.focus_force()
        self.film_frame.grab_set()
        self.film_frame.grab_release()


if __name__ == "__main__":
    debug_workbook_gui = WorkbookGUI(wb.Workbook())
    input()
