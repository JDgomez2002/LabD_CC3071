
import pickle
import time
import simulators.Scanner as scanner
def ws():
	print('WHITESPACE')

def id():
	print('ID')

def number():
	print('NUMBER')

def IF():
	print('IF')

def THEN():
	print('THEN')

def ELSE():
	print('ELSE')

def plus():
	print('PLUS')

def hyphen():
	print('MINUS')

def asterisk():
	print('TIMES')

def slash():
	print('DIV')

def open_parenthesis():
	print('LPAREN')

def close_parenthesis():
	print('RPAREN')


def readYalexFile(file):
  with open(file, 'r') as file:
    data = file.read()
  return data

def main():
  print("scan.py: main()")

  archivo = "program.txt"

  # Leer .txt
  data = readYalexFile(archivo)

  DFAMin = {}
  # Load the data
  with open("result/minDFA.pickle", "rb") as f:
    DFAMin = pickle.load(f)

  print("Returns: ", DFAMin['returns'])

  # # Remove leading spaces from each line in the string
  # code = '\n'.join(line.lstrip() for line in code.split('\n'))

  startTime = time.time()

  readString(data, DFAMin)

  totalTime = time.time() - startTime

  print(f"\nTotal time: {round(totalTime, 3)}s\n")

def readString(data, DFAMin):
  i = 0
  contador = 0

  lengthData = len(data)

  while i < lengthData:
    print("\ni: " + str(i))
    num, valores, temp, error = scanner.exec(DFAMin["transitions"], DFAMin["start_states"], DFAMin["returns"], data, i)
    if error:
      print(f"Valor no reconocido: '{temp}'")
      i += 1
      print("m: " + str(i))
      continue

    print("m: " + str(num))
    print("Valor: " + temp)
    print("Command: " + valores)
    print("Ejecución: ")
    try:
      exec(valores)
    except:
      print("Error al momento de ejecutar el comando")
    contador += 1
    i = num
    continue