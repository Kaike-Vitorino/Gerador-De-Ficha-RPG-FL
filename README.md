# Forbidden Lands Character Generator

--- 
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-092E20?style=for-the-badge&logo=flask&logoColor=white)
![CSS](https://img.shields.io/badge/CSS-0072C6?style=for-the-badge&logo=css3&logoColor=white)
![HTML](https://img.shields.io/badge/HTML-E34237?style=for-the-badge&logo=html5&logoColor=white)
![Cover](https://raw.githubusercontent.com/Kaike-Vitorino/Gerador-De-Ficha-RPG-FL/main/Artes_Ficha_Livro/Artes_Front/FL%20-%20Generator%20-%20Background_Inicial.png)

## Por que Pensei Neste Projeto

No sistema amplamente conhecido de RPG "Forbidden Lands", a criação de uma ficha de personagem é essencial para começar o jogo. No entanto, isso requer que todos os jogadores e o mestre leiam os dois livros da franquia, o "Forbidden Lands Quickstart" e o "Forbidden Lands Master", totalizando mais de 400 páginas de leitura e estudo. Um jogador levaria pelo menos uma semana para ler e estudar todo o material necessário para o sistema, e mais 2 ou 3 horas para criar uma ficha de personagem e iniciar a jogatina. Considerando que geralmente são necessários 5 jogadores para jogar o jogo, isso pode atrasar significativamente o início do jogo para todos terem suas fichas prontas.

Diante desse cenário, decidi desenvolver um programa que é capaz de gerar fichas aleatórias que estejam em conformidade com as rigorosas regras desse sistema de RPG. Isso permitirá que você tenha uma ficha totalmente equilibrada em questão de segundos, economizando dias no processo de iniciar o jogo com seus amigos.

Espero que este programa torne a experiência de jogar "Forbidden Lands" mais acessível e divertida para todos os entusiastas de RPG. Acreditamos que ele pode economizar tempo e eliminar as barreiras iniciais que muitos jogadores enfrentam ao entrar nesse mundo incrível de aventuras.

**Deve-se lembrar de que o projeto foi concebido, na verdade, não para ser algo muito útil, mas sim para aprimorar minhas habilidades, colocando-as em prática, explorando e testando novas tecnologias para expandir meu conhecimento. Este programa, de fato, não é muito útil para pessoas iniciantes que** **querem jogar esse FL, até porque saber as regras do jogo é imprescindível para a jogatina, sem contar que criar uma ficha do zero sempre será mais interessante. Isso aqui pode ser útil para fazer one-shots do sistema em encontros entre amigos, viagens, etc.**

--- 
## Descrição do Projeto

O Forbidden Lands Character Generator é uma ferramenta projetada para simplificar a criação de fichas de personagem no sistema "Forbidden Lands". Este software foi desenvolvido com o intuito de facilitar o processo de início do jogo, economizando tempo e esforço.

### Descrição das etapas envolvidas na criação deste programa.

- **Definição de Classes, Raças e Skills:** O programa, de forma aleatória, escolhe as classes, raças e habilidades do seu personagem, assegurando um equilíbrio conforme especificado pelas regras e diretrizes do sistema de RPG.

- **Geração de Todas as Outras Informações Necessárias:** Calcula e gera uma ampla gama de informações, incluindo níveis de habilidades, pontos de experiência, talentos e perícias, mantendo a conformidade com as rigorosas regras do "Forbidden Lands".

- **Criação da Ficha em Formato de Texto:** O programa organiza as informações aleatórias em uma ficha de personagem em formato de texto.

- **Confecção da Ficha de Fato:** Com a ficha pronta, o programa preenche todos os campos correspondentes e a disponibiliza para visualização imediata e, se desejado, para salvar.

- **Interface do Usuário:** interface de usuário simples.

---

## Nomenclatura e Uso de Constantes


Neste projeto, segui uma convenção de nomenclatura para facilitar a organização e compreensão do código. Aqui está um resumo da nomenclatura utilizada:

### Arquivos e Diretórios:

- **DATA_**: Prefixo utilizado para arquivos que retêm informações e dados utilizados pelo programa. Por exemplo, `DATA_racas`, `DATA_classes`, entre outros. Esses arquivos geralmente contêm estruturas de dados como dicionários, listas ou mapas.

- **FUNCOES_**: Prefixo utilizado para arquivos que contêm funções lógicas utilizadas pelo programa. Por exemplo, `FUNCOES_geral`, `FUNCOES_conjunta_main`, entre outros. Esses arquivos são responsáveis por obter e manipular dados de acordo com a lógica do programa.

- **FICHA_**: Prefixo utilizado para arquivos relacionados à geração e edição de fichas de personagens. Por exemplo, `FICHA_funcoes`, `FICHA_coordenadas`, entre outros. Esses arquivos geralmente são responsáveis por gerar a representação visual das fichas de personagens com base nos dados obtidos pelo programa.

### Variáveis, Mapas e Listas:

Variáveis, mapas e listas que são consideradas constantes ou imutáveis são nomeadas em MAIÚSCULAS.
```python
CONSTANTE_EXEMPLO = "valor_constante"
MAPA_EXEMPLO = {1: "a", 2: "b"}
LISTA_EXEMPLO = ["item1", "item2", "item3"]
```

O uso de letras maiúsculas ajuda a identificar rapidamente quais variáveis são consideradas constantes e não serão modificadas durante a execução do programa.

Ao seguir essa nomenclatura e convenção, espero tornar o código mais legível e organizado.

--- 

## **Como Rodar o Projeto**

Para executar este projeto em sua máquina local, siga os passos abaixo ou o tutorial em video:

[Tutorial em video](https://www.youtube.com/watch?v=f51sToKAaec)

1. **Clone o Repositório:**
   ```bash
   git clone https://github.com/Kaike-Vitorino/Gerador-De-Ficha-RPG-FL.git
   ```

2. **Navegue até o Diretório do Projeto:**
   ```bash
   cd Gerador-De-Ficha-RPG-FL
   ```

3. **Navegue até o Diretório do Flask:**
   ```bash
   cd Flask-WebApp
   ```

4. **Instale as Dependências Necessárias:**
   ```bash
   pip install --upgrade -r requirements.txt
   ```

5. **Inicie o Servidor Flask:**
   ```bash
   python app.py
   ```

6. **Visualize o Projeto no Navegador:**
   - Após a inicialização, acesse o projeto através do link fornecido no terminal, por exemplo:
     ```plaintext
     * Running on http://127.0.0.1:5000
     ```
     - Clique no link, e seu navegador abrirá, exibindo a interface do projeto.
   - Para gerar uma ficha, insira o número desejado de XP no campo apropriado e clique no botão "Gerar Ficha".

   *Essa interação é ilustrada no Video demonstração abaixo, proporcionando uma visão prática do funcionamento do projeto.
    Clique no texto em destaque ou na imagem:

   [Video demonstração do programa abaixo.](https://www.youtube.com/watch?v=uZCNOTq5j4k)

   [![Miniatura do Vídeo](https://img.youtube.com/vi/uZCNOTq5j4k/maxresdefault.jpg)](https://www.youtube.com/watch?v=uZCNOTq5j4k)

---  
## Licença

Este projeto está sob a Licença Pública Geral GNU Versão 3 - veja o arquivo [LICENSE](LICENSE.md) para detalhes.

--- 