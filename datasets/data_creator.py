import csv
import json

from django.db import models


def ads_csv_to_json(csv_file: csv, json_file: json, model: models):
    """ Конвертируем csv файл в json для последующей заливки в БД"""
    with open(csv_file, newline='') as file:
        data_list = []
        reader = csv.DictReader(file)
        for row in reader:
            data_dict = {"model": model, "pk": row['id'], "fields": row}

            del data_dict["fields"]["id"]

            if "price" in data_dict["fields"]:
                data_dict["fields"]["price"] = int(data_dict["fields"]["price"])

            if "is_published" in data_dict["fields"]:
                data_dict["fields"]["is_published"] = bool(data_dict["fields"]["is_published"])

            data_list.append(data_dict)
    with open(json_file, 'w', encoding='utf-8') as file:
        file.write(json.dumps(data_list, ensure_ascii=False))


ads_csv_to_json('./datasets/ad.csv', './datasets/ads.json', 'ads.ads')
ads_csv_to_json('./datasets/category.csv', './datasets/category.json', 'ads.categories')
ads_csv_to_json('./datasets/location.csv', './datasets/location.json', 'users.locations')
ads_csv_to_json('./datasets/user.csv', './datasets/user.json', 'users.user')
