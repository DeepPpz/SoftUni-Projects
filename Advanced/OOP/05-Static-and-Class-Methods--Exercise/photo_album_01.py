import math


class PhotoAlbum:
    MAX_PHOTOS = 4
    
    def __init__(self, pages: int) -> None:
        self.pages = pages
        self.photos = [[] for _ in range(pages)]
    
    @classmethod
    def from_photos_count(cls, photos_count: int) -> "PhotoAlbum":
        pages = math.ceil(photos_count / PhotoAlbum.MAX_PHOTOS)
        return PhotoAlbum(pages)
    
    def add_photo(self, label: str) -> str:
        for row in range(len(self.photos)):
            if len(self.photos[row]) < PhotoAlbum.MAX_PHOTOS:
                self.photos[row].append(label)
                return f"{label} photo added successfully on page {len(self.photos)} slot {len(self.photos[-1])}"
        return "No more free slots"
    
    def display(self) -> str:
        result = "-----------"
        for i in range(self.pages):
            result += f"\n{' '.join('[]' for photo in range(len(self.photos[i])))}"
            result += f"\n-----------"
        return result
