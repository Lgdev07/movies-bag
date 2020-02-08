<h1 align="center">
      <img alt="Fastfeet" title="Fastfeet" src=".github/logo.png" width="300px" />
</h1>

<h3 align="center">
  Movies-Bag API
</h3>

<p align="center">Organize your favourite movies and never lose a good recomendation 🎓</p>

<p align="center">Made with Python-Flask and MongoDB 🚀</p>
<p align="center">Using API Restful, Bcrypt, JWTManager, Flask_Mail and Users Management 🚀</p>

<p align="center">
  <img alt="GitHub language count" src="https://img.shields.io/github/languages/count/Lgdev07/fastfeet-backend?color=%2304D361">

  <a href="https://rocketseat.com.br">
    <img alt="Made by Rocketseat" src="https://img.shields.io/badge/made%20by-Lgdev07-%2304D361">
  </a>

  <img alt="License" src="https://img.shields.io/badge/license-MIT-%2304D361">

  <a href="https://github.com/Rocketseat/bootcamp-gostack-10/stargazers">
    <img alt="Stargazers" src="https://img.shields.io/github/stars/Lgdev07/fastfeet-backend?style=social">
  </a>
</p>

<p align="center">
  <a href="#-instalacao-e-execução">Installation and execution</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-como-contribuir">Available Routes</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-como-contribuir">How to contribute</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
</p>

## 🚀 Installation and execution

1. Clone this repository;
2. Run `pip3 install -r requirements.txt ` to install dependencies;
3. Create a .env file and configure the fields below with your preferences:
4. JWT_SECRET_KEY = random string that will be a secret key </br>
MAIL_SERVER="smtp.gmail.com" (this is for gmail only)</br>
MAIL_PORT=465</br>
MAIL_USE_SSL=True</br>
MAIL_USERNAME = your email</br>
MAIL_PASSWORD = your email password</br>
MONGODB_URL = your mongodb database url</br>
5. Run `python run.py`.
6. Access `http://localhost:3000`.

## 🛣️ Available Routes

- '/api/movies'
- '/api/movies/<id>'
- '/api/auth/signup'
- '/api/auth/login'
- '/api/auth/forgot'
- '/api/auth/reset'

## 🤔 How to contribute

- Fork this repository;
- Create a branch with your feature: `git checkout -b minha-feature`;
- Commit your changes: `git commit -m 'feat: Minha nova feature'`;
- Push to your branch: `git push origin minha-feature`.

After the merge of your pull request is done, you can delete your branch.

---
