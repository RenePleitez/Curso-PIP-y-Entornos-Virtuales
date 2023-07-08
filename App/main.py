import utils 
import read_csv 
import charts 


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

def run():
  data = read_csv.read_csv('data.csv')
  labels, values = world_population_percentage(data)
  charts.generate_pie_chart(labels, values)

# Código para generar un gráfico de barras de la población de un país a lo largo de un periodo de tiempo 
 
  country = input('Escribe un país: ')
  result = utils.population_by_countries(data, country)
  print(len(result))


  if len(result) > 0:
    country = result[0]
    labels, values = utils.get_population_project(country)
    charts.generate_bar_chart(country['Country/Territory'], labels, values)


if __name__ == '__main__':
  run()