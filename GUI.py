import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog

from asn1crypto._ffi import null

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
    def __init__(self, workbook):
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

        self.btn_category = tk.Button(main_menu_frame, text="catégories", command=self.manage_category_frame,
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

    def exit_ap(self):  # TODO implement saving
        exit()

    def open_workbook(self):
        WorkbookGUI(self.workbook)

    def manage_category_frame(self):
        GestionCategGUI(self.workbook)

    def debug_ph(self):
        AlertPopUP('test', 'test message',
                   btn1=dict(text='test', command=print('test')),
                   btn2=dict(text='test', command=print('test')))


class AlertPopUP:
    def __init__(self, text, **kwargs):
        """
        :param kwargs:  btn1=dict(text=String, command=function)
                        btn2=dict(text=String, command=function)
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

        if 'btn1' in kwargs:
            btn1_text = kwargs['btn1']['text']
            btn1_y = 0.74
            btn1_heigth = 0.27
        else:
            btn1_text = "ok"
            btn1_y = 0.55
            btn1_heigth = 0.45
        self.B1 = tk.Button(self.popup_frame, text=btn1_text, command=self.popup.destroy,
                            activeforeground=RAISIN_BLACK, activebackground=MAIZE,
                            bg=RAISIN_BLACK, fg=MAIZE, font=HELV_20_BUTTON_FONT)
        self.B1.place(relx=0, rely=btn1_y, relwidth=1, relheight=btn1_heigth)
        if 'btn2' in kwargs:
            self.B2 = tk.Button(self.popup_frame, text=kwargs['btn2']['text'], command=kwargs['btn2']['command'],
                                activeforeground=RAISIN_BLACK, activebackground=MAIZE,
                                bg=RAISIN_BLACK, fg=MAIZE, font=HELV_20_BUTTON_FONT)
            self.B2.place(relx=0, rely=0.37, relwidth=1, relheight=0.27)
            label_height = 0.27
        else:
            label_height = 0.45

        self.label = tk.Label(self.popup_frame, text=text, bg=MAIZE, fg=RAISIN_BLACK, anchor=tk.CENTER,
                              font=FUTURA_20_FONT)
        self.label.place(relx=0, rely=0, relwidth=1, relheight=label_height)

        print('\a')
        self.popup.mainloop()
        self.set_active()


class WorkbookGUI:

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
        style.layout("Custom.Treeview.Heading", [
            ("Custom.Treeheading.cell", {'sticky': 'nswe'}),
            ("Custom.Treeheading.border", {'sticky': 'nswe', 'children': [
                ("Custom.Treeheading.padding", {'sticky': 'nswe', 'children': [
                    ("Custom.Treeheading.image", {'side': 'right', 'sticky': ''}),
                    ("Custom.Treeheading.text", {'side': 'left', 'sticky': 'we'})
                ]})
            ]}),
        ])
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
        self.search_button = tk.Button(self.search_frame, text="chercher", command=self.update_tree,
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
                                       command=self.delete_film)
        self.delete_button.place(relx=0.60, rely=0, relwidth=0.15, relheight=1)
        self.save_button = tk.Button(self.options_button_frame, text="exporter liste",
                                     bd=2, activeforeground=RAISIN_BLACK, activebackground=GAINSBORO,
                                     bg=RAISIN_BLACK, fg=GAINSBORO, font=HELV_20_BUTTON_FONT,
                                     command=self.save_search)
        self.save_button.place(relx=0.80, rely=0, relwidth=0.2, relheight=1)

        self.cancel_button = tk.Button(self.workbook_frame, text="retour",
                                       bd=2, activeforeground=RAISIN_BLACK, activebackground=MAIZE,
                                       bg=RAISIN_BLACK, fg=MAIZE, font=HELV_20_BUTTON_FONT,
                                       command=self.exit_window)
        self.cancel_button.place(relx=0.74, rely=0.90, relwidth=0.16, relheight=0.05)

        self.set_active()

    def update_tree(self):
        self.result_dict = dict()
        for element in self.result_tree.get_children():
            self.result_tree.delete(element)
        self.update_parameter()
        if self.parameter_dict:
            self.result_dict = self.workbook.find_films(**self.parameter_dict)  # TODO Pop-up if no result
        else:
            self.result_dict = self.workbook.find_films(all=True)
        for k, v in self.result_dict.items():
            self.result_tree.insert('', "end", text=k, values=[v.get('year'), v.get('category'),
                                                               v.get('director'),
                                                               list(filter(lambda actor: actor, v.get('actors'))),
                                                               v.get('rating'), v.get('comment')])

    def set_active(self):  # TODO bind update to enter?
        self.workbook_frame.lift()
        self.workbook_frame.focus_force()
        self.workbook_frame.grab_set()
        self.workbook_frame.grab_release()

    def exit_window(self):
        self.workbook_frame.destroy()


    def save_search(self):  # TODO implement confirmation pop-up
        path = filedialog.asksaveasfile(initialdir="/", filetypes=[("Fichier CSV", "*.csv")])
        if path:
            Workbook.save_search(path.name + '.csv', self.results_dict)
            self.exit_window()

    def delete_film(self):  # TODO implement confirmation pop-up
        try:
            selected = self.result_tree.focus()
            name = self.result_tree.item(selected).get('text')
            category = self.result_tree.item(selected).get('values')[1]
            self.workbook.remove_film(name, category)
            self.result_tree.delete(selected)
        except IndexError:  # TODO implement please select pop up
            AlertPopUP(text='Veuillez sélectionner\nun film')

    def add_film(self):
        InputFilmGUI(self.workbook, self, add=True)

    def edit_film(self):
        try:
            self.result_tree.focus()
            InputFilmGUI(self.workbook, self, edit=True)
        except IndexError:  # TODO implement please select pop up
            pass

    def clear_inputs(self):  # TODO implement method
        self.parameter_dict = dict()
        self.tittle_entry.delete(0, 'end')
        self.year_entry.delete(0, 'end')
        self.director_entry.delete(0, 'end')
        self.actor1_entry.delete(0, 'end')
        self.actor2_entry.delete(0, 'end')
        self.actor3_entry.delete(0, 'end')
        self.category_combobox.set('')
        self.rating_combobox.set('')
        self.update_tree()

    def update_parameter(self):
        if self.tittle_entry.get():
            self.parameter_dict.update(name=self.tittle_entry.get())
        if self.year_entry.get():
            self.parameter_dict.update(year=self.year_entry.get())
        if self.director_entry.get():
            self.parameter_dict.update(name=self.director_entry.get())
        if self.actor1_entry.get() or self.actor2_entry.get() or self.actor3_entry.get():
            self.parameter_dict.update(actors=[entry.get() for entry in
                                               [self.actor1_entry,
                                                self.actor2_entry,
                                                self.actor3_entry] if entry.get()])
        if self.category_combobox.get():
            self.parameter_dict.update(category=self.category_combobox.get())
        if self.rating_combobox.get():
            self.parameter_dict.update(rating=self.rating_combobox.get())


class InputFilmGUI: # TODO implement confirmation pop-up
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
        self.tittle_label = tk.Label(self.title_film_frame, bg=JET, fg=GAINSBORO, font=FUTURA_20_FONT,
                                     text="titre", anchor="w")
        self.tittle_label.place(relx=0, rely=0, relwidth=0.3, relheight=1)
        self.tittle_entry = tk.Entry(self.title_film_frame, bg=GAINSBORO, fg=JET, font=FUTURA_20_FONT, justify='center')
        self.tittle_entry.place(relx=0.3, rely=0, relwidth=0.7, relheight=1)
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
        self.commentary_text = tk.Text(self.category_comment_frame, bd=0,
                                    bg=GAINSBORO, fg=JET, font=FUTURA_20_FONT)
        self.comment_text.place(relx=0, rely=0.25, relwidth=1, relheight=0.75)
        if kwargs.get('edit'):
            self.edit_button = tk.Button(main_film_frame, text="modifier",
                                         bd=2, activeforeground=GAINSBORO, activebackground=JET,
                                         bg=GAINSBORO, fg=JET, font=HELV_20_BUTTON_FONT,
                                         command=self.edit_film_ctr)
            self.edit_button.place(relx=0, rely=0.9, relheight=0.1, relwidth=1)
            selected = workbookGUI.result_tree.focus()
            self.name = workbookGUI.result_tree.item(selected).get('text')
            self.category = workbookGUI.result_tree.item(selected).get('values')[1]
            self.tittle_entry.insert(0, self.name)
            self.year_entry.insert(0,  str(workbook.category_dict.get(self.category).film_dict.get(self.name).get('year')))
            self.director_entry.insert(0, workbook.category_dict.get(self.category).film_dict.get(self.name).get('director'))
            try:
                self.actor1_entry.insert(0, workbook.category_dict.get(self.category).film_dict.get(self.name).get('actors')[0])
            except IndexError:
                self.actor1_entry.insert(0, '')
            try:
                self.actor2_entry.insert(0, workbook.category_dict.get(self.category).film_dict.get(self.name).get('actors')[1])
            except IndexError:
                self.actor2_entry.insert(0, '')
            try:
                self.actor3_entry.insert(0, workbook.category_dict.get(self.category).film_dict.get(self.name).get('actors')[2])
            except IndexError:
                self.actor3_entry.insert(0, '')
            self.category_combobox.set(self.category)
            self.rating_combobox.set(workbook.category_dict.get(self.category).film_dict.get(self.name).get('rating'))
            self.comment_text.insert(tk.INSERT, workbook.category_dict.get(self.category).film_dict.get(self.name).get('comment'))
        elif kwargs.get('add'):
            self.add_button = tk.Button(main_film_frame, text="ajouter",
                                        bd=2, activeforeground=GAINSBORO, activebackground=JET,
                                        bg=GAINSBORO, fg=JET, font=HELV_20_BUTTON_FONT,
                                        command=self.add_film_ctr)
            self.add_button.place(relx=0, rely=0.9, relheight=0.1, relwidth=0.6)
        self.cancel_button = tk.Button(main_film_frame, text="annuler",
                                       bd=0, activeforeground=JET, activebackground=MAIZE,
                                       bg=JET, fg=MAIZE, font=HELV_20_BUTTON_FONT,
                                       command=self.exit_window)
        self.cancel_button.place(relx=0.7, rely=0.9, relheight=0.1, relwidth=0.3)
        self.set_active()

    def add_film_ctr(self):
        self.workbook.add_film(self.category_combobox.get(),  # TODO implement pop up if missing name or year
                               self.tittle_entry.get(),
                               self.year_entry.get(),
                               director=self.director_entry.get(),
                               actors=[self.actor1_entry.get(), self.actor2_entry.get(), self.actor3_entry.get()],
                               rating=self.rating_combobox.get(),
                               comment=self.comment_text.get('1.0', tk.END))
        self.workbookGUI.update_tree()
        self.exit_window()

    def edit_film_ctr(self):
        kwargs = dict(year=self.year_entry.get(),
                                director=self.director_entry.get(),
                                actors=[self.actor1_entry.get(), self.actor2_entry.get(), self.actor3_entry.get()],
                                rating=self.rating_combobox.get(),
                                comment=self.comment_text.get('1.0', tk.END))
        if self.name != self.tittle_entry.get():
            kwargs.update(name=self.tittle_entry.get())
        if self.category != self.category_combobox.get():
            kwargs.update(category=self.category_combobox.get())
        self.workbook.edit_film(self.category, self.name, **kwargs)
        self.workbookGUI.update_tree()
        self.exit_window()

    def exit_window(self):
        self.film_frame.destroy()

    def set_active(self):
        self.film_frame.lift()
        self.film_frame.focus_force()
        self.film_frame.grab_set()
        self.film_frame.grab_release()


class GestionCategGUI:
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
        self.category_combobox['state'] = 'readonly'
        self.category_combobox.place(relx=0, rely=0.125, relwidth=1, relheight=0.15)

        btn_add_category = tk.Button(manage_main_frame, text="ajouter une catégorie", command=self.add_category,
                                     bd=2, activeforeground=RAISIN_BLACK, activebackground=GAINSBORO, bg=RAISIN_BLACK,
                                     fg=GAINSBORO, font=HELV_30_BUTTON_FONT)
        btn_add_category.place(relx=0, rely=0.4, relwidth=1, relheight=0.167)

        btn_modify_category = tk.Button(manage_main_frame, text="modifier une catégorie", command=self.edit_category,
                                        bd=2, activeforeground=RAISIN_BLACK, activebackground=GAINSBORO,
                                        bg=RAISIN_BLACK,
                                        fg=GAINSBORO, font=HELV_30_BUTTON_FONT)
        btn_modify_category.place(relx=0, rely=0.617, relwidth=1, relheight=0.167)

        btn_remove_category = tk.Button(manage_main_frame, text="supprimer une catégorie",
                                        bd=2, activeforeground=RAISIN_BLACK, activebackground=GAINSBORO,
                                        bg=RAISIN_BLACK,
                                        fg=GAINSBORO, font=HELV_30_BUTTON_FONT)
        btn_remove_category.place(relx=0, rely=0.833, relwidth=1, relheight=0.167)

        btn_exit = tk.Button(self.manage_window, text="retour", command=self.exit_window,
                             bd=0, activeforeground=RAISIN_BLACK, activebackground=MAIZE, bg=RAISIN_BLACK,
                             fg=MAIZE, font=HELV_20_BUTTON_FONT)
        btn_exit.place(relx=0.55, rely=0.85, relwidth=0.25, relheight=0.075)

        self.set_active()

    def edit_category(self):
        if len(self.category_combobox.get()) == 0:
            AlertPopUP(text='Veuillez sélectionner\nune catéorie')
        else:
            ModifyAddCategory(self.workbook, category_to_change=self.category_combobox.get())

    def add_category(self):
        ModifyAddCategory(self.workbook, add=True)

    def exit_window(self):
        self.manage_window.destroy()

    def set_active(self):
        self.manage_window.lift()
        self.manage_window.focus_force()
        self.manage_window.grab_set()
        self.manage_window.grab_release()


class ModifyAddCategory:
    def __init__(self, workbook, **kwargs):
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
            label_x = 0
            label_y = 0
            label_height = 0.1
            entry_x = 0
            entry_y = 0.12
            button_x = 0
            button_y = 0.45
        else:
            title = "mofifier une catégorie"
            label_text = "nouveau nom de " + kwargs.get('category_to_change')
            button_text = "modifier"
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
                                       fg=GAINSBORO, font=HELV_30_BUTTON_FONT)
        self.action_button.place(relx=button_x, rely=button_y, relwidth=1, relheight=0.25)

        self.action_button = tk.Button(edit_add_frame, text="retour", command=self.exit_window,
                                       bd=2, activeforeground=RAISIN_BLACK, activebackground=MAIZE,
                                       bg=RAISIN_BLACK,
                                       fg=MAIZE, font=HELV_30_BUTTON_FONT)
        self.action_button.place(relx=0, rely=0.75, relwidth=1, relheight=0.25)

    def exit_window(self):
        self.window.destroy()


if __name__ == "__main__":
    debug_workbook_gui = MenuGUI(Workbook())
