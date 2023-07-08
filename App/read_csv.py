import csv


def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    header = next(reader)
    data = []

    for row in reader:
      iterable = zip(header, row)
      country_dict = {key: value for key, value in iterable}
      data.append(country_dict) 

  return data
    

if __name__ == '__main__':
  final_data = read_csv('./App/data.csv')
  #print(final_data)
  # Filtrando la lista para únicamente obtener los datos de México.
  #print(list(filter(lambda x : x['Country/Territory'] == 'Mexico', final_data)))
  #Utilizando la función map para obtener una lista de las capitales de todos los países mencionados en el archivo csv.
  #print(list(map(lambda x : x['Capital'], final_data)))