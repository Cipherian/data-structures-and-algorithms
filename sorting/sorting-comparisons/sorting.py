from movies import movies as mov

def sort_by_title(movies):
    sorted_titles = []
    def remove_article(title):
        if title.lower().startswith('a '):
            return title[2:]
        elif title.lower().startswith('an '):
            return title[3:]
        elif title.lower().startswith('the '):
            return title[4:]
        return title

    def quick_sort(movies):
            if not movies:
                return []

            index = movies[0]
            left = [movie for movie in movies if movies[1:] if remove_article(movie['title']) < remove_article(index['title'])]
            right = [movie for movie in movies if movies[1:] if remove_article(movie['title']) > remove_article(index['title'])]

            left_sorted = quick_sort(left)
            right_sorted = quick_sort(right)

            return left_sorted + [index] + right_sorted

    for movie in sort_helper(movies):
        sorted_titles.append(movie['title'])
    return sorted_titles


def sort_by_year(movies):
    # Create a new list with each dictionary as a tuple (year, movie)
    movie_list = [movie for movie in movies]
    sorted_list = []

    def quicksort(arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[0]
        right = [x for x in arr[1:] if x['year'] < pivot['year']]
        left = [x for x in arr[1:] if x['year'] >= pivot['year']]
        return quicksort(left) + [pivot] + quicksort(right)

    movie_list = quicksort(movie_list)
    for movie in movie_list:
        if not movie:
            pass
        sorted_list.append(movie['title'])
    return sorted_list

print(sort_by_year(mov))
