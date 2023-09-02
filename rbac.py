class User:
    def __init__(self, username, role, password):
        self.username = username
        self.role = role
        self.password = password

def access_control():
    print('Controle de acesso')
    print('1 - Acessar a área administrativa')
    print('2 - Acessar a área do gerente')
    print('3 - Acessar a área do membro')
    print('4 - Sair')
    action = input('Digite a ação que deseja executar: ')

    return action

def menu_back():
  action = input('Digite qualquer coisa para voltar ao controle de acesso e 4 para sair do sistema: ')

  if (action in ['1', '2', '3']):
    action = '-1'
  elif action == '4':
    print('Já vai? Bye bye!')

  return action

def actions(action, users, foundPassword):
  if action == '4':
    print('Já vai? Bye bye!')
  elif action == '1':
    if(users[foundPassword].role != 'admin'):
      print('Usuários do cargo {} não tem permissão para entrar na área administrativa'.format(users[foundPassword].role))
      action = -1
    else:
      print('Bem-vindo à área administrativa!')
      action = menu_back()
  elif action == '2':
    if(users[foundPassword].role != 'gerente' and users[foundPassword].role != 'admin'):
      print('Usuários do cargo {} não tem permissão para entrar na área do gerente'.format(users[foundPassword].role))
      action = -1
    else:
      print('Bem-vindo à área do gerente!')
      action = menu_back()
  elif action == '3':
    print('Bem-vindo à área do membro!')
    action = menu_back()
  else:
    print('Ação não encontrada! Tente novamente')

  return action

def username_login(users):
    username = input('Digite o username: ')

    usernames = [user.username for user in users]

    foundUsername = usernames.index(username)

    return foundUsername

def password_login(users, foundUsername):
    password = input('Digite a senha: ')

    passwords = [user.password for user in users]

    foundPassword = passwords.index(password)

    if(foundPassword == foundUsername):
      return foundPassword

    return False

def wrong_password():
  print('Senha incorreta! Tente novamente')
  
  return -1

users = []
user1 = User("gabrielsilva", "admin", "abac14as")
user2 = User("pedrolima", "gerente", "b124aca1")
user3 = User("annalfr", "membro", "c1205acay")
users.append(user1)
users.append(user2)
users.append(user3)

action = -1
while True:
  if action == '4':
    break

  print('Login')

  try:
    foundUsername = username_login(users)
  except ValueError:
    print('Username não encontrado!')
    break

  foundPassword = -1
  while foundPassword == -1:
    try:
      foundPassword = password_login(users, foundUsername)
      if isinstance(foundPassword, bool):
        foundPassword = wrong_password()
    except ValueError:
      foundPassword = wrong_password()

  while action not in ['1', '2', '3', '4']:
    action = access_control()

    action = actions(action, users, foundPassword)
    if action == '4':
      break



