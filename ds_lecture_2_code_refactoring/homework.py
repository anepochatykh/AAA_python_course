"""
Реализуйте класс CountVectorizer, имеющий
- метод fit_transform
- метод get_feature_names
Условия:
- пользоваться внешними пакетами запрещено
- решение должно быть в *.py файлах
- не должно быть замечаний по PEP8
- решение загружено на github до ...
- если умеешь, то напиши проверки/тесты
Далее на слайдах пример получения терм-документной матрицы
https://ru.wikipedia.org/wiki/Терм-документная_матрица
"""

from sklearn.feature_extraction.text import CountVectorizer

if __name__ == "__main__":
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)

    print(vectorizer.get_feature_names())
    # Out: ['crock', 'pot', 'pasta', 'never', 'boil', 'again', 'pomodoro',
    #       'fresh', 'ingredients', 'parmesan', 'to', 'taste']

    # 'scipy.sparse._csr.csr_matrix'
    # попробовать сделать не через sparse_matrix, а через обычный массив
    print(type(count_matrix))
    print(count_matrix)
    # Out: [[1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    #       [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]]
