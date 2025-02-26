# 📌 Projeto CRUD Usuário  

## 📖 Descrição  
Este é um projeto de gerenciamento de usuários desenvolvido com **Flask (Python)** e **MySQL**. Ele permite cadastro, login, edição de perfil, recuperação de senha e exclusão de conta via **API RESTful**, garantindo segurança por meio de **criptografia de senhas** e autenticação baseada em sessões.  

## 🚀 Funcionalidades  
✔ Cadastro de usuário (nome, e-mail e senha criptografada)  
✔ Login e autenticação via sessão  
✔ Edição de perfil (nome e e-mail)  
✔ Recuperação de senha por e-mail  
✔ Exclusão de conta  

## 📋 Requisitos Não Funcionais  
✅ O sistema deve ser implementado como uma **API RESTful**  
✅ A comunicação entre cliente e servidor deve ser feita em **JSON**  
✅ As senhas dos usuários devem ser criptografadas utilizando **bcrypt**  
✅ A aplicação deve ser capaz de **enviar e-mails** para recuperação de senha  
✅ A autenticação deve ser feita por **sessões baseadas no user_id**  

## 📂 Estrutura do Banco de Dados  
```sql
CREATE DATABASE user_system;
USE user_system;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    password VARCHAR(255)
);
```

## 🔗 Endpoints da API  
- **`POST /api/register`** → Registro de usuário  
- **`POST /api/login`** → Login e criação de sessão  
- **`GET /api/profile`** → Retorna dados do perfil  
- **`PUT /api/profile`** → Atualiza nome e e-mail  
- **`POST /api/reset_password`** → Solicita recuperação de senha  
- **`POST /api/confirm_reset_password`** → Confirma nova senha  
- **`DELETE /api/delete_account`** → Exclui a conta do usuário  

## 🔄 Fluxo de Trabalho do Sistema  
1. **Registro de Usuário**  
   - O usuário envia uma solicitação `POST /api/register` com nome, e-mail e senha.  
   - O sistema verifica se o e-mail já está cadastrado.  
   - Caso não esteja, a senha é criptografada e os dados são armazenados no banco.  

2. **Login**  
   - O usuário envia uma solicitação `POST /api/login` com e-mail e senha.  
   - O sistema valida as credenciais e cria uma sessão.  

3. **Edição de Perfil**  
   - O usuário pode atualizar seu nome e e-mail via `PUT /api/profile`.  
   - A senha não pode ser alterada diretamente, apenas por recuperação.  

4. **Recuperação de Senha**  
   - O usuário solicita um código via `POST /api/reset_password`.  
   - O sistema envia um código temporário por e-mail.  
   - O usuário usa o código para definir uma nova senha em `POST /api/confirm_reset_password`.  

5. **Exclusão de Conta**  
   - O usuário solicita a exclusão via `DELETE /api/delete_account`.  
   - O sistema remove os dados do usuário permanentemente.  

## 🚀 Como Executar o Projeto  
1. Clone o repositório:  
   ```bash
   git clone https://github.com/seu-usuario/projeto-crud-usuario.git
   ```
2. Instale as dependências:  
   ```bash
   pip install -r requirements.txt
   ```
3. Configure o banco de dados MySQL e ajuste as credenciais no código.  
4. Execute a aplicação:  
   ```bash
   python app.py
   ```
5. Acesse os endpoints via **Postman** ou outro cliente REST.  

## 🛠 Tecnologias Utilizadas  
- **Backend**: Flask (Python)  
- **Banco de Dados**: MySQL  
- **Criptografia**: Flask-Bcrypt  
- **Envio de E-mail**: Flask-Mail (SMTP)  
- **Autenticação**: Flask Sessions  
