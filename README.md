<p align="center">
   <img src="./.github/logo.svg" alt="e-diaristas" width="280"/>
</p>

<p align="center">
   <a href="https://www.linkedin.com/in/jorge-gon%C3%A7alves-de-oliveira-7570771a2/">
      <img alt="Jorge Oliveira" src="https://img.shields.io/badge/-Jorge Oliveira-4e5acf?style=flat&logo=Linkedin&logoColor=white" />
   </a>
 <img alt="Repository size" src="https://img.shields.io/github/repo-size/JG-OLIVEIRA/ediaristas?color=4e5acf">

  <a aria-label="Last Commit" href="https://github.com/JG-OLIVEIRA/ediaristas/commits/master">
    <img alt="Last commit on GitHub" src="https://img.shields.io/github/last-commit/JG-OLIVEIRA/moveit?color=4e5acf">
  </a>
  <a href="https://github.com/JG-OLIVEIRA/ediaristascommits/master">
    <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/JG-OLIVEIRA/ediaristas?color=4e5acf">
  </a>
  <img alt="License" src="https://img.shields.io/badge/license-MIT-4e5acf">
</p>

# Descrição

Projeto realizado durante a semana multi-stack da [TreinaWeb](https://github.com/treinaweb). Tanto o back quanto frontend foram desenvolvido durante esse workshop. É possível realizar o CRUD de diaristas com o framework Django e visualizá-las no front com a biblioteca React.

<img src="./.github/Captura%20de%20Tela%20(40).png">
<img src="./.github/Captura%20de%20Tela%20(41).png">

## Instalação

```bash
# Primeiro, você precisa clonar o repositório na sua maquina

$ git clone https://github.com/JG-OLIVEIRA/ediaristas.git
```

Antes da próxima etapa, verifique se você possui o pacote [NPM](https://www.npmjs.com/), o software [NODE](https://nodejs.org/en/) e o [Python](https://www.python.org/downloads/) instalado na sua máquina.

```bash
# Agora vá até a raiz do projeto e abra dois terminais para rodar o back e o frontend juntos.
```

Navegue até a pasta backend e execute.

```bash
$ cd backend
\backend\ $ python manage.py runserver
```

Navegue até a pasta frontend e instale os pacotes npm.

```bash
$ cd frontend
\frontend\ $ npm install
```

Finalmente, ainda no mesmo diretório, rode o seguinte comando:

```bash
$ npm run dev
```

Acesse http://localhost:3000 para ver o resultado.

Para manipular o banco de dados, acesse http://127.0.0.1:8000/web/listar_diaristas.

## Tecnologias

- [NextJS](https://github.com/vercel/next.js/)
- [React](https://reactjs.org/)
- [Typescript](https://www.typescriptlang.org/)
- [Axios](https://github.com/axios/axios)
- [Python](https://www.python.org/downloads/)
- [Django](https://www.djangoproject.com/)

<div align="center">
  <sub>O <strong>E-diaristas</strong> foi desenvolvido com ❤︎ pelo
    <a href="https://github.com/JG-OLIVEIRA">Jorge Oliveira</a>
  </sub>
</div>

## Licença

Este projeto está sob a licença [MIT](./LICENSE).
