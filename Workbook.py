import csv


class Workbook:
    def __init__(self):
        self.category_dict = {'action': Category('action'),
                              'drame': Category('drame'),
                              'comedie': Category('comedie'),
                              'documentaire': Category('documentaire')}

    def add_category(self, name):
        self.category_dict.update({name: Category(name)})

    def remove_category(self, name):
        del self.category_dict[name]

    def add_film(self, category, name, year, **kwargs):
        self.category_dict.get(category).add_film(name, year, **kwargs)

    def edit_film(self, current_category, name, **kwargs):
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
        search_dict = dict()
        for key in self.category_dict.keys():
            search_dict.update(self.category_dict[key].find_films(**kwargs))
        return search_dict

    def write_search_results(self, path, *films):
        pass  # TODO Call methods from the csv lib to write the list of films to the target location

    # TODO open csv (possible issues, writing/opening the list/dict nested structure of the category_list.film_list) for
    def open_workbook(self):
        pass

    def save_workbook(self):
        pass


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
        getattr(self, "film_dict")[name].update(kwargs)

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
