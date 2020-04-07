import os
import sys


class bcolors:
    DIRETORIO = '\033[94m'
    ARQUIVO = '\033[92m'
    ENDC = '\033[0m'


class SubDiretorio(object):
	def __init__(self, diretorioOrigem, posicao):
		self.diretorio = diretorio
		self.posicao = posicao
		self.acessar(self.diretorio)
		self.listagemDoDiretorio(self.diretorio, posicao)

	def listagemDoDiretorio(self, diretorio, posicao):
		dir = []
		arq = []
		for entry in os.scandir(self.origem + '/' + diretorio):
			if not entry.name.startswith('.') and entry.is_file():
				arq.append(entry.name)
				sys.stdout.write('|')
				for pos in range(posicao):
					sys.stdout.write('-')
				print(bcolors.ARQUIVO + entry.name + bcolors.ENDC)
			if not entry.name.startswith('.') and entry.is_dir():
				dir.append(entry.name)
				sys.stdout.write('|')
				for pos in range(posicao):
					sys.stdout.write('-')
				print(bcolors.DIRETORIO + entry.name + bcolors.ENDC)
		return dir

	def acessar(self, diretorio):
		try:
			os.chdir(self.diretorio)
		except NotADirectoryError:
			print('Erro: O caminho passado não é referente a um diretorio')
		except FileNotFoundError:
			print('Erro: Arquivo não encontrado')
		except PermissionError:
			print('Erro: Não é permitido acessar o arquivo')
		except OSError:
			print('Erro: Erro desconhecido')
		finally:
			self.listagemDoDiretorio(self.checar)

	def retornar(self, diretorio):
		try:
			os.chdir(self.diretorio)
		except NotADirectoryError:
			print('Erro: O caminho passado não é referente a um diretorio')
		except FileNotFoundError:
			print('Erro: Arquivo não encontrado')
		except PermissionError:
			print('Erro: Não é permitido acessar o arquivo')
		except OSError:
			print('Erro: Erro desconhecido')
		finally:
			self.listagemDoDiretorio(self.checar)

class Diretorio(object):
	"""docstring for Diretorio"""
	def __init__(self, checar):
		self.checar = checar
		print(self.checar)
		self.origem = os.getcwd()
		super(Diretorio, self).__init__()

	def acessar(self):
		try:
			os.chdir(self.origem)
		except NotADirectoryError:
			print('Erro: O caminho passado não é referente a um diretorio')
		except FileNotFoundError:
			print('Erro: Arquivo não encontrado')
		except PermissionError:
			print('Erro: Não é permitido acessar o arquivo')
		except OSError:
			print('Erro: Erro desconhecido')
		finally:
			self.listagemDoDiretorio(self.checar)

	def listagemDoDiretorio(self, diretorio):
		dir = []
		arq = []
		for entry in os.scandir(self.origem + '/' + diretorio):
			if not entry.name.startswith('.') and entry.is_file():
				arq.append(entry.name)
				sys.stdout.write('|-')
				print(bcolors.ARQUIVO + entry.name + bcolors.ENDC)
			if not entry.name.startswith('.') and entry.is_dir():
				dir.append(entry.name)
				sys.stdout.write('|-')
				print(bcolors.DIRETORIO + entry.name + bcolors.ENDC)
		for diretorio in dir:
			var = SubDiretorio(diretorio, 1)
		return dir

	def processar(self):
		print('Diretorio inicial: ', self.origem)
		#Receber a pasta de origem
		#Listar todos os diretorios e arquivos internos <------------------------------------|
		#Acessar o n-diretorio (Criar uma instancia da classe que represente n-diretorio)    |Loop
		#Listar >----------------------------------------------------------------------------|



def main():
	#argv[1] = diretorio em que o script fara a varredura
	#Exemplo: python gerenciamentodedados.py ../../diretorio
	#Irá fazer a varredura dois diretórios atrás

	try:
		var = Diretorio(sys.argv[1])
		var.acessar()
	except Exception as e:
		raise
	else:
		pass
	finally:
		pass
	
	pass


if __name__ == "__main__":
	main()