# Imersão Alura Gemini: Meu Aprendizado em Chatbots com IA

* **IA:**
    * Este repositório documenta minha jornada no curso "Imersão Alura Gemini", onde mergulhei no mundo dos chatbots com inteligência artificial, utilizando a API Gemini e o Google Colab.

* **Heitor:**
    * *Aula 1:*
        * Essa é uma documentação simples do meu histórico de aprendizado com IAs em geral, especialmente LLMs;
        * Vou evitar fazer alterações retroativas justamente para preservar a sensação de evolução de aprendizado que tive ~~espero ter~~ ao longo do curso; 
        * Vale ressaltar que até a primeira aula nunca havia testado nenhuma LLM, nem mesmo o famoso Chatgpt.
        * Foi gerado esse markdown inteiro (pelo menos a parte **IA**) na primeira aula

## Aulas

### Aula 1: Introdução ao Gemini e Google Colab 

* **IA:**
    * *Resumo:* 
    Esta aula me apresentou à linguagem Gemini e suas capacidades, além de explorar o ambiente Google Colab para desenvolvimento do chatbot. 
    * *Links:*
        * [Documentação Gemini](https://ai.google.dev/gemini-api/docs)
        * [Introdução ao Google Colab](https://colab.research.google.com/notebooks/intro.ipynb)
        
* **Heitor:**
    * *Resumo:*
        * Como o próprio Gemini diz, é uma aula bem básica;
        * Basicamente utilizei só o AiStudio, achei mais agradável;
        * Os prompts princiapis estão salvos na pasta da aula-1;
        * Usei o AiStudio para criar um template bem básico para um site-cv genérico. Imagino que pudesse melhorar bem o template colocando mais uma sequência de prompts, mas fiquei satisfeito com o resultado básico e parei. Nas próximas aulas, devo ter orientações mais claras de como melhorar a qualidade dos prompts;
        * Aprveitei para fazer esse mesmo *Readme.md* com o AiStudio.

### Aula 2: Criando um Prompt Eficiente

* **IA:**
    * *Resumo:* 
    Aprendi a criar prompts eficazes para orientar o Gemini e obter respostas relevantes do chatbot, explorando diferentes tipos de prompts e suas aplicações. 
        
* **Heitor:**
    * *Resumo:*
        * Basicamente uma geral sobre como fazer prompts;
        * As técnicas levam nomes intuitívos, e duas se destacam: zero-shot e few-shot. São adaptações da nomenclatura padrão de ML, mas se diferem porque não tratam do treinamento da máquina em si. A máquina é capaz de absorver alguma informação nova (contexto), mas não é treinada do zero:
            * **Zero-shot**: se resume a dar um comando sem contexto algum;
            * **Few-shot**: como o nome sugere, é a técnica de prover alguma informação prévia para direcionar a formatação da resposta da máquina;
        * Há também o conceito de enriquecer os prompts. Segue a lógica inversa de busca por palavra-chave: quanto mais plavras e frases forem usadas, melhor o direcionamento da resposta. Não ficou exatamente claro se essa abordagem seria chamada de few-shot, mas acredito que sim.
        * Ainda um pouco mais sobre o few-shot, ele pode ser feito tanto de forma contínua quanto blocada. Isto é, pode ser um ou alguns texto de contexto em sequência ou seguir um modelo de input/ouput (pergunta/resposta, resumo/título, etc...)


### Aula 3: Conversando com o Chatbot

* **IA:**
    * *Resumo:*  
    Coloquei meu chatbot em ação, interagindo e avaliando suas respostas. Refinei o prompt para melhorar a qualidade das conversas.
        
* **Heitor:**
    * Além das versões do programa e comandos básicos (exportação, uso do API de python, etc..), existem três parâmetros principais: TK, TP, e T
    * Top K (TK):
        * Primeira restrição de conxeções formadas para escolha da próxima palavra
        * Representa o subconjunto completamente conectado a um dado nodo (palavra)
    * Top P (TP):
        * Subjconjunto de TK;
        * Recebe o parâmetro p_tot;
        * É composto por uma subcoleção de palavras rankeadas em probilidade;
        * Agrupa-se N palavras | Sum(p(palavra)) <= p_tot;
    * Temperatura (T):
        * Flutuação aleatória (agitação térmica) da vacância de escolha E de TP;
        * T = 0 => E(TP) = max(p_TP(palavra));
        * T = 1 => E(TP) = rand_uni(palavra)


### Aula 4: Personalizando o Chatbot

* **IA:**
    * *Resumo:* 
    Explorei maneiras de personalizar meu chatbot, definindo personalidade, tom de voz e áreas de conhecimento.
        
* **Heitor:**
    * Uma introdução sobre python/notebooks e o uso da google-generativeai;
    * Documentação segue um padrão bem diferente das outras libs de python [link](https://ai.google.dev/gemini-api/docs/get-started/python?hl=pt-br);
    * Foi feito um chat-bot em aula. É simplesmente um while com input e print, mas funciona legalzinho igual a versão web;

### Chat-bot

* **Your turn:** Me indique 2 livros sobre Machine learning, 1 focado em LLM e outro para identificação de padrões de imagens
* **Answer**: Focado em LLM (Large Language Models):

    * **Natural Language Processing with Transformers: A Guide for Practitioners** por Lewis Tunstall, Asli Celikyilmaz, Doug Burger
    * **Deep Learning for Natural Language Processing** por Jason Brownlee

    * Para identificação de padrões de imagens:

    * **Computer Vision with OpenCV 4 and Deep Learning: A Practical Guide** por Adrian Rosebrock
    * **Deep Learning for Computer Vision: A Hands-on Guide** por Adrian Rosebrock

### Aula 5: Integrando o Chatbot a Outras Plataformas

* **IA:**
    * *Resumo:* 
    Aprendi a integrar o chatbot a outras plataformas, como sites e aplicativos de mensagens, para torná-lo acessível a um público maior. 
        
* **Heitor:**
    * [Embeding](https://ai.google.dev/gemini-api/docs/embeddings?hl=pt-br) é um método de represnetação N-dimensional (aparentemente 768 dimensional)
    * Utilizando o embeding, é possível fazer operações vetoriais padrão;
    * Não necessariamente todas as oprações farão sentido;
    * Estou curioso para entender o que seria um campo vetorial nesse espaço;
    * É muito útil para formar respostas a partir de uma base de dados buscando por similaridades (projeções) no espaço N-dimensional

## Contato e Links Úteis

* [**Meu LinkedIn para contato**](https://www.linkedin.com/in/hmynssen/) 
* [**Laboratório metaBIO**](https://metabio.netlify.app)