import os
import sys


class bcolors:
    DIRETORIO = '\033[94m'
    ARQUIVO = '\033[92m'
    ENDC = '\033[0m'


class SubDiretorio(object):
	
	#Receber a pasta de origem
	#Listar todos os diretorios e arquivos internos <------------------------------------|
	#Acessar o n-diretorio (Criar uma instancia da classe que represente n-diretorio)    |Loop
	#Listar >----------------------------------------------------------------------------|
	def __init__(self, diretorioOrigem='.', diretorioDestino='.', posicao=0):
		self.diretorioDestino = diretorioDestino
		self.diretorioOrigem = diretorioOrigem
		self.posicao = posicao
		if(self.acessar(self.diretorioDestino)):
			self.listagemDoDiretorio(self.diretorioDestino, posicao)	

	def listagemDoDiretorio(self, diretorio, posicao):
		dir = []
		arq = []
		diretorioAtual = os.getcwd()

		for entry in os.scandir(diretorioAtual):
			if not entry.name.startswith('.') and entry.is_file():
				arq.append(entry.name)
				sys.stdout.write('|')
				for pos in range(self.posicao):
					sys.stdout.write('-')
				print(bcolors.ARQUIVO + entry.name + "    " + diretorioAtual + bcolors.ENDC)
			if not entry.name.startswith('.') and entry.is_dir():
				dir.append(entry.name)

		for novoDestino in dir:
			sys.stdout.write('|')
			for pos in range(self.posicao):
				sys.stdout.write('-')
			print(bcolors.DIRETORIO + novoDestino + "    " + diretorioAtual + '/' +  novoDestino + bcolors.ENDC)
			var = SubDiretorio(diretorioOrigem=diretorioAtual, diretorioDestino=novoDestino, posicao=self.posicao+1)
			del var
		
		os.chdir(self.diretorioOrigem)

		return dir

	def acessar(self, diretorio):
		try:
			os.chdir(diretorio)
		except NotADirectoryError:
			#print('Erro: O caminho passado não é referente a um diretorio')
			return False
		except FileNotFoundError:
			#print('Erro: Arquivo não encontrado')
			return False
		except PermissionError:
			#print('Erro: Não é permitido acessar o arquivo')
			return False
		except OSError:
			#print('Erro: Erro desconhecido')
			return False
		finally:
			return True


def main():
	#argv[1] = diretorio em que o script fara a varredura
	#Exemplo: python gerenciamentodedados.py ../../diretorio
	#Irá fazer a varredura dois diretórios atrás

	try:
		SubDiretorio(diretorioDestino=sys.argv[1])
		#var.acessar()
	except Exception as e:
		print(e)
		raise
	finally:
		pass
	
	

if __name__ == "__main__":
	main()
