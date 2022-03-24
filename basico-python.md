# Básico do Python

Python é uma linguage de programação de propósito geral.

Um de suas principais características é a facilidade de escrita e leitura do código. Python engaja todos os tipos de desenvolvedores, experientes ou não, sendo atualmente a principal porta de entrada para recém chegados no mundo da programação.

Possui as seguintes características:

* **Alto Nível**: [Clique aqui para saber mais.](https://pt.wikipedia.org/wiki/Linguagem_de_programa%C3%A7%C3%A3o_de_alto_n%C3%ADvel)
* **Interpretada de Script**: 
* **Tipagem Dinâmica e Forte**:
* **Multiparadigma**: 
  * **Imperativa**: 
  * **Funcional**: 
  * **Procedural**: 
  * **Orientada à Objetos**: 
 
## Linha de Comando

Como o Python é uma linguagem `interpreta de script` é possível executar comandos Python diretamente em uma linha de comando, sem necessidae de nenhuma outra interface ou processo de `build`  ou ` compilação`.

Para acesasr o `shell` do `Python` basta abrir um `cmd` ou `terminal` e digitar o comando:

``` shell
python
``` 

Será aberto o `shell` do Python conforme imagem abaixo:

![Python Shell](./images/python-shell.png)

Na imagem acima é possível visualizar o `shell` do Python e neles excutamos o comando `print('Ola Mundo')` para exemplificar a utilização deste.

## Variáveis

> _Variável é um `espaço` reservado na memória do computador capaz de armazenar um determinado `valor`._

Este `valor` pode ser algo discreto como um `nome (Eduardo)` ou um `número 36`. Estes valores são descritos como [tipos primitivos](https://en.wikipedia.org/wiki/Primitive_data_type), que são _"um conjunto de tipos de dados básicos a partir dos quais todos os outros tipos de dados são construídos"_.

Uma `variável` também pode armazenar `objetos complexos (uma classe que representa uma pessoa)` ou até mesmo `funções (métodos executáveis da linguagem de programação)`. Estes valores são descritos como [tipos compostos ou derivados](https://en.wikipedia.org/wiki/Composite_data_type), que é _"qualquer tipo de dados que pode ser construído em um programa usando os tipos de dados primitivos da linguagem de programação"_.

Custome dizer que as `variáveis` dão vida aos programas, pois são através delas que `manipulamos` as informações do `sistema de informações`. Sacou?!

Cada espaço reservado na memória, ou seja, uma variável, está associada a um `nome` que identifica únicamente esta variável no escopo do programa. Não é possível ter duas variáveis com o mesmo nome, dentro do mesmo escopo.

Uma variável, somente existe em `tempo de execuçã`, ou seja, quando o programa está `executando` ou `rodando`.

Existem vários padrões para `nomear` uma variável, e cada linguagem de programação normalmente estabelece um padrão que pode ser seguido pelos desenvolvedores. No caso do Python o padrão mais adotado, segue as seguintes regras:

* Utilizar nomes com letras minúsculas
* Utilizar o caractere `_ (underline)` como separados entre as palavras

Lembrando que Python é `case sensivite`, ou seja, a variável `pessoa` é diferente da varíavel `Pessoa`.

O Python possui um jeito peculiar de criar ou `declarar` uma variável. Diferente de outras linguagens de `tipagem estática`, para declarar uma variável no Python, basta apenas informar o `nome`da variável, `inicializando` ela com algum valor, conforme demonstrado abaixo:

```shell
nome_pessoa = 'Eduardo'
```

Caso a variável ainda não exista em memória o `interpretador` Python irá criá-la. Caso a variável já exista em memória, o valor desta será atualizada.

```shell
print(nome_pessoa)

# Resultado: Eduardo
```

Para verificar o `tipo` de uma variável, basta usar o comando a seguir:

```shell
type(nome_pessoa)

# Resultado: <class 'str'>
```

O Python trata todas as variáveis como um `objeto` em memória. Um `objeto` contém `propriedades` e `métodos` que podem ser `explorados` pelo desenvolvedor.

Para verificar quais `propriedades` e `métodos`um `objeto` possui, basta usar o comando abaixo:

```shell
dir(nome_pessoa)

# Resultado: ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
```
As `propriedades` e `métodos` listados acima, podem ser utilizados pelo desenvedor. Por exemplo:

```shell
print(nome_pessoa.isnumeric())

# Resultado: False
```

## Operadores

Operadores em linguagem de programação são `símbolos` especiais que executam alguma `operação` especial durante a execução do programa, por exemplo:

* **`+`**: Realiza operações de `soma` entre dois objetos/variáveis `numéricas` ou `concatenação` entre das variáveis do tipo `texto`.
* **`-`** Realiza operações de `subtração`.
* **`*`**: Realiza operações de `multiplicação`.
* **`/`**: Realiza operações de `divisão`.
* **`== >= <= > <`**: Realiza operações de `comparação`.
* **`=`**: Realiza operações de `atribuição` de valores para `objetos` e `variáveis`.

Exemplos:

```shell
# atribuição
x = 2
y = 2

# soma
print(x + y) # 4

# subtração
print(x - y) # 0

# multiplicação
print(x * y) # 4

# divisão
print(x / y) $ 1

# comparação de igualdade
print(x == y) # True

# comparação de maior
print(x > y) # False

# comparação de menor
print(x < y) # False

# comparação de maior ou igual
print(x >= y) # True

# comparação de menor ou igual
print(x <= y) # True

```

## Palavras Reservadas

São palavras especiais reservadas e utilizadas pelo interpretador Python para acessar algum comando própria da linguagem. Estas palavras jamais devem ser usadas para `nomear` variáveis.

São elas:

```
and, as, assert, break, class, continue, def, del, elif, else, except, False, finally,
for, from, global, if, import, in, is, lambda, None, nonlocal, not, or, pass, raise,
return, True, try, while, with, yield
```

## Módulos (Modules)

Um `módulo` nada mais é do que um `arquivo` contendo `comandos` do Python, que serão executados pelo seu interpretador. 

Como dito anteriormente, Python é uma linguagem `interpretada` de `script`, ou seja, não existe uma etapa de `compilação` prévia como outras linguagens (C#, por exemplo). 

O código Python é `interpretada` em tempo de execução. O código é `lido` e `executado` de forma sequencial, por isso é chamado de script.

Os programas python são compostos por diversos módulos.

Cada módulo pode conter tanto `instruções executáveis` quanto definições de `funções` e `classes`.

A seguir é exibido um `arquivo (módulo)` python:

```python
# -*- utf-8 -*
# File: matematica.py

import math

def fatorial(x):
	return math.factorial(x)
	
def soma(x, y):
	return x + y
```

Acima é exibido o arquivo `matematica.py` contendo a definição de duas `funções`: `fatorial` e `soma`.

É importante observar que `módulos` Python podem ser reaproveitados, assim o desenvolvedor não precisa re-escrever ou duplicar código.

Para isso, basta realizar a importação de um `módulo` já existente, conforme demonstrado na instrução `import math` do arquivo acima.

Existem diversos `módulos` Python disponíveis. Alguns desses `módulos` são disponibilizados pela própria Python Fondation e já acompanham a instalação padrão do Python. Outros `módulos` são criados pela `comunidade` e distribuídos livremente na web. Além dissp, você pode criar seus próprios `módulos` e importá-los no seu programa Python.

## Pacotes (Packages)

Um `pacote` Python nada mais é do que um `conjunto` de `módulos` Python. Os pacotes servem para deixar o projeto mais `organizado`.

Para criar um `pacote` Python, basta criar um `diretório` contendo um arquivo chamado `__init__.py` dentro dele. Sempre que o `interpretador` Python localizar um arquivo `__init__.py` dentro de uma pasta, este saberá que ali existe um `pacote`.

Assim como os `módulos` um `pacote` Python também pode ser importados. Por exemplo:

```python
from os import path

print(path.isdir('C:\Windows')
```

O código acima, realiza a importação do módulo `path` a partir do pacote `os`.

Caso queria o desenvolvedor também pode importar todo o `pacote`, como demonstrado a seguir:

```python
import os

print(os.path.isdir('C:\Windows')
```

O código acima, importa o pacote `os`. Dessa forma, todos os `módulos` disponíveis no pacote `os` ficarão acessíveis no escopo atual.

Você também pode criar `subpacotes`(`pacotes` dentro de `pacotes`), basta que para cada subpasta exista um arquivo `__init__.py`. Exemplo: 

```
pacoteA
|_ __init__.py
|_ moduloA.py
|_ pacoteB
   |_ __init__.py
   |_ moduloB.py
   |_ pacoteC
      |_ __init__.py
	  |_ moduloC.py
```

## Estruturas de dados


…

## Fluxo de controle

if
loops
indentação 

…

## Funções/Métodos

…


## Bibliotecas

…

## Programação orientada à objetos

### Classes

…

### Propriedades

…

### Métodos

…

### Herança

…


## Referências

* https://pt.wikipedia.org/wiki/Python
* https://www.devmedia.com.br/guia/python/37024
* https://www.devmedia.com.br/python-tutorial-tour-pela-linguagem/40646
* https://www.devmedia.com.br/primeiros-passos-com-o-python/37003
* https://www.devmedia.com.br/como-criar-minha-primeira-classe-em-python/38912
* https://en.wikipedia.org/wiki/Primitive_data_type
* https://en.wikipedia.org/wiki/Composite_data_type
* https://docs.python.org/pt-br/3/tutorial/modules.html
