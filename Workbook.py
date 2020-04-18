import csv


class Workbook:
    def __init__(self, ):
        self.category_dict = {'action': Category('action'),
                              'drame': Category('drame'),
                              'comedie': Category('comedie'),
                              'documentaire':Category('documentaire')}

        # TODO implement rest of top level constructor

    def add_category(self, name):
        self.category_dict.update({'name': Category(name)})

    def remove_category(self, name):
        del self.category_dict[name]

    def add_film(self, category, name, year, **kwargs):
        self.category_dict.get(category).add_film(name, year, kwargs)

    def edit_film(self, currentcategory, name, **kwargs):
        if 'category' in kwargs:
            categ = self.category_dict.get(kwargs['category'])
            current_categ = self.category_dict.get(currentcategory)
            categ.film_list.update({name:current_categ.film_list.pop(name)})
            self.category_dict.get(kwargs['category']).edit_film(name, kwargs)
            currentcategory = kwargs['category']
        self.category_dict.get(currentcategory).edit_film(name,kwargs)

    def remove_film(self, name):
        pass  # TODO find and remove film

    def find_films(self, **kwargs):
        pass  # TODO search function using different input to return lists of film

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
        self.film_list = dict()

    def add_film(self, name, year, **kwargs):
        self.film_list.update({name: {
            'year': year,
            'category': self.name,
            'director': kwargs.get('director'),
            'actors': kwargs.get('actors'),  # TODO implement validation max 3
            'rating': kwargs.get('rating'),
            'comment': kwargs.get('comment')}
            }
        )

    def edit_film(self, name, **kwargs):
        for k, v in kwargs:
            self.film_list.get(name)[k] = v

    def find_film(self, **kwargs):
        pass  # TODO search function using different input (if 'key' in kwargs:) to return list of film

    def remove_film(self, name):
        del self.film_list[name]


if __name__ == "__main__":
    debug_workbook = Workbook()
