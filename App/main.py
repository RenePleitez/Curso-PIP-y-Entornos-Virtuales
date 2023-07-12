import utils 
import read_csv 
import charts 
import pandas as pd


"""
# Código para generar un gráfico de pastel del porcentaje de población mundial correspondiente a cada país de un continente específico (en este caso Sudamérica)
def world_population_percentage(data):
  
  data = list(filter(lambda x : x['Continent'] == 'South America', data))
  country_name = list(map(lambda x : x['Country/Territory'], data))
  for country in data:
    world_population = list(map(lambda x : float(x['World Population Percentage']), data))
    iterable = list(zip(country_name, world_population))
    world_dict = {key: value for key, value in iterable}
    labels = world_dict.keys()
    values = world_dict.values()
  return labels, values
"""

# Código para generar un gráfico de pastel del porcentaje de población mundial correspondiente a cada país de un continente específico (en este caso África) usando Pandas.
def run():
  df = pd.read_csv('data.csv') #Esta línea utiliza el método read_csv() que incluye esta librería, el cual permite ahorrarnos el módulo read_csv que creamos nosotros para pasar un CSV a formato de diccionario; además, estamos cubriendo otros casos que no estábamos teniendo en cuenta y Pandas sí.
  df = df[df['Continent'] == 'Africa'] #Esta línea indica que solo quiero seleccionar los datos en donde la columna Continet sea igual a Africa.
  countries = df['Country/Territory'].values #Esta línea obtiene los valores (nombres) de la columna Country/Territory de los países de interés (filtrados por continente anteriormente).
  percentages =df['World Population Percentage'].values #Esta línea obtiene los valores (porcentaje de población) de la columna World Population Percentage de los países de interés
  charts.generate_pie_chart(countries, percentages) #Esta línea genera el gráfico de pastel.
  
  """
def run():
  data = read_csv.read_csv('data.csv')
  labels, values = world_population_percentage(data)
  charts.generate_pie_chart(labels, values)
  """
  
# Código para generar un gráfico de barras de la población de un país a lo largo de un periodo de tiempo 
  data = read_csv.read_csv('data.csv')
  country = input('Escribe un país: ')
  country = country.capitalize() # Agregamos esta línea para que evitar errores de typo por diferencias entre como lo escribió el usuario y como está en los datos.
  result = utils.population_by_countries(data, country)
  print(len(result))
  print(result)

  if len(result) > 0:
    country = result[0]
    labels, values = utils.get_population_project(country)
    charts.generate_bar_chart(country['Country/Territory'], labels, values)


if __name__ == '__main__':
  run()