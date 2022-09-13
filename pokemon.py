import request

#Nombre: Kevin Yair Peña Salazar
#Matricula:1827227

if __name__ == '__main__':
	url = 'https://pokeapi.co/api/v2/pokemon-form/'
 	
	response = request.get(url)
	if response.status_code == 200:
		payload = response.json()
		results = payload.get('results',[])

	if results:
		for pokemon in results
			name = pokemon['name']
			print(name)
