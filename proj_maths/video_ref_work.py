import csv

def get_video_ref_list():
    """Метод по отображению информации о ссылках"""
    terms = []
    with open("./data/video_ref.csv", "r", encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter=';')
        for index, row in enumerate(reader):
            cnt = index + 1
            term = row['term']
            ref = row['ref']
            ref_definition = row['ref_definition']
            terms.append([cnt, term, ref, ref_definition])
    return terms

def write_video_ref(new_term, new_ref, new_ref_definition):
    """Метод по добалвению ссылки в базу данных"""
    with open("./data/video_ref.csv", "a", encoding="utf-8", newline='\n') as f:
        writer = csv.DictWriter(f, delimiter=";", fieldnames=["term", "ref", "ref_definition"])
        writer.writerow({"term": new_term, "ref": new_ref, "ref_definition": new_ref_definition})
