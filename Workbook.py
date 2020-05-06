import csv


class Workbook:
    def __init__(self):
        self.category_dict = dict()
        try:
            self.open_workbook()
        except FileNotFoundError:
            self.category_dict = {'Action': Category('Action'),
                                  'Drame': Category('Drame'),
                                  'Comedie': Category('Comedie'),
                                  'Documentaire': Category('Documentaire')}

    def add_category(self, name):
        self.category_dict.update({name: Category(name)})

    def remove_category(self, name):
        del self.category_dict[name]

    def add_film(self, category, name, year, **kwargs):
        """
        :param kwargs:
            director= str
            actors=  list[str]
            rating= int < 10
            comment= str
        """
        self.category_dict.get(category).add_film(name, year, **kwargs)

    def edit_film(self, current_category, current_name, **kwargs):
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

    def remove_film(self, name, category):
        self.category_dict.get(category).film_dict.pop(name)

    def find_films(self, **kwargs):
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
                if'category' in kwargs:
                    if kwargs.get('category') == key:
                        search_dict.update(self.category_dict[key].film_dict)
                        continue
                else:
                    search_dict.update(self.category_dict[key].find_films(**kwargs))
        return search_dict

    def open_workbook(self):
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

    def save_workbook(self):
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
    def save_search(path, film_dict):  # TODO fix duplicate saves
        to_write = list()
        for kf, vf in film_dict.items():
            to_write.append([kf, vf.get('year'),
                             vf.get('category'), vf.get('director'),
                             vf.get('actors'), vf.get('rating'),
                             vf.get('comment')])
        Workbook.write_list(path, to_write)

    @staticmethod
    def write_list(path, to_write):
        col_name = ['name', 'year', 'category', 'director', 'actors', 'rating', 'comment']
        with open(path, mode='w', newline='') as workbook_file:
            workbook_writer = csv.writer(workbook_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            workbook_writer.writerow(col_name)
            workbook_writer.writerows(to_write)


class Category:
    def __init__(self, name):
        self.name = name
        self.film_dict = dict()

    def add_film(self, name, year, **kwargs):
        self.film_dict.update({name: {
            'year': year,
            'category': str(self.name),
            'director': kwargs.get('director'),
            'actors': kwargs.get('actors'),
            'rating': kwargs.get('rating'),
            'comment': kwargs.get('comment')}
        }
        )

    def edit_film(self, current_name, **kwargs):
        if kwargs.get('name'):
            self.film_dict.update({kwargs.get('name'): self.film_dict.pop(current_name)})
            current_name = kwargs.pop('name')
        self.film_dict.get(current_name).update(kwargs)

    def find_films(self, **kwargs):
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

    def remove_films(self, name):
        del self.film_dict[name]


if __name__ == "__main__":
    debug_workbook = Workbook()
    input()
