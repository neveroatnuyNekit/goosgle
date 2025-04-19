import json,re
from itertools import combinations
from collections import defaultdict
from urllib.parse import urlparse
from fuzzywuzzy import fuzz

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

def is_like_url(query, url, threshold=70):
    parsed_url = urlparse(url)
    domain_parts = parsed_url.netloc.split('.')
    path_parts = parsed_url.path.strip('/').split('/')
    url_keywords = []
    url_keywords.extend(domain_parts[:-1]) 
    url_keywords.extend(path_parts)
    url_keywords = [part for part in url_keywords if part] 
    query_words = re.findall(r'\w+', query.lower())
    
    for word in query_words:
        for part in url_keywords:
            similarity = fuzz.ratio(word.lower(), part.lower())
            if similarity >= threshold:
                return True
    return False

def find_most_similar_url(query, urls, threshold=70):
    best_match = None
    best_score = 0
    
    for url in range(len(urls)):
        score = 0
        parsed_url = urlparse(urls[url])
        domain_parts = parsed_url.netloc.split('.')
        path_parts = parsed_url.path.strip('/').split('/')
        
        url_keywords = []
        url_keywords.extend(domain_parts[:-1])
        url_keywords.extend(path_parts)
        url_keywords = [part for part in url_keywords if part]
        
        query_words = re.findall(r'\w+', query.lower())
        
        for word in query_words:
            for part in url_keywords:
                current_score = fuzz.ratio(word.lower(), part.lower())
                if current_score > score:
                    score = current_score
        
        if score > best_score and score >= threshold:
            best_score = score
            best_match = url
    
    return best_match

def main():
    req = "cookies 2 cash"

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

    # print(element_counts)
    reit = [element_counts[x] for x in result]

    reit[int(find_most_similar_url(text,result))] += 5
    # print(reit)
    # Сортируем результат по убыванию количества вхождений
    # result.sort(key=lambda x: -reit[int(x)])
    # paired = sorted(zip(reit, result), key=lambda x: x[0])

    # Извлекаем отсортированные элементы b
    # sorted_b = [item[1] for item in paired]
    result = [x for _, x in sorted(zip(reit, result), key=lambda pair: pair[0])]

    # print()
    print(result)
    # print()
    

main()

# print(ind.get(req, None))