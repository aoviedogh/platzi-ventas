PASSWORD = "12345"

def password_requerido(func):
  def wrapper():
    password = input("Contraseña: ")

    if (password == PASSWORD):
      return func()
    else:
      print("La contraseña es incorrecta")
  
  return wrapper


@password_requerido
def necesita_password():
  print("La contraseña es correcta")


def upper(func):
  def wrapper(*args, **kwargs):
    resultado = func(*args, **kwargs)

    return resultado.upper()
  
  return wrapper

@upper
def di_mi_nombre(nombre):
  return "Hola {}".format(nombre)


if __name__ == "__main__":
  necesita_password()
  print(di_mi_nombre("Pedro"))