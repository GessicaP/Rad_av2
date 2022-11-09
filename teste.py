import sqlite3

conexao = sqlite3.connect("myDB.db")
cursor = conexao.cursor()
try:
  bd_hospital = """
    CREATE TABLE hospital(
      cnpj VARCHAR(11) PRIMARY KEY NOT NULL,
      nome VARCHAR(20) NOT NULL,
      rua VARCHAR(50) NOT NULL,
      bairro VARCHAR(20) NOT NULL,
      cidade VARCHAR(20) NOT NULL,
      cep VARCHAR(8) NOT NULL,
      telefone VARCHAR(10) NOT NULL
    )
  """

  bd_medico = """
    CREATE TABLE medico(
      crm VARCHAR(10) PRIMARY KEY NOT NULL,
      cpf VARCHAR(11) NOT NULL,
      nome VARCHAR(50) NOT NULL,
      rua VARCHAR(50) NOT NULL,
      bairro VARCHAR(20) NOT NULL,
      cidade VARCHAR(20) NOT NULL,
      cep VARCHAR(8) NOT NULL
    )
  """ 

  bd_especialidade = """
    CREATE TABLE especialidade(
      cod INT(4) PRIMARY KEY NOT NULL,
      especialidades VARCHAR(50) NOT NULL,
      documento VARCHAR(10),      
      FOREIGN KEY(documento) REFERENCES medico(crm)
      
      )
  """

  bd_telefone = """
    CREATE TABLE telefone(
      cod INT(4) PRIMARY KEY NOT NULL,
      telefone VARCHAR(10) NOT NULL,      
      documento VARCHAR(10),
      FOREIGN KEY(documento) REFERENCES medico(crm)
      
    )
  """

  bd_enfermeira = """
    CREATE TABLE enfermeira(
      coren VARCHAR(10) PRIMARY KEY NOT NULL,
      cpf VARCHAR(11) NOT NULL,
      nome VARCHAR(50) NOT NULL,
      rua VARCHAR(50) NOT NULL,
      bairro VARCHAR(20) NOT NULL,
      cidade VARCHAR(20) NOT NULL,
      cep VARCHAR(8) NOT NULL
    )
  """

  bd_paciente = """
    CREATE TABLE paciente(
      cpf VARCHAR(11) PRIMARY KEY NOT NULL,
      rg VARCHAR(10) NOT NULL,
      nome VARCHAR(50) NOT NULL,
      rua VARCHAR(50) NOT NULL,
      bairro VARCHAR(20) NOT NULL,
      cidade VARCHAR(20) NOT NULL,
      cep VARCHAR(8) NOT NULL
    )
  """

  bd_tratamento = """
    CREATE TABLE tratamento(
      cpf VARCHAR(11) NOT NULL,
      crm VARCHAR(10) NOT NULL,
      cid VARCHAR(50) PRIMARY KEY NOT NULL,
      data DATE
      )
  """  
  
  db_corpo_clinico_hospital = """
    CREATE TABLE hospital_profissional(
      id LONG NOT NULL PRIMARY KEY,
      doc_profissional VARCHAR(10) NOT NULL,
      doc_hospital VARCHAR(11) NOT NULL,
      Foreign KEY(doc_profissional)
      REFERENCES medico(crm),
      Foreign KEY(doc_profissional)
      REFERENCES enfermeira(coren)
      )
    """

  db_medico_paciente = """
   CREATE TABLE medico_paciente(
     id LONG NOT NULL PRIMARY KEY,
     doc_paciente VARCHAR(11),
     doc_medico VARCHAR(10),
     FOREIGN KEY(doc_paciente) REFERENCES paciente(cpf),
     FOREIGN KEY(doc_medico) REFERENCES medico(crm)
    )
   """
  print("Criado com sucesso")
  columns = {bd_hospital, bd_medico, bd_especialidade, bd_telefone,
  bd_enfermeira, bd_paciente, bd_tratamento, db_corpo_clinico_hospital,db_medico_paciente} 
  if FileExistsError(columns):
    print("Já existe")
  else:
    cursor.execute(bd_hospital)
    cursor.execute(bd_medico)
    cursor.execute(bd_especialidade)
    cursor.execute(bd_telefone)
    cursor.execute(bd_enfermeira)
    cursor.execute(bd_paciente)
    cursor.execute(bd_tratamento)
    cursor.execute(db_corpo_clinico_hospital)
    cursor.execute(db_medico_paciente)

  menu = """

    1- CADASTRAR
    1.1- HOSPITAL
    1.2- MÉDICO
    1.3- ESPECIALIDADE
    1.4- TELEFONE
    1.5- ENFERMEIRA
    1.6- PECIENTE
    1.7- TRATAMENTO
    2- PESQUISAR
    2.1- HOSPITAL
    2.2- MÉDICO
    2.3- ESPECIALIDADE
    2.4- TELEFONE
    2.5- ENFERMEIRA
    2.6- PECIENTE
    2.7- TRATAMENTO
    3- EXCLUIR
    3.1- HOSPITAL
    3.2- MÉDICO
    3.3- ESPECIALIDADE
    3.4- TELEFONE
    3.5- ENFERMEIRA
    3.6- PECIENTE
    3.7- TRATAMENTO
    4- ATUALIZAR
    4.1- HOSPITAL
    4.2- MÉDICO
    4.3- ESPECIALIDADE
    4.4- TELEFONE
    4.5- ENFERMEIRA
    4.6- PECIENTE
    4.7- TRATAMENTO
    5- Sair

  """
  opcao = True
  while(opcao):
    print(menu)
    n = input("Digite a opção que deseja: ")
    if(n == "5"):
      opcao = False
      break
    


  
  
  cursor.execute( """
    INSERT INTO hospital(cnpj, nome, rua, bairro, cidade, cep, telefone) 
    values(?,?,?,?,?,?,?)
  """,(h_cnpj, h_nome, h_rua, h_bairro, h_cidade, h_cep, h_telefone))

  

  cursor.execute("""
    INSERT INTO paciente(cpf, rg, nome, rua, bairro, cidade, cep)
    VALUES(?,?,?,?,?,?,?)
  """,(p_cpf, p_rg, p_nome, p_rua, p_bairro, p_cidade, p_cep))

 
  cursor.execute("""
    INSERT INTO medico(crm, cpf, nome, rua, bairro, cidade, cep)
    VALUES(?,?,?,?,?,?,?)
  """,(m_crm,m_cpf, m_nome, m_rua, m_bairro, m_cidade, m_cep))

  query_hospital = """SELECT * FROM hospital"""
  query_paciente = """SELECT * FROM paciente"""
  query_medico = """SELECT * FROM medico"""

  cursor.execute(query_hospital)
  cursor.execute(query_paciente)
  cursor.execute(query_medico)

  




  conexao.commit() 


except ConnectionError as e:
    print("Erro ao conectar ao banco: ", e)

finally:
  cursor.close()
  conexao.close()