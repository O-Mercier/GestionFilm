import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog
from Workbook import Workbook

GAINSBORO = "#E8EDDF"
IVORY = "#E8EDDF"
MAIZE = "#F5CB5C"
RAISIN_BLACK = "#242423"
JET = "#333533"

HELV_30_BUTTON_FONT = "Helvetica, 30"
HELV_20_BUTTON_FONT = "Helvetica, 20"
HELV_15_FONT = "Helvetica, 15"
FUTURA_30_FONT = "Futura, 30"
FUTURA_20_FONT = "Futura, 20"
FUTURA_15_FONT = "Futura, 15"
FUTURA_10_FONT = "Futura, 10"


class MenuGUI:
    def __init__(self, workbook):  # Construit la fenetre de menu et demare le thread tkinter
        self.workbook = workbook
        self.window = tk.Tk()
        self.window.title("Gestionnaire de films")
        ws = self.window.winfo_screenwidth()  # width of the screen
        hs = self.window.winfo_screenheight()  # height of the screen
        h = ws / 2
        w = ws / 2
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        self.window.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.window.configure(background=RAISIN_BLACK)
        main_menu_frame = tk.Frame(self.window, bg=RAISIN_BLACK)
        main_menu_frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
        self.btn_category = tk.Button(main_menu_frame, text="catégories", command=self.open_manage_category,
                                      bd=2, activeforeground=RAISIN_BLACK, activebackground=MAIZE,
                                      bg=RAISIN_BLACK, fg=GAINSBORO, font=HELV_30_BUTTON_FONT)
        self.btn_category.place(relx=0, rely=0, relwidth=1, relheight=0.27)

        self.btn_research = tk.Button(main_menu_frame, text="recherche et gestion", command=self.open_workbook,
                                      bd=2, activeforeground=RAISIN_BLACK, activebackground=MAIZE,
                                      bg=RAISIN_BLACK, fg=GAINSBORO, font=HELV_30_BUTTON_FONT)
        self.btn_research.place(relx=0, rely=0.37, relwidth=1, relheight=0.27)

        self.btn_exit = tk.Button(main_menu_frame, text="quitter", command=self.exit_ap,
                                  bd=2, activeforeground=RAISIN_BLACK, activebackground=MAIZE,
                                  bg=RAISIN_BLACK, fg=GAINSBORO, font=HELV_30_BUTTON_FONT)
        self.btn_exit.place(relx=0, rely=0.73, relwidth=1, relheight=0.27)
        self.window.mainloop()

    def exit_ap(self):  # ferme le programe et enregistre
        def exit_cmd():  # Inner fucntion a passer en objet au pop-up
            self.workbook.save_workbook
            exit()

        AlertPopUP(text='Quitter et enregister? \n',
                   btn1_text='oui',
                   btn1_command=exit_cmd)

    def open_workbook(self):  # ouvre une instance de WorkbookGUI
        WorkbookGUI(self.workbook)

    def open_manage_category(self):  # ouvre une instance de GestionCategGUI
        GestionCategGUI(self.workbook)


class AlertPopUP:  # Classe qui construit un pop up d'avertissement ou de validation en fonction des kwargs
    def __init__(self, text, **kwargs):
        """
        :param kwargs:
            btn1_text=String
            btn1_command=function
        """
        self.popup = tk.Tk()
        self.popup.overrideredirect(1)
        self.popup.configure(bg=MAIZE)
        ws = self.popup.winfo_screenwidth()  # width of the screen
        hs = self.popup.winfo_screenheight()  # height of the screen
        h = ws / 4
        w = ws / 4
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        self.popup.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.popup_frame = tk.Frame(self.popup, bg=MAIZE)
        self.popup_frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
        if 'btn1_text' in kwargs:
            def btn1_cmd():
                kwargs.get('btn1_command')()
                self.popup.destroy()

            btn1_text = kwargs.get('btn1_text')
            btn1_y = 0.74
            btn1_heigth = 0.27
            self.B2 = tk.Button(self.popup_frame, text='annuler', command=self.popup.destroy,
                                activeforeground=RAISIN_BLACK, activebackground=MAIZE,
                                bg=RAISIN_BLACK, fg=MAIZE, font=HELV_20_BUTTON_FONT)
            self.B2.place(relx=0, rely=0.37, relwidth=1, relheight=0.27)
            label_height = 0.27
        else:
            btn1_text = "ok"
            btn1_y = 0.55
            btn1_heigth = 0.45
            btn1_cmd = self.popup.destroy
            label_height = 0.45
        self.B1 = tk.Button(self.popup_frame, text=btn1_text, command=btn1_cmd,
                            activeforeground=RAISIN_BLACK, activebackground=MAIZE,
                            bg=RAISIN_BLACK, fg=MAIZE, font=HELV_20_BUTTON_FONT)
        self.B1.place(relx=0, rely=btn1_y, relwidth=1, relheight=btn1_heigth)
        self.label = tk.Label(self.popup_frame, text=text, bg=MAIZE, fg=RAISIN_BLACK, anchor=tk.CENTER,
                              font=FUTURA_20_FONT)
        self.label.place(relx=0, rely=0, relwidth=1, relheight=label_height)
        print('\a')
        self.popup.mainloop()
        set_active(self.popup)


class WorkbookGUI:  # Ouvre une instance du gestionaire de film interactif
    def __init__(self, workbook):
        self.workbook = workbook
        self.parameter_dict = dict()
        self.result_dict = dict()
        self.workbook_frame = tk.Tk()
        self.workbook_frame.title("Recherche de film")
        ws = self.workbook_frame.winfo_screenwidth()  # width of the screen
        hs = self.workbook_frame.winfo_screenheight()  # height of the screen
        h = hs
        w = ws
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        self.workbook_frame.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.workbook_frame.configure(background=RAISIN_BLACK)
        self.main_frame = tk.Frame(self.workbook_frame, background=RAISIN_BLACK)
        self.main_frame.place(relx=0.1, rely=0.1, relheight=0.8, relwidth=0.8)
        cols = ('year', 'category', 'director', 'actors', 'rating')
        self.search_result_frame = tk.Frame(self.main_frame, background=RAISIN_BLACK)
        self.search_result_frame.place(relx=0.4, rely=0, relwidth=0.6, relheight=0.8)
        style = ttk.Style(self.workbook_frame)
        style.element_create("Custom.Treeheading.border", "from", "default")
        style.layout("Custom.Treeview.Heading", [("Custom.Treeheading.cell", {'sticky': 'nswe'}),
                                                 ("Custom.Treeheading.border", {'sticky': 'nswe', 'children': [
                                                     ("Custom.Treeheading.padding", {'sticky': 'nswe', 'children': [
                                                         ("Custom.Treeheading.image", {'side': 'right', 'sticky': ''}),
                                                         ("Custom.Treeheading.text",
                                                          {'side': 'left', 'sticky': 'we'})]})]}), ])
        style.configure("Custom.Treeview.Heading", background=GAINSBORO,
                        foreground=RAISIN_BLACK, font=HELV_15_FONT, relief="flat", anchor=tk.CENTER)
        style.map("Custom.Treeview.Heading",
                  relief=[('active', 'groove'), ('pressed', 'sunken')])
        style.configure("Custom.Treeview", fieldbackground=GAINSBORO, fieldforeground=RAISIN_BLACK, font=FUTURA_10_FONT,
                        background=GAINSBORO, foreground=RAISIN_BLACK, anchor=tk.CENTER)
        self.result_tree = ttk.Treeview(self.search_result_frame, columns=cols, style="Custom.Treeview")
        self.result_tree.place(relx=0, rely=0, relwidth=1, relheight=1)
        header_w = round(((ws / 2) * 0.8) / 6)
        self.result_tree.column('#0', width=header_w, minwidth=header_w)
        self.result_tree.column('year', width=header_w, minwidth=header_w)
        self.result_tree.column('category', width=header_w, minwidth=header_w)
        self.result_tree.column('director', width=header_w, minwidth=header_w)
        self.result_tree.column('actors', width=header_w, minwidth=header_w)
        self.result_tree.column('rating', width=header_w, minwidth=header_w)
        self.result_tree.heading('#0', text="Nom", anchor=tk.W)
        self.result_tree.heading('year', text="Année", anchor=tk.W)
        self.result_tree.heading('category', text="Catégorie", anchor=tk.W)
        self.result_tree.heading('director', text="Réalisateur", anchor=tk.W)
        self.result_tree.heading('actors', text="Acteurs", anchor=tk.W)
        self.result_tree.heading('rating', text="Note", anchor=tk.W)
        self.search_frame = tk.Frame(self.main_frame, background=RAISIN_BLACK)
        self.search_frame.place(relx=0, rely=0, relwidth=0.35, relheight=0.8)
        self.title_film_frame = tk.Frame(self.search_frame, background=RAISIN_BLACK)
        self.title_film_frame.place(relx=0, rely=0, relwidth=1, relheight=0.05)
        self.tittle_label = tk.Label(self.title_film_frame, bg=RAISIN_BLACK, fg=GAINSBORO, font=FUTURA_15_FONT,
                                     text="titre", anchor="w")
        self.tittle_label.place(relx=0, rely=0, relwidth=0.3, relheight=1)
        self.tittle_entry = tk.Entry(self.title_film_frame, bg=RAISIN_BLACK, fg=GAINSBORO, font=FUTURA_15_FONT,
                                     justify='center')
        self.tittle_entry.place(relx=0.3, rely=0, relwidth=0.7, relheight=1)
        # frame pour la saisie de la date de création
        self.year_film_frame = tk.Frame(self.search_frame, background=RAISIN_BLACK)
        self.year_film_frame.place(relx=0, rely=0.1, relwidth=1, relheight=0.05)
        self.year_label = tk.Label(self.year_film_frame, bg=RAISIN_BLACK, fg=GAINSBORO, font=FUTURA_15_FONT,
                                   text="année", anchor="w")
        self.year_label.place(relx=0, rely=0, relwidth=0.3, relheight=1)
        self.year_entry = tk.Entry(self.year_film_frame, bg=RAISIN_BLACK, fg=GAINSBORO, font=FUTURA_15_FONT,
                                   justify='center')
        self.year_entry.place(relx=0.3, rely=0, relwidth=0.7, relheight=1)
        # frame pour le réalisateur
        self.director_film_frame = tk.Frame(self.search_frame, background=RAISIN_BLACK)
        self.director_film_frame.place(relx=0, rely=0.2, relwidth=1, relheight=0.05)
        self.director_label = tk.Label(self.director_film_frame, bg=RAISIN_BLACK, fg=GAINSBORO, font=FUTURA_15_FONT,
                                       text="réalisateur", anchor="w")
        self.director_label.place(relx=0, rely=0, relwidth=0.3, relheight=1)
        self.director_entry = tk.Entry(self.director_film_frame, bg=RAISIN_BLACK, fg=GAINSBORO, font=FUTURA_15_FONT,
                                       justify='center')
        self.director_entry.place(relx=0.3, rely=0, relwidth=0.7, relheight=1)
        # frame pour la saisie de trois noms d'acteurs
        self.actors_film_frame = tk.Frame(self.search_frame, background=RAISIN_BLACK)
        self.actors_film_frame.place(relx=0, rely=0.3, relwidth=1, relheight=0.15)
        self.actors_label = tk.Label(self.actors_film_frame, bg=RAISIN_BLACK, fg=GAINSBORO, font=FUTURA_15_FONT,
                                     text="acteurs", anchor="w")
        self.actors_label.place(relx=0, rely=0, relwidth=0.3, relheight=1)
        self.actor1_entry = tk.Entry(self.actors_film_frame, bg=RAISIN_BLACK, fg=GAINSBORO, font=FUTURA_15_FONT,
                                     justify='center')
        self.actor1_entry.place(relx=0.3, rely=0, relwidth=0.7, relheight=0.33)
        self.actor2_entry = tk.Entry(self.actors_film_frame, bg=RAISIN_BLACK, fg=GAINSBORO, font=FUTURA_15_FONT,
                                     justify='center')
        self.actor2_entry.place(relx=0.3, rely=0.33, relwidth=0.7, relheight=0.33)
        self.actor3_entry = tk.Entry(self.actors_film_frame, bg=RAISIN_BLACK, fg=GAINSBORO, font=FUTURA_15_FONT,
                                     justify='center')
        self.actor3_entry.place(relx=0.3, rely=0.66, relwidth=0.7, relheight=0.33)
        # frame pour la catégorie
        self.category_film_frame = tk.Frame(self.search_frame, background=RAISIN_BLACK)
        self.category_film_frame.place(relx=0, rely=0.5, relwidth=1, relheight=0.05)
        style.map('TCombobox', fieldbackground=[('readonly', RAISIN_BLACK)])
        style.map('TCombobox', fieldforeground=[('readonly', GAINSBORO)])
        style.map('TCombobox', background=[('readonly', GAINSBORO)])
        style.map('TCombobox', foreground=[('readonly', GAINSBORO)])
        style.map('TCombobox', selectbackground=[('readonly', RAISIN_BLACK)])
        style.map('TCombobox', selectforeground=[('readonly', GAINSBORO)])
        self.category_label = tk.Label(self.category_film_frame, bg=RAISIN_BLACK, fg=GAINSBORO, font=FUTURA_15_FONT,
                                       text="catégorie", anchor="w")
        self.category_label.place(relx=0, rely=0, relwidth=0.3, relheight=1)
        self.category_combobox = ttk.Combobox(self.category_film_frame, values=list(self.workbook.category_dict.keys()),
                                              font=FUTURA_15_FONT, justify='center')
        self.category_combobox['state'] = 'readonly'
        self.category_combobox.place(relx=0.3, rely=0, relwidth=0.7, relheight=1)
        self.category_rating_frame = tk.Frame(self.search_frame, background='#7A918D')
        self.category_rating_frame.place(relx=0, rely=0.6, relwidth=1, relheight=0.05)
        self.rating_label = tk.Label(self.category_rating_frame, bg=RAISIN_BLACK, fg=GAINSBORO, font=FUTURA_15_FONT,
                                     text="note", anchor="w")
        self.rating_label.place(relx=0, rely=0, relwidth=0.3, relheight=1)
        self.rating_combobox = ttk.Combobox(self.category_rating_frame, values=list(range(0, 11)), font=FUTURA_15_FONT,
                                            justify='center')
        self.rating_combobox['state'] = 'readonly'
        self.rating_combobox.place(relx=0.3, rely=0, relwidth=0.7, relheight=1)
        self.search_button = tk.Button(self.search_frame, text="chercher", command=self.ctr_update_tree,
                                       bd=2, activeforeground=RAISIN_BLACK, activebackground=GAINSBORO,
                                       bg=RAISIN_BLACK, fg=GAINSBORO, font=HELV_20_BUTTON_FONT)
        self.search_button.place(relx=0, rely=0.75, relwidth=1, relheight=0.1)
        self.clear_button = tk.Button(self.search_frame, text="vider champs", command=self.clear_inputs,
                                      bd=2, activeforeground=RAISIN_BLACK, activebackground=GAINSBORO,
                                      bg=RAISIN_BLACK, fg=GAINSBORO, font=HELV_20_BUTTON_FONT)
        self.clear_button.place(relx=0, rely=0.9, relwidth=1, relheight=0.1)
        self.options_button_frame = tk.Frame(self.main_frame, background=RAISIN_BLACK)
        self.options_button_frame.place(relx=0, rely=0.85, relwidth=1, relheight=0.1)
        self.add_button = tk.Button(self.options_button_frame, text="ajouter film", command=self.add_film,
                                    bd=2, activeforeground=RAISIN_BLACK, activebackground=MAIZE,
                                    bg=GAINSBORO, fg=RAISIN_BLACK, font=HELV_30_BUTTON_FONT)
        self.add_button.place(relx=0, rely=0, relwidth=0.35, relheight=1)
        self.edit_button = tk.Button(self.options_button_frame, text="modifier film",
                                     bd=2, activeforeground=RAISIN_BLACK, activebackground=GAINSBORO,
                                     bg=RAISIN_BLACK, fg=GAINSBORO, font=HELV_20_BUTTON_FONT,
                                     command=self.edit_film)
        self.edit_button.place(relx=0.4, rely=0, relwidth=0.15, relheight=1)
        self.delete_button = tk.Button(self.options_button_frame, text="supprimer film",
                                       bd=2, activeforeground=RAISIN_BLACK, activebackground=GAINSBORO,
                                       bg=RAISIN_BLACK, fg=GAINSBORO, font=HELV_20_BUTTON_FONT,
                                       command=self.ctr_delete_film)
        self.delete_button.place(relx=0.60, rely=0, relwidth=0.15, relheight=1)
        self.save_button = tk.Button(self.options_button_frame, text="exporter liste",
                                     bd=2, activeforeground=RAISIN_BLACK, activebackground=GAINSBORO,
                                     bg=RAISIN_BLACK, fg=GAINSBORO, font=HELV_20_BUTTON_FONT,
                                     command=self.crt_save_search)
        self.save_button.place(relx=0.80, rely=0, relwidth=0.2, relheight=1)
        self.cancel_button = tk.Button(self.workbook_frame, text="retour",
                                       bd=2, activeforeground=RAISIN_BLACK, activebackground=MAIZE,
                                       bg=RAISIN_BLACK, fg=MAIZE, font=HELV_20_BUTTON_FONT,
                                       command=self.exit_window)
        self.cancel_button.place(relx=0.74, rely=0.90, relwidth=0.16, relheight=0.05)
        set_active(self.workbook_frame)

    def ctr_update_tree(self):  # controleur pour l'interface d'affichage
        self.result_dict = dict()
        for element in self.result_tree.get_children():
            self.result_tree.delete(element)
        self.update_parameter()
        if self.parameter_dict:
            self.result_dict = self.workbook.find_films(**self.parameter_dict)
            if not self.result_dict:
                AlertPopUP(text='Rien trouvé')
        else:
            self.result_dict = self.workbook.find_films(all=True)
        for k, v in self.result_dict.items():
            self.result_tree.insert('', "end", text=k, values=[v.get('year'), v.get('category'),
                                                               v.get('director'),
                                                               list(filter(lambda actor: actor, v.get('actors'))),
                                                               v.get('rating'), v.get('comment')])

    def exit_window(self):
        self.workbook_frame.destroy()

    def crt_save_search(self):  # controleur sauvegarde de film
        path = filedialog.asksaveasfilename(filetypes=[('Fichier CSV', '*.csv')]) + '.csv'
        if path:
            Workbook.save_search(path, self.result_dict)
        set_active(self.workbook_frame)

    def ctr_delete_film(self):  # controleur effacement de film
        def del_command():
            self.result_tree.delete(selected)

        try:
            selected = self.result_tree.focus()
            name = self.result_tree.item(selected).get('text')
            category = self.result_tree.item(selected).get('values')[1]
            self.workbook.remove_film(name, category)
            AlertPopUP(text='Voulez-vous bien suprimer:\n' + name,
                       btn1_text='oui',
                       btn1_command=del_command)
            self.result_tree.delete(selected)
        except IndexError:
            AlertPopUP(text='Veuillez sélectionner\nun film')

    def add_film(self):  # ouvre une instance de InputFilmGUI add=True
        InputFilmGUI(self.workbook, self, add=True)

    def edit_film(self):  # ouvre une instance de InputFilmGUI edit=True
        if not self.result_tree.focus():
            AlertPopUP(text='Veuillez sélectionner\nun film')
        else:
            InputFilmGUI(self.workbook, self, edit=True)

    def clear_inputs(self):  # vide les champs de recherche
        self.parameter_dict = dict()
        self.tittle_entry.delete(0, 'end')
        self.year_entry.delete(0, 'end')
        self.director_entry.delete(0, 'end')
        self.actor1_entry.delete(0, 'end')
        self.actor2_entry.delete(0, 'end')
        self.actor3_entry.delete(0, 'end')
        self.category_combobox.set('')
        self.rating_combobox.set('')
        self.ctr_update_tree()

    def update_parameter(self):  # mets les parametre de recherche a jours a l'interne
        if self.tittle_entry.get() or self.year_entry.get() or self.director_entry.get() \
                or self.actor1_entry.get() or self.actor2_entry.get() or self.actor3_entry.get() \
                or self.category_combobox.get() or self.rating_combobox.get():
            self.parameter_dict.update(name=self.tittle_entry.get())
            self.parameter_dict.update(year=self.year_entry.get())
            self.parameter_dict.update(name=self.director_entry.get())
            self.parameter_dict.update(actors=[entry.get() for entry in
                                               [self.actor1_entry,
                                                self.actor2_entry,
                                                self.actor3_entry] if entry.get()])
            self.parameter_dict.update(category=self.category_combobox.get())
            self.parameter_dict.update(rating=self.rating_combobox.get())
        else:
            self.parameter_dict = dict()


class InputFilmGUI:   # ouvre une instance de la fenetre d'entré d'information de film, soit en mode edit ou add
    def __init__(self, workbook, workbookGUI, **kwargs):
        """
        :param kwargs:
            add=True
            edit=True
        """
        self.workbook = workbook
        self.workbookGUI = workbookGUI
        self.film_frame = tk.Tk()
        if kwargs.get('add'):
            self.film_frame.title("Ajout d'un film")
        elif kwargs.get('edit'):
            self.film_frame.title("Modification d'un film")
        ws = self.film_frame.winfo_screenwidth()  # width of the screen
        hs = self.film_frame.winfo_screenheight()  # height of the screen
        h = ws / 2
        w = ws / 2
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        self.film_frame.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.film_frame.configure(background=JET)
        main_film_frame = tk.Frame(self.film_frame, background=JET)
        main_film_frame.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.7)
        self.title_film_frame = tk.Frame(main_film_frame, background=GAINSBORO)
        self.title_film_frame.place(relx=0, rely=0, relwidth=1, relheight=0.05)
        self.title_label = tk.Label(self.title_film_frame, bg=JET, fg=GAINSBORO, font=FUTURA_20_FONT,
                                    text="titre", anchor="w")
        self.title_label.place(relx=0, rely=0, relwidth=0.3, relheight=1)
        self.title_entry = tk.Entry(self.title_film_frame, bg=GAINSBORO, fg=JET, font=FUTURA_20_FONT, justify='center')
        self.title_entry.place(relx=0.3, rely=0, relwidth=0.7, relheight=1)
        # frame pour la saisie de la date de création
        self.year_film_frame = tk.Frame(main_film_frame, background=JET)
        self.year_film_frame.place(relx=0, rely=0.075, relwidth=1, relheight=0.05)
        self.year_label = tk.Label(self.year_film_frame, bg=JET, fg=GAINSBORO, font=FUTURA_20_FONT,
                                   text="année", anchor="w")
        self.year_label.place(relx=0, rely=0, relwidth=0.3, relheight=1)
        self.year_entry = tk.Entry(self.year_film_frame, bg=GAINSBORO, fg=JET, font=FUTURA_20_FONT, justify='center')
        self.year_entry.place(relx=0.3, rely=0, relwidth=0.7, relheight=1)
        # frame pour le réalisateur
        self.director_film_frame = tk.Frame(main_film_frame, background=JET)
        self.director_film_frame.place(relx=0, rely=0.15, relwidth=1, relheight=0.05)
        self.director_label = tk.Label(self.director_film_frame, bg=JET, fg=GAINSBORO, font=FUTURA_20_FONT,
                                       text="réalisateur", anchor="w")
        self.director_label.place(relx=0, rely=0, relwidth=0.3, relheight=1)
        self.director_entry = tk.Entry(self.director_film_frame, bg=GAINSBORO, fg=JET, font=FUTURA_20_FONT,
                                       justify='center')
        self.director_entry.place(relx=0.3, rely=0, relwidth=0.7, relheight=1)
        # frame pour la saisie de trois noms d'acteurs
        self.actors_film_frame = tk.Frame(main_film_frame, background=GAINSBORO)
        self.actors_film_frame.place(relx=0, rely=0.225, relwidth=1, relheight=0.15)
        self.actors_label = tk.Label(self.actors_film_frame, bg=JET, fg=GAINSBORO, font=FUTURA_20_FONT,
                                     text="acteurs", anchor="w")
        self.actors_label.place(relx=0, rely=0, relwidth=0.3, relheight=1)
        self.actor1_entry = tk.Entry(self.actors_film_frame, bg=GAINSBORO, fg=JET, font=FUTURA_20_FONT,
                                     justify='center')
        self.actor1_entry.place(relx=0.3, rely=0, relwidth=0.7, relheight=0.33)
        self.actor2_entry = tk.Entry(self.actors_film_frame, bg=GAINSBORO, fg=JET, font=FUTURA_20_FONT,
                                     justify='center')
        self.actor2_entry.place(relx=0.3, rely=0.33, relwidth=0.7, relheight=0.33)
        self.actor3_entry = tk.Entry(self.actors_film_frame, bg=GAINSBORO, fg=JET, font=FUTURA_20_FONT,
                                     justify='center')
        self.actor3_entry.place(relx=0.3, rely=0.66, relwidth=0.7, relheight=0.33)
        # frame pour la catégorie
        self.category_film_frame = tk.Frame(main_film_frame, background=IVORY)
        self.category_film_frame.place(relx=0, rely=0.4, relwidth=1, relheight=0.05)
        style = ttk.Style(self.film_frame)
        style.map('TCombobox', fieldbackground=[('readonly', IVORY)])
        style.map('TCombobox', fieldforeground=[('readonly', JET)])
        style.map('TCombobox', background=[('readonly', GAINSBORO)])
        style.map('TCombobox', foreground=[('readonly', JET)])
        style.map('TCombobox', selectbackground=[('readonly', GAINSBORO)])
        style.map('TCombobox', selectforeground=[('readonly', JET)])
        self.category_label = tk.Label(self.category_film_frame, bg=JET, fg=GAINSBORO, font=FUTURA_20_FONT,
                                       text="catégorie", anchor="w")
        self.category_label.place(relx=0, rely=0, relwidth=0.3, relheight=1)
        self.category_combobox = ttk.Combobox(self.category_film_frame, values=list(self.workbook.category_dict.keys()),
                                              font=FUTURA_20_FONT, justify='center')
        self.category_combobox['state'] = 'readonly'
        self.category_combobox.place(relx=0.3, rely=0, relwidth=0.7, relheight=1)
        self.category_rating_frame = tk.Frame(main_film_frame, background=JET)
        self.category_rating_frame.place(relx=0, rely=0.475, relwidth=1, relheight=0.05)
        self.rating_label = tk.Label(self.category_rating_frame, bg=JET, fg=GAINSBORO, font=FUTURA_20_FONT,
                                     text="note", anchor="w")
        self.rating_label.place(relx=0, rely=0, relwidth=0.3, relheight=1)
        self.rating_combobox = ttk.Combobox(self.category_rating_frame, values=list(range(0, 11)), font=FUTURA_20_FONT,
                                            justify='center')
        self.rating_combobox['state'] = 'readonly'
        self.rating_combobox.place(relx=0.3, rely=0, relwidth=0.7, relheight=1)
        self.category_comment_frame = tk.Frame(main_film_frame, background=GAINSBORO)
        self.category_comment_frame.place(relx=0, rely=0.55, relwidth=1, relheight=0.3)
        self.comment_label = tk.Label(self.category_comment_frame, bg=JET, fg=GAINSBORO, font=FUTURA_20_FONT,
                                      text="commentaire", anchor="w")
        self.comment_label.place(relx=0, rely=0, relwidth=1, relheight=0.25)
        self.comment_text = tk.Text(self.category_comment_frame, bd=0,
                                    bg=GAINSBORO, fg=JET, font=FUTURA_20_FONT)
        self.comment_text.place(relx=0, rely=0.25, relwidth=1, relheight=0.75)
        if kwargs.get('edit'):
            self.edit_button = tk.Button(main_film_frame, text="modifier",
                                         bd=2, activeforeground=GAINSBORO, activebackground=JET,
                                         bg=GAINSBORO, fg=JET, font=HELV_20_BUTTON_FONT,
                                         command=self.edit_film_confirmation)
            self.edit_button.place(relx=0, rely=0.9, relheight=0.1, relwidth=1)
            selected = workbookGUI.result_tree.focus()
            self.name = workbookGUI.result_tree.item(selected).get('text')
            self.category = workbookGUI.result_tree.item(selected).get('values')[1]
            self.title_entry.insert(0, self.name)
            self.year_entry.insert(0,
                                   str(workbook.category_dict.get(self.category).film_dict.get(self.name).get('year')))
            self.director_entry.insert(0, workbook.category_dict.get(self.category).film_dict.get(self.name).get(
                'director'))
            try:
                self.actor1_entry.insert(0, workbook.category_dict.get(self.category).film_dict.get(self.name).get(
                    'actors')[0])
            except IndexError:
                self.actor1_entry.insert(0, '')
            try:
                self.actor2_entry.insert(0, workbook.category_dict.get(self.category).film_dict.get(self.name).get(
                    'actors')[1])
            except IndexError:
                self.actor2_entry.insert(0, '')
            try:
                self.actor3_entry.insert(0, workbook.category_dict.get(self.category).film_dict.get(self.name).get(
                    'actors')[2])
            except IndexError:
                self.actor3_entry.insert(0, '')
            self.category_combobox.set(self.category)
            self.rating_combobox.set(workbook.category_dict.get(self.category).film_dict.get(self.name).get('rating'))
            self.comment_text.insert(tk.INSERT,
                                     workbook.category_dict.get(self.category).film_dict.get(self.name).get('comment'))
        elif kwargs.get('add'):
            self.add_button = tk.Button(main_film_frame, text="ajouter",
                                        bd=2, activeforeground=GAINSBORO, activebackground=JET,
                                        bg=GAINSBORO, fg=JET, font=HELV_20_BUTTON_FONT,
                                        command=self.add_film_confirmation)
            self.add_button.place(relx=0, rely=0.9, relheight=0.1, relwidth=0.6)
        self.cancel_button = tk.Button(main_film_frame, text="annuler",
                                       bd=0, activeforeground=JET, activebackground=MAIZE,
                                       bg=JET, fg=MAIZE, font=HELV_20_BUTTON_FONT,
                                       command=self.exit_window)
        self.cancel_button.place(relx=0.7, rely=0.9, relheight=0.1, relwidth=0.3)
        set_active(self.film_frame)

    def add_film_confirmation(self):  # fonction de validation de input
        if not self.title_entry.get():
            AlertPopUP(text='Veuillez entrer\nun nom')
        elif not self.year_entry.get():
            AlertPopUP(text='Veuillez entrer\nune année')
        elif not self.year_entry.get().isdigit():
            AlertPopUP(text='Veuillez entrer\nune année valide')
        elif not self.category_combobox.get():
            AlertPopUP(text='Veuillez choisir\nune catégorie')
        else:
            AlertPopUP(text='Voulez-vous bien ajouter:\n' + self.title_entry.get(),
                       btn1_text='oui',
                       btn1_command=self.crt_add_film)

    def crt_add_film(self):  # controleur pour l'ajout de film
        self.workbook.add_film(self.category_combobox.get(),
                                   self.title_entry.get(),
                                   self.year_entry.get(),
                                   director=self.director_entry.get(),
                                   actors=[self.actor1_entry.get(), self.actor2_entry.get(), self.actor3_entry.get()],
                                   rating=self.rating_combobox.get(),
                                   comment=self.comment_text.get('1.0', tk.END))
        self.workbookGUI.ctr_update_tree()
        self.exit_window()

    def edit_film_confirmation(self):  # fonction de validation de input
        if not self.title_entry.get():
            AlertPopUP(text='Veuillez entrer\nun nom')
        elif not self.year_entry.get():
            AlertPopUP(text='Veuillez entrer\nune année')
        elif not self.category_combobox.get():
            AlertPopUP(text='Veuillez choisir\nune catégorie')
        else:
            AlertPopUP(text='Voulez-vous bien modifier:\n' + self.name,
                       btn1_text='oui',
                       btn1_command=self.crt_edit_film)

    def crt_edit_film(self): # controleur pour la modification de film
        kwargs = dict(year=self.year_entry.get(),
                      director=self.director_entry.get(),
                      actors=[self.actor1_entry.get(), self.actor2_entry.get(), self.actor3_entry.get()],
                      rating=self.rating_combobox.get(),
                      comment=self.comment_text.get('1.0', tk.END))
        if self.name != self.title_entry.get():
            kwargs.update(name=self.title_entry.get())
        if self.category != self.category_combobox.get():
            kwargs.update(category=self.category_combobox.get())
        self.workbook.edit_film(self.category, self.name, **kwargs)
        self.workbookGUI.ctr_update_tree()
        self.exit_window()

    def exit_window(self):
        self.film_frame.destroy()


class GestionCategGUI:  # instance d'une fenetre du gestionaire de catégorie
    def __init__(self, workbook):
        self.workbook = workbook
        self.manage_window = tk.Tk()
        self.manage_window.title("gérer les catégories")
        # self.manage_window.overrideredirect(1)
        ws = self.manage_window.winfo_screenwidth()  # width of the screen
        hs = self.manage_window.winfo_screenheight()  # height of the screen
        w = ws / 2  # width for the Tk root
        h = ws / 2  # height for the Tk root
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        self.manage_window.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.manage_window.configure(background=RAISIN_BLACK)
        manage_main_frame = tk.Frame(self.manage_window, bg=RAISIN_BLACK)
        manage_main_frame.place(relx=0.2, rely=0.2, relwidth=0.6, relheight=0.6)
        style = ttk.Style(manage_main_frame)
        style.map('TCombobox', fieldbackground=[('readonly', RAISIN_BLACK)])
        style.map('TCombobox', fieldforeground=[('readonly', GAINSBORO)])
        style.map('TCombobox', background=[('readonly', GAINSBORO)])
        style.map('TCombobox', foreground=[('readonly', GAINSBORO)])
        style.map('TCombobox', selectbackground=[('readonly', RAISIN_BLACK)])
        style.map('TCombobox', selectforeground=[('readonly', GAINSBORO)])
        self.category_label = tk.Label(manage_main_frame, bg=RAISIN_BLACK, fg=GAINSBORO, font=FUTURA_30_FONT,
                                       text="catégorie.s", anchor="w")
        self.category_label.place(relx=0, rely=0, relwidth=1, relheight=0.1)
        self.category_combobox = ttk.Combobox(manage_main_frame, values=list(self.workbook.category_dict.keys()),
                                              font=FUTURA_30_FONT, justify='center')
        self.category_combobox.current(0)
        self.category_combobox['state'] = 'readonly'
        self.category_combobox.place(relx=0, rely=0.125, relwidth=1, relheight=0.15)
        self.category_combobox.set('')
        btn_add_category = tk.Button(manage_main_frame, text="ajouter une catégorie",
                                     command=self.add_category,
                                     bd=2, activeforeground=RAISIN_BLACK, activebackground=GAINSBORO, bg=RAISIN_BLACK,
                                     fg=GAINSBORO, font=HELV_30_BUTTON_FONT)
        btn_add_category.place(relx=0, rely=0.4, relwidth=1, relheight=0.167)

        btn_modify_category = tk.Button(manage_main_frame, text="modifier une catégorie",
                                        command=self.edit_category,
                                        bd=2, activeforeground=RAISIN_BLACK, activebackground=GAINSBORO,
                                        bg=RAISIN_BLACK,
                                        fg=GAINSBORO, font=HELV_30_BUTTON_FONT)
        btn_modify_category.place(relx=0, rely=0.617, relwidth=1, relheight=0.167)

        btn_remove_category = tk.Button(manage_main_frame, text="supprimer une catégorie",
                                        command=self.delete_category_confirmation,
                                        bd=2, activeforeground=RAISIN_BLACK, activebackground=GAINSBORO,
                                        bg=RAISIN_BLACK,
                                        fg=GAINSBORO, font=HELV_30_BUTTON_FONT)
        btn_remove_category.place(relx=0, rely=0.833, relwidth=1, relheight=0.167)
        btn_exit = tk.Button(self.manage_window, text="retour", command=self.exit_window,
                             bd=0, activeforeground=RAISIN_BLACK, activebackground=MAIZE, bg=RAISIN_BLACK,
                             fg=MAIZE, font=HELV_20_BUTTON_FONT)
        btn_exit.place(relx=0.55, rely=0.85, relwidth=0.25, relheight=0.075)
        set_active(self.manage_window)

    def edit_category(self):  # ouvre une instance de ModifyAddCategory de type edit
        if not self.category_combobox.get():
            AlertPopUP(text='Veuillez sélectionner\nune catéorie')
        else:
            InputCategoryGUI(self.workbook, self, edit=True, name=self.category_combobox.get())

    def add_category(self): # ouvre une instance de InputCategoryGUI de type add
        InputCategoryGUI(self.workbook, self, add=True)
        self.category_combobox['values'] = list(self.workbook.category_dict.keys())

    def delete_category_confirmation(self):  # fonction de validation de input
        if not self.category_combobox.get():
            AlertPopUP(text='Veuillez sélectionner\nune catéorie')
        else:
            AlertPopUP(text='Voulez-vous bien supprimer:\n' + self.category_combobox.get(),
                       btn1_text='oui',
                       btn1_command=self.crt_delete_category)

    def crt_delete_category(self):  # controleur effacer des catégorie
        self.workbook.remove_category(self.category_combobox.get())
        self.category_combobox['values'] = list(self.workbook.category_dict.keys())
        self.category_combobox.set('')

    def exit_window(self):
        self.manage_window.destroy()


class InputCategoryGUI:  # fenetre de input pour les catégorie soit en mode add ou edit
    """
            :param kwargs:
                add=True
                edit=True
                name=str
            """
    def __init__(self, workbook, gui, **kwargs):
        self.gui = gui
        self.workbook = workbook
        self.window = tk.Tk()
        ws = self.window.winfo_screenwidth()
        hs = self.window.winfo_screenheight()
        h = ws / 2
        w = ws / 2
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        self.window.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.window.configure(background=RAISIN_BLACK)
        edit_add_frame = tk.Frame(self.window, bg=RAISIN_BLACK)
        edit_add_frame.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.7)
        if kwargs.get('add'):
            title = "ajouter une catégorie"
            label_text = "nouvelle catégorie"
            button_text = "ajouter"
            cmd = self.add_category_confirmation
            label_x = 0
            label_y = 0
            label_height = 0.1
            entry_x = 0
            entry_y = 0.12
            button_x = 0
            button_y = 0.45
        elif kwargs.get('edit'):
            self.name = kwargs.get('name')
            title = "mofifier une catégorie"
            label_text = "nouveau nom de " + self.name
            button_text = "modifier"
            cmd = self.edit_category_confirmation
            label_x = 0
            label_y = 0
            label_height = 0.1
            entry_x = 0
            entry_y = 0.12
            button_x = 0
            button_y = 0.45
        self.window.title(title)
        self.label_title = tk.Label(edit_add_frame, bg=RAISIN_BLACK, fg=GAINSBORO, font=FUTURA_30_FONT,
                                    text=label_text, anchor="w")
        self.label_title.place(relx=label_x, rely=label_y, relwidth=1, relheight=label_height)
        self.title_entry = tk.Entry(edit_add_frame, bg=RAISIN_BLACK, fg=GAINSBORO, font=FUTURA_30_FONT,
                                    justify='center')
        self.title_entry.place(relx=entry_x, rely=entry_y, relwidth=1, relheight=0.2)
        self.action_button = tk.Button(edit_add_frame, text=button_text,
                                       bd=2, activeforeground=RAISIN_BLACK, activebackground=GAINSBORO,
                                       bg=RAISIN_BLACK,
                                       fg=GAINSBORO, font=HELV_30_BUTTON_FONT,
                                       command=cmd)
        self.action_button.place(relx=button_x, rely=button_y, relwidth=1, relheight=0.25)

        self.action_button = tk.Button(edit_add_frame, text="retour", command=self.exit_window,
                                       bd=2, activeforeground=RAISIN_BLACK, activebackground=MAIZE,
                                       bg=RAISIN_BLACK,
                                       fg=MAIZE, font=HELV_30_BUTTON_FONT)
        self.action_button.place(relx=0, rely=0.75, relwidth=1, relheight=0.25)
        set_active(self.window)

    def edit_category_confirmation(self):  # fonction de validation de input
        AlertPopUP(text='Voulez-vous bien modifier:\n' + self.name,
                   btn1_text='oui',
                   btn1_command=self.ctr_edit_category)

    def ctr_edit_category(self):  # controleur pour la modification
        self.workbook.edit_category(self.gui.category_combobox.get(), self.title_entry.get())
        self.gui.category_combobox['values'] = list(self.workbook.category_dict.keys())
        self.gui.category_combobox.set('')
        self.exit_window()

    def add_category_confirmation(self):  # fonction de validation de input
        if not self.title_entry.get():
            AlertPopUP(text='Veuillez entrer\nun nom')
        else:
            AlertPopUP(text='Voulez-vous bien ajouter:\n' + self.title_entry.get(),
                       btn1_text='oui',
                       btn1_command=self.crt_add_category)

    def crt_add_category(self): # controleur pour l'ajout
        self.workbook.add_category(self.title_entry.get())
        self.gui.category_combobox['values'] = list(self.workbook.category_dict.keys())
        self.gui.category_combobox.set('')
        self.exit_window()

    def exit_window(self):
        self.window.destroy()


def set_active(window):  # Fonction statique de fermeture de fenetre
    window.lift()
    window.focus_force()
    window.grab_set()
    window.grab_release()
