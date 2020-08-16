from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
import pandas
import datetime
import collections

env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

now = datetime.datetime.now()
now_year = now.year
start_year = 1920
life_year = now_year - start_year

template = env.get_template('template.html')
rendered_page = template.render(
    life_year = str(life_year)
)
excel_data_df = pandas.read_excel('wine3.xlsx', usecols=['Категория', 'Название', 'Сорт', 'Цена', 'Картинка', 'Акция'],
                                  na_values='', keep_default_na=False)
excel_data_df  = excel_data_df.fillna('')
products_group = collections.defaultdict(list)
for element in excel_data_df.to_dict(orient='record'):
    products_group[element['Категория']].append(element)
    element.pop('Категория')

rendered_page = template.render(categories=products_group)

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)


server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()
