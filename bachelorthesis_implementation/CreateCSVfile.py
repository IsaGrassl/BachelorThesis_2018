import json
import csv
import random
import nltk

jsonData = json.load(open('collections.json'))

dataset_csv = open('dataset.csv', 'w')  # open file
csv_file = csv.writer(dataset_csv)  # create csv writer object

csv_file.writerow(['task_id', ])  # header row

# for item in jsonData:
# csv_file.writerow()

dataset_csv.close()


# returns a list of 20 random collections
def load_collections(collections_path, all_abstracts):
    json_data = open(collections_path)
    collections_data = json.load(json_data)
    key_list = list(collections_data.keys())

    collection_key_list = []
    while len(collection_key_list) < 20:
        random_collection = random.choice(key_list)
        if random_collection not in collection_key_list and check_language(collections_data[random_collection],
                                                                           all_abstracts):
            collection_key_list.append([random_collection])

    collection_list = []
    for collection_key in collection_key_list:
        collection_list.append(collections_data[collection_key[0]])

    return collection_list

# verifies that the language of the extracted abstracts is English
def check_language(collection, all_abstracts):
    is_english = True
    for abstract_id in collection['collection']:
        print(json.loads(all_abstracts[(int(abstract_id) - 1)])['language'][0])
        if json.loads(all_abstracts[(int(abstract_id) - 1)])['language'][0] != 'eng':
            is_english = False
    for candidate in collection['candidates'].keys():
        if json.loads(all_abstracts[int(collection['candidates'][candidate]) - 1])['language'][0] != 'eng':
            is_english = False
    return is_english



# first approach of writing abstracts to the given collections in a csv file
# each keyword will be written in its own column
def load_econstar_dataset(dataset_path, keyword_path, collections_path):
    dataset = open(dataset_path)
    keywords_file = open(keyword_path)
    keywords = json.load(keywords_file)  # keyword dictionary; each key is a document id
    all_abstracts = dataset.readlines()  # List that holds all abstract dictionaries. The row nr. is the abstract id (indices).
    collections = load_collections(collections_path, all_abstracts)
    candidate_keys = ['sim', 'intermediate', 'dissim']
    outfile = open('out_new.csv', 'w')

    fieldnames = ['id', 'id_0', 'abstract_0', 'id_1', 'abstract_1', 'id_2', 'abstract_2', 'id_3', 'type_3',
                  'abstract_3', 'keyword_0', 'keyword_1', 'keyword_2', 'keyword_3', 'keyword_4', 'keyword_5',
                  'keyword_6', 'keyword_7', 'keyword_8', 'keyword_9', 'keyword_10', 'keyword_11',
                  'keyword_switch_index', 'keyword_mapping_sim', 'keyword_mapping_dissim']
    csv_writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    csv_writer.writeheader()

    row_id = 0
    for collection in collections:  # collections given by the method load_collections
        csv_row = {'id': row_id}  # dictionary
        row_id = row_id + 1
        abstract_id = 0
        for line_nr in collection[
            'collection']:  # collection['collection'] = list of 3 line nr's each representing an abstract
            csv_row['id_' + str(abstract_id)] = line_nr
            csv_row['abstract_' + str(abstract_id)] = clean_abstract(
                json.loads(all_abstracts[int(line_nr) - 1])['abstract'])
            abstract_id = abstract_id + 1

        candidate_key = random.choice(candidate_keys)
        candidate_id = collection['candidates'][candidate_key]
        csv_row['id_3'] = candidate_id
        csv_row['type_3'] = candidate_key
        print(json.loads(all_abstracts[14782]).keys())
        print(json.loads(all_abstracts[14782]))
        print(json.loads(all_abstracts[14783]).keys())
        print(json.loads(all_abstracts[14783]))

        abstract_3 = clean_abstract(json.loads(all_abstracts[int(candidate_id) - 1])['abstract'])
        csv_row['abstract_3'] = abstract_3
        similar_list, dissimilar_list = get_keywords2(collection['collection'], candidate_id, keywords)
        switch_index = get_switch_index(len(similar_list), len(dissimilar_list))
        for i in range(switch_index):
            csv_row['keyword_' + str(i)] = similar_list[i][0]
        for i in range(len(dissimilar_list)):
            if i < 12 - switch_index:
                csv_row['keyword_' + str(i + switch_index)] = dissimilar_list[i][0]
        csv_row['keyword_switch_index'] = switch_index
        csv_row['keyword_mapping_sim'] = similar_list
        csv_row['keyword_mapping_dissim'] = dissimilar_list
        csv_writer.writerow(csv_row)


# writes the abstracts fitting to the given collections in a csv file
# keywords will be written in one column (per category), separated with '_' according to CrowdFlowers restrictions
def load_econstar_dataset2(dataset_path, keyword_path, collections_path):
    dataset = open(dataset_path)
    keywords_file = open(keyword_path)
    keywords = json.load(keywords_file)  # keyword dictionary; each key is a document id
    all_abstracts = dataset.readlines()  # List that holds all abstract dictionaries. The row nr. is the abstract id (indices).
    collections = load_collections(collections_path, all_abstracts)
    candidate_keys = ['sim', 'intermediate', 'dissim']
    outfile = open('out_new2.csv', 'w')

    fieldnames = ['id', 'id_0', 'abstract_0', 'id_1', 'abstract_1', 'id_2', 'abstract_2', 'id_3', 'type_3',
                  'abstract_3', 'keyword_sim', 'keyword_dissim', 'keyword_mapping_sim', 'keyword_mapping_dissim']
    csv_writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    csv_writer.writeheader()

    row_id = 0
    for collection in collections:  # collections given by the method load_collections
        csv_row = {'id': row_id}  # dictionary
        row_id = row_id + 1
        abstract_id = 0
        for line_nr in collection[
            'collection']:  # collection['collection'] = list of 3 line nr's each representing an abstract
            csv_row['id_' + str(abstract_id)] = line_nr
            csv_row['abstract_' + str(abstract_id)] = clean_abstract(
                json.loads(all_abstracts[int(line_nr) - 1])['abstract'])
            abstract_id = abstract_id + 1

        candidate_key = random.choice(candidate_keys)
        candidate_id = collection['candidates'][candidate_key]
        csv_row['id_3'] = candidate_id
        csv_row['type_3'] = candidate_key
        print(json.loads(all_abstracts[14782]).keys())
        print(json.loads(all_abstracts[14782]))
        print(json.loads(all_abstracts[14783]).keys())
        print(json.loads(all_abstracts[14783]))

        abstract_3 = clean_abstract(json.loads(all_abstracts[int(candidate_id) - 1])['abstract'])
        csv_row['abstract_3'] = abstract_3
        similar_list, dissimilar_list = get_keywords2(collection['collection'], candidate_id, keywords)
        switch_index = get_switch_index(len(similar_list), len(dissimilar_list))
        similar_string = ""
        for i in range(switch_index):
            similar_string = similar_string + similar_list[i][0] + "_"
        csv_row['keyword_sim'] = similar_string[0:len(similar_string) - 1]
        dissimilar_string = ""
        for i in range(len(dissimilar_list)):
            if i < 12 - switch_index:
                dissimilar_string = dissimilar_string + dissimilar_list[i][0] + "_"
        csv_row['keyword_dissim'] = dissimilar_string[0:len(dissimilar_string) - 1]
        csv_row['keyword_mapping_sim'] = similar_list
        csv_row['keyword_mapping_dissim'] = dissimilar_list
        csv_writer.writerow(csv_row)

# key phrases will be selected with respect to set operations
def get_keywords2(collection_id_list, candidate_id, keywords):
    # example_keyword = ("keyword", "doc_id", "algorithm")
    keywords_collection_set = set()
    for doc_id in collection_id_list:
        keyword_dict = keywords[str(doc_id)]
        for algorithm in keyword_dict.keys():
            for keyword in keyword_dict[algorithm]:
                keywords_collection_set.add(keyword)
    keywords_candidate = []
    keyword_dict = keywords[str(candidate_id)]
    for algorithm in keyword_dict.keys():
        for keyword in keyword_dict[algorithm]:
            keywords_candidate.append((keyword, candidate_id, algorithm))
    keywords_candidate_set = set()
    for keyword_tuple in keywords_candidate:
        keywords_candidate_set.add(keyword_tuple[0])
    similar_set = keywords_candidate_set & keywords_collection_set
    similar_list = []
    dissimilar_set = keywords_candidate_set - keywords_collection_set
    dissimilar_list = []
    for keyword_tuple in keywords_candidate:
        if keyword_tuple[0] in similar_set:
            similar_list.append(keyword_tuple)
        elif keyword_tuple[0] in dissimilar_set:
            dissimilar_list.append(keyword_tuple)
    random.shuffle(similar_list)
    random.shuffle(dissimilar_list)
    return similar_list, dissimilar_list


# the first three key phrases from every algorithm will be selected
def get_keywords(keywords, abstract):
    keyword_list = []
    index_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    random.shuffle(index_list)
    for algorithm in list(keywords.keys()):
        keyword_list.extend(keywords[algorithm][0:3])
        if len(keywords[algorithm][0:3]) < 3:
            # TODO if no more available keywords
            print("Hello")
    keyword_list.extend(get_random_keywords(abstract))
    print(keyword_list)
    keyword_random_list = []
    position_map = dict(
        {'TFIDF': index_list[0:3], 'Rake': index_list[3:6], 'textRank': index_list[6:9], 'random': index_list[9:12]})
    position_dict = dict()
    for i in range(12):
        position_dict[index_list[i]] = keyword_list[i]
    for i in range(12):
        keyword_random_list.append(position_dict[i])
    return keyword_random_list, position_map


def get_random_keywords(abstract):
    random_keywords = []
    word_list = abstract.split(" ")
    while len(random_keywords) < 3:
        keyword = random.choice(word_list)
        if len(keyword) >= 3 and keyword not in nltk.corpus.stopwords.words('english'):
            random_keywords.append(keyword)
    return random_keywords


def clean_abstract(abstract):
    new_abstract = abstract[0]
    if new_abstract.startswith('"') and new_abstract.endswith('"'):
        new_abstract = new_abstract[1:-1]
    return new_abstract


def get_switch_index(length_1, length_2):
    if length_1 < 6:
        return length_1
    elif length_2 > 6:
        return 6
    else:
        return 12 - length_2


if __name__ == '__main__':
    nltk.download('stopwords')
    load_econstar_dataset2('dataset_econstar//econstor_2017-06-01.json', 'CDS_Dataset//keywords.json',
                           'collections.json')
