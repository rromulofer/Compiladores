def analisa_sintaxe(cadeia):
  """
  Analisa a sintaxe de uma expressão condicional usando um analisador
  recursivo descendente.

  Args:
    cadeia: A expressão condicional a ser analisada.

  Returns:
    True se a expressão é sintaticamente correta, False caso contrário.
  """

  pilha = []
  for caractere in cadeia:
    if caractere in ["(", ")", ",", "=", ">", "<", ">=", "<=", "==", "!="]:
      operador = caractere
      if not pilha:
        return False
      if pilha[-1] != operador:
        return False
      pilha.pop()
    else:
      if caractere.isalpha():
        pilha.append("IDENT")
      elif caractere.isdigit():
        pilha.append("INTCONST")
      elif caractere in [".", "e"]:
        pilha.append("REALCONST")
      else:
        return False

  if len(pilha) != 1:
    return False

  return pilha[0] == "IDENT"


def analisa_funcao(cadeia):
  """
  Analisa a sintaxe de uma função usando um analisador
  recursivo descendente.

  Args:
    cadeia: A função a ser analisada.

  Returns:
    True se a função é sintaticamente correta, False caso contrário.
  """

  pilha = []
  for caractere in cadeia:
    if caractere in ["(", ")", "="]:
      operador = caractere
      if not pilha:
        return False
      if pilha[-1] != operador:
        return False
      pilha.pop()
    else:
      if caractere.isalpha():
        pilha.append("IDENT")
      elif caractere.isdigit():
        pilha.append("INTCONST")
      elif caractere in [".", "e"]:
        pilha.append("REALCONST")
      elif caractere == "(":
        pilha.append("(", "IDENT)")
      elif caractere == ")":
        pilha.pop()

  if len(pilha) != 1:
    return False

  return pilha[0] == "IDENT"


def main():
  cadeia = "funcao(x, y) = if x > 0 then 1 else 0"
  if analisa_sintaxe(cadeia):
    print("A expressão condicional é sintaticamente correta.")
  else:
    print("A expressão condicional é sintaticamente incorreta.")

  cadeia = "funcao(x) = if x > 0 then 1 else 0"
  if analisa_funcao(cadeia):
    print("A função é sintaticamente correta.")
  else:
    print("A função é sintaticamente incorreta.")


if __name__ == "__main__":
  main()
