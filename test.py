import pandas
from pprint import pprint
import collections
excel_data_df = pandas.read_excel('wine2.xlsx', usecols=['Категория', 'Название', 'Сорт', 'Цена', 'Картинка'],
                                  na_values='', keep_default_na=False)
excel_data_df  = excel_data_df.fillna('')
products_group = collections.defaultdict(list)
for element in excel_data_df.to_dict(orient='record'):
    products_group[element['Категория']].append(element)
    element.pop('Категория')

pprint(products_group)