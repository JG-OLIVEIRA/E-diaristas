<p align="center">
   <img src="./.github/logo.svg" alt="e-diaristas" width="280"/>
</p>

# Descrição

Projeto realizado durante a semana multi-stack da [TreinaWeb](https://github.com/treinaweb). Tanto o back quanto frontend foram desenvolvido durante esse workshop. É possível realizar o CRUD de diaristas com o framework Django e visualizá-las no front com a biblioteca React.

## Instalação

Primeiro, você precisa clonar o repositório na sua maquina

```bash
git clone https://github.com/JG-OLIVEIRA/ediaristas.git
```

Antes da próxima etapa, verifique se você possui o pacote [NPM](https://www.npmjs.com/), o software [NODE](https://nodejs.org/en/) e o [Python](https://www.python.org/downloads/) instalado na sua máquina.

Agora vá até a raiz do projeto e abra dois terminais para rodar o back e o frontend juntos.

## Rodando o backend

Navegue até a pasta backend e execute.

```bash
python manage.py runserver
```

Para manipular o banco de dados, acesse http://127.0.0.1:8000/web/listar_diaristas.

## Rodando o frontend

Navegue até a pasta frontend e instale os pacotes npm.

```bash
npm install
```

Finalmente, ainda no mesmo diretório, rode o seguinte comando:

```bash
npm run dev
```

Acesse http://localhost:3000 para ver o resultado.

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
