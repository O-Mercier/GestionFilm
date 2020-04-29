import csv


class Workbook:
    def __init__(self):
        self.category_dict = dict()
        try:
            self.open_workbook()
        except FileNotFoundError:
            self.category_dict = {'Action': Category('action'),
                                  'Drame': Category('drame'),
                                  'Comedie': Category('comedie'),
                                  'Documentaire': Category('documentaire')}

    def add_category(self, name):
        self.category_dict.update({name: Category(name)})

    def remove_category(self, name):
        del self.category_dict[name]

    def add_film(self, category, name, year, **kwargs):
        """
        kwargs:
            director= str
            actors=  list[str]
            rating= int < 10 TODO Implement validation max 10 in controler
            comment= str
        """

        self.category_dict.get(category).add_film(name, year, **kwargs)

    def edit_film(self, current_category, name, **kwargs):
        """
        kwargs:
            category= str
            director= str
            actors=  list[str]
            rating= int < 10 TODO Implement validation max 10 in controler
            comment= str
        """
        if 'category' in kwargs:
            current_categ = self.category_dict.get(current_category)
            categ = self.category_dict.get(kwargs.get('category'))
            categ.film_dict.update({name: current_categ.film_dict.pop(name)})
            current_category = kwargs.get('category')
        self.category_dict.get(current_category).edit_film(name, **kwargs)

    def remove_film(self, name):
        for categ in self.category_dict.keys():
            for key in self.category_dict[categ].film_dict.keys():
                if key == name:
                    del self.category_dict[categ].film_dict[key]

    def find_films(self, **kwargs):
        """
        kwargs:
            name= str
            category= str
            director= str
            actors=  list[str]
            rating= int < 10 TODO Implement validation max 10 in controler
            comment= str
        """
        search_dict = dict()
        for key in self.category_dict.keys():
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
                        self.category_dict.get(row[2]).add_film(row[0],row[1], director=row[3], actors=row[4],rating=row[5],comment=row[6])
                    line_count += 1
        except FileNotFoundError:
            raise

    def save_workbook(self):
        to_write = list()
        for k, v in self.category_dict.items():
            for kf, vf in v.film_dict.items():
                to_write.append(
                    [kf, vf['year'], vf['category'], vf['director'], vf['actors'], vf['rating'], vf['comment']])
        self.write_list('workbook_file.csv', to_write)

    def write_list(self, path, to_write):
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
            'actors': kwargs.get('actors'),  # TODO implement validation max 3
            'rating': kwargs.get('rating'),
            'comment': kwargs.get('comment')}
        }
        )

    def edit_film(self, name, **kwargs):
        self.film_dict[name].update(kwargs)

    def find_films(self, **kwargs):
        search_dict = dict()
        for key in self.film_dict.keys():
            for kw in kwargs.keys():
                if kwargs[kw] == self.film_dict[key][kw]:
                    search_dict[key] = self.film_dict[key]
        return search_dict

    def remove_films(self, name):
        del self.film_dict[name]


if __name__ == "__main__":
    debug_workbook = Workbook()
    input()

