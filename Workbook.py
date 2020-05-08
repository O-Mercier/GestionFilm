import csv


class Workbook:  # Classe de gestion des categorie
    def __init__(self):
        self.category_dict = dict()
        try:
            self.open_workbook()
        except FileNotFoundError:
            self.category_dict = {'Action': Category('Action'),
                                  'Drame': Category('Drame'),
                                  'Comedie': Category('Comedie'),
                                  'Documentaire': Category('Documentaire')}

    def add_category(self, name):  # Ajoute une categorie au category_dict
        self.category_dict.update({name: Category(name)})

    def remove_category(self, name):  # retire une categorie au category_dict
        del self.category_dict[name]

    def edit_category(self, current_name, new_name):  # modifie une categorie au category_dict
        self.category_dict.update({new_name: self.category_dict.pop(current_name)})
        self.category_dict.get(new_name).rename_category(new_name)

    def add_film(self, category, name, year, **kwargs):  # ajoute un film dans sa categorie
        """
        :param kwargs:
            director= str
            actors=  list[str]
            rating= int < 10
            comment= str
        """
        self.category_dict.get(category).add_film(name, year, **kwargs)

    def edit_film(self, current_category, current_name, **kwargs):  # modifie un film dans sa categorie
        """
       :param kwargs:
            name=str
            category=str
            director=str
            actors=list[str]
            rating=int < 10
            comment=str
        """
        if 'category' in kwargs:
            current_categ = self.category_dict.get(current_category)
            categ = self.category_dict.get(kwargs.get('category'))
            categ.film_dict.update({current_name: current_categ.film_dict.pop(current_name)})
            categ.film_dict.get(current_name).update(category=kwargs.get('category'))
            current_category = kwargs.pop('category')
        self.category_dict.get(current_category).edit_film(current_name, **kwargs)

    def remove_film(self, name, category):  # retire un film dans sa categorie
        self.category_dict.get(category).film_dict.pop(name)

    def find_films(self, **kwargs):  # produit une liste de films avec les kwargs fournis
        """
        :param kwargs:
            name= str
            category= str
            director= str
            actors=  list[str]
            rating= int < 10
            comment= str
            all=True
        """
        search_dict = dict()
        for key in self.category_dict.keys():
            if kwargs.get('all'):
                search_dict.update(self.category_dict[key].film_dict)
            else:
                if 'category' in kwargs:
                    if kwargs.get('category') == key:
                        search_dict.update(self.category_dict[key].film_dict)
                        continue
                else:
                    search_dict.update(self.category_dict[key].find_films(**kwargs))
        return search_dict

    def open_workbook(self):  # ouvre le CSV workbook_file et va y chercher les films ajouter par le passe
        try:
            with open('workbook_file.csv', newline='') as workbook_file:
                workbook_reader = csv.reader(workbook_file, delimiter=',')
                line_count = 0
                for row in workbook_reader:
                    if line_count == 0:
                        pass
                    else:
                        if not self.category_dict.get(row[2]):
                            self.add_category(row[2])
                        self.category_dict.get(row[2]).add_film(row[0], row[1], director=row[3], actors=row[4],
                                                                rating=row[5], comment=row[6])
                    line_count += 1
        except FileNotFoundError:
            raise
        if not self.category_dict:
            self.category_dict = {'Action': Category('Action'),
                                  'Drame': Category('Drame'),
                                  'Comedie': Category('Comedie'),
                                  'Documentaire': Category('Documentaire')}

    def save_workbook(self):  # construit une liste a ecrire a partir de category_dict
        to_write = list()
        for k, v in self.category_dict.items():
            for kf, vf in v.film_dict.items():
                to_write.append(
                    [kf, vf['year'],
                     vf['category'], vf['director'],
                     vf['actors'], vf['rating'],
                     vf['comment']])
        self.write_list('workbook_file.csv', to_write)

    @staticmethod
    def save_search(path, film_dict):  # construit une liste a partir d'un dict de film, methode static
        to_write = list()
        for kf, vf in film_dict.items():
            to_write.append([kf, vf.get('year'),
                             vf.get('category'), vf.get('director'),
                             vf.get('actors'), vf.get('rating'),
                             vf.get('comment')])
        Workbook.write_list(path, to_write)

    @staticmethod
    def write_list(path, to_write):  # ecrit une liste au path dans un csv, methode static
        col_name = ['name', 'year', 'category', 'director', 'actors', 'rating', 'comment']
        with open(path, mode='w', newline='') as workbook_file:
            workbook_writer = csv.writer(workbook_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            workbook_writer.writerow(col_name)
            workbook_writer.writerows(to_write)


class Category:  # sous classe d'organisation de film, contient les fiche de films
    def __init__(self, name):
        self.name = name
        self.film_dict = dict()

    def rename_category(self, new_name):  # change le nom de la categorie dans les entree de film
        self.name = new_name
        for key in self.film_dict.keys():
            self.film_dict.get(key).update({'category': str(self.name)})

    def add_film(self, name, year, **kwargs):  # ajoute un film au film_dict avec les kwargs fournis
        self.film_dict.update({name: {
            'year': year,
            'category': str(self.name),
            'director': kwargs.get('director'),
            'actors': kwargs.get('actors'),
            'rating': kwargs.get('rating'),
            'comment': kwargs.get('comment')}
        })

    def edit_film(self, current_name, **kwargs):  # modifie un film au film_dict avec les kwargs fournis
        if kwargs.get('name'):
            self.film_dict.update({kwargs.get('name'): self.film_dict.pop(current_name)})
            current_name = kwargs.pop('name')
        self.film_dict.get(current_name).update(kwargs)

    def remove_films(self, name):  # retire un film
        del self.film_dict[name]

    def find_films(self, **kwargs):  # cherche des films dans la categorie, retourne un search_dict
        """
        :param
        kwargs:
        name = str
        director = str
        actors = list[str]
        rating = int < 10
        """
        search_dict = dict()
        for key, value in self.film_dict.items():
            for k, v in kwargs.items():
                if k == 'name':
                    if v == key:
                        search_dict[key] = value
                elif k == 'actors':
                    if set(kwargs.get('actors')).intersection(v):
                        search_dict[key] = value
                elif v == value.get(k):
                    search_dict[key] = value
        return search_dict
