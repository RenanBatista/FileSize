import os
import sys


class bcolors:
    DIRETORIO = '\033[94m'
    ARQUIVO = '\033[92m'
    ENDC = '\033[0m'


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
				sys.stdout.write('|')
				print(bcolors.ARQUIVO + entry.name + bcolors.ENDC)
			if not entry.name.startswith('.') and entry.is_dir():
				dir.append(entry.name)
				sys.stdout.write('|')
				print(bcolors.DIRETORIO + entry.name + bcolors.ENDC)
		return dir

	def processar(self):
		print('Diretorio inicial: ', self.origem)		


def main():
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