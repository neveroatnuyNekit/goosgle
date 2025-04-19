import json,re
from itertools import combinations
from collections import defaultdict


GET_OUT = {
    "for",
    "you",
    "this",
    "more",
    "without",
    "may",
    "through",
    "between",
    "after",
    "before",
    "thanks",
    "your",
}

def load(file):
    with open(file, "r", encoding="utf-8") as file:
        try:
            data = json.load(file)
        except json.decoder.JSONDecodeError:
            return {}
    return(data)

def make_ok(text:str):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    if len(text) <= 2 or text in GET_OUT:
        return None
    if text:
        return text
    return None


def main():
    req = "example"

    text = req

    text = text.split()
    text = map(make_ok, text)
    text = [x for x in text if x is not None]
    text = " ".join(text)

    print(text)

    ind = load("indexes.json")

    if len(text.split()) == 0:
        print("Not vaild request")
        return

    if len(text.split()) == 1:
        print(ind.get(text, None))
        return

    # alles = []

    b = text.split()

    
    lists = [ind[key] for key in b if key in ind]
    element_counts = defaultdict(int)
    result = []

    # Сначала проходимся по всем комбинациям от n до 1
    for r in range(len(lists), 0, -1):
        for indices in combinations(range(len(lists)), r):
            current_lists = [lists[i] for i in indices]
            common_elements = set(current_lists[0])
            for lst in current_lists[1:]:
                common_elements.intersection_update(lst)
            for elem in common_elements:
                if elem not in result:  # Добавляем только новые элементы
                    result.append(elem)
                    element_counts[elem] = r  # Запоминаем, в скольки списках встретился

    # Сортируем результат по убыванию количества вхождений
    result.sort(key=lambda x: -element_counts[x])

    print(result)

main()

# print(ind.get(req, None))