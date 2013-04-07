import urllib.request
import json
import os

class Facebook(object):

	def __init__(self,user):
		self.user = user
		
	def dados(url):
		#Pega os dados no Facebook
		#Precisa trocar a URL a cada 1h
		#Pegar no site, https://developers.facebook.com/docs/reference/api/examples/
		
		resp = urllib.request.urlopen(url).read()
		data = json.loads(resp.decode('utf-8'))	
		return data
	
	def baixarFoto(self):
		#data = self.procura()
		url = 'https://graph.facebook.com/' + self.user + '/picture?width=200&height=200'
		figura = urllib.request.urlopen(url).read()
		arq = 'images/sorteados/' + self.user + '.jpg'
		f = open(arq,"wb")
		f.write(figura)
		f.close()
		return arq

	def procura(self):    
	    url = 'https://graph.facebook.com/'	    
	    resp = urllib.request.urlopen(url+self.user).read()
	    data = json.loads(resp.decode('utf-8'))	    
	    return data

	def profile(self): #imprime todos os dados de um user
		data = self.procura()
		print ("User: " + data['username'])
		print ("Nome: " + data['first_name'])
		print ("Sobrenome: " + data['last_name'])
		print ("Local: " + data['locale'])
		print ("Sexo: " + data['gender'])
		print ("ID: " + data['id'])

	#Recebe a URL token, e o tipo chave que sera adicionada
	#Podendo ser 'id' ou 'username'
	#Retorna um tupla com a lista e o tamanho dela
	def listarAmigos(url, tipo):
		lista = []
		cont = 0

		#Mudar a cada 1h
		#Pegar no site, https://developers.facebook.com/docs/reference/api/examples/
		#Connections -> Friends		
		data = Facebook.dados(url)
		for amigo in data['data']:	
			lista.append(amigo[tipo]) #adiciona na lista pelo id
			cont += 1 #conta o numero de amigos
		return lista,cont

	def limpaDados():
		total_de_pessoas = 10
		try:
			dir_atual = os.getcwd()
			lista_Sorteados = os.listdir(dir_atual + '/images/sorteados/')
			if len(lista_Sorteados) > total_de_pessoas:
				for pessoa in lista_Sorteados:			
					os.remove(dir_atual + '/images/sorteados/' + pessoa)	
		except OSError:
			print ("\nArquivo ou diretório não existe!\n")
