import json



data_json = open('JsonReal.json')
jsontxt = data_json.read()
#print(jsontxt)

data_dict = json.loads(jsontxt)
print(data_dict)

data_dict['uniqueTournament'].pop('primaryColorHe')
data_dict['uniqueTournament'].pop('secondaryColorHe')
data_dict['uniqueTournament'].pop('logo')
data_dict['uniqueTournament'].pop('userCount')
data_dict['uniqueTournament'].pop('tier')



#print('\n\n\nnew dict->',data_dict) 

#popChave = input('digite a chave que deseja excluir: ')
#for chave in data_dict['uniqueTournament'].items():
 #   if(chave==popChave):
  #     data_dict['uniqueTournament'].pop() 
       

print('new Json->',data_dict)
