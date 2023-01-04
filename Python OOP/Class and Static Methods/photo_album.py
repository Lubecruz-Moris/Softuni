import os
from math import ceil


class PhotoAlbum:
    PHOTOS_PER_PAGE = 4

    def __init__(self, pages):
        self.pages = pages
        self.__photos = self.build_matrix()

    @property
    def photos(self):
        return [[ele for ele in page if ele is not None] for page in self.__photos]

    def build_matrix(self):
        result = []
        for _ in range(self.pages):
            result.append([None] * self.PHOTOS_PER_PAGE)
        return result

    @classmethod
    def from_photos_count(cls, photos_count):
        pages = ceil(photos_count / PhotoAlbum.PHOTOS_PER_PAGE)
        return cls(pages)

    def add_photo(self, label):
        for page in range(self.pages):
            for position in range(PhotoAlbum.PHOTOS_PER_PAGE):
                if self.__photos[page][position] is None:
                    self.__photos[page][position] = label
                    return f"{label} photo added successfully on page {page + 1} slot {position + 1}"
        return "No more free slots"

    def display(self):
        delimiter = '-' * 11
        result = delimiter + os.linesep

        for page in self.__photos:
            page_str = ' '.join(['[]' if photo is not None else '' for photo in page])
            result += page_str.strip() + os.linesep + delimiter + os.linesep

        return result.strip()


album = PhotoAlbum(2)
print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
