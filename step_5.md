# Activer l'IAGen dans notre bot

[<img src="img/Indiana_Jones_and_the_Last_Crusade_Motorcycle_Chase.png"  alt="Indiana Jones and the Last Crusade">](https://www.youtube.com/watch?v=e1KKVy-nki8)

> "The solution presents itself !", Indiana Jones Last Crusade, Steven Spielberg, 1989

<br/>
<u>Objectifs:</u>

- Configurer les paramètres de l'IA générative
- Activer l'IA générative dans Tock Studio
- Interroger le bot


## Sommaire

- [Gen AI / RAG Settings](#gen-ai--rag-settings)
  - [Configuration](#configuration)
    - [LLM Engine](#llm-engine)
      - [Configurer Ollama pour LLM Engine](#configurer-ollama-pour-llm-engine)
      - [Configurer OpenAi pour LLM Engine](#configurer-openai-pour-llm-engine)
      - [Configurer AzureOpenAI pour LLM Engine](#configurer-azureopenai-pour-llm-engine)
    - [Emdedding](#emdedding)
      - [Configurer Ollama pour Emdedding](#configurer-ollama-pour-emdedding)
      - [Configurer OpenAi pour Emdedding](#configurer-openai-pour-emdedding)
      - [Configurer AzureOpenAI pour Emdedding](#configurer-azureopenai-pour-emdedding)
  - [Configuration final et activation](#configuration-final-et-activation)
  

- [Interroger le bot](#interroger-le-bot)


- [Étape suivante](#étape-suivante)


## Gen AI / RAG Settings
## Configuration

Dans le menu de gauche au niveau **Gen AI** > **RAG Settings** (Retrieving augmented Generation) vous allez pouvoir 
choisir les modèles d'IA générative pris en charge par Tock et de configurer un ensemble de critères spécifiques à chaque fournisseur d'IA.
Cette fonctionnalité permettra à TOCK de générer une réponse à une requête de l'utilisateur, sur la base d'un ensemble de documents intégrés dans une base de données vectorielle.

> Pour accéder à cette page il faut bénéficier du rôle **_botUser_**, role que vous avez en étant admin.


### Activation du RAG & Configuration du LLM Engine

Écran d'exemple d'une configuration du RAG avec le LLM Engine (a ne pas suivre):

![RAG - Partie 1](img/gen-ai-settings-rag-llm_ollama.png "Ecran de configuration du RAG - Partie 1")

**RAG activation :**
- L’activation n’est possible qu’une fois que tous les champs marqués d’un * sont remplis.
- Une fois les champs remplis, choisir si oui ou non, le bot doit offrir l’option RAG.

**Un provider IA :** (LLM Engine)

<img src="img/llm-engine.png" alt="llm engine">

- Cette section permet de paramétrer les options liées au modèle IA qui génère la réponse à l’utilisateur.
- Voir la [liste des fournisseurs d'IA](providers/gen-ai-provider-llm-and-embedding.md)

**Température :**

<img src="img/temperature.png" alt="temperature">

- On peut définir une température située entre 0 et 1.
- Celle-ci permet de déterminer le niveau de créativité du Bot dans la réponse apportée à une requête qui lui est envoyée.

**Prompt :**

<img src="img/prompt.png" alt="prompt">

- Le prompt est le script qui détermine la personnalité du Bot, le contexte dans lequel il doit répondre, la façon dont il doit s’adresser à l’utilisateur, les recommandations ou instructions de réponses, les styles et formats de réponses.

### Configurer Ollama pour LLM Engine
<details>
  <summary>Voir la configuration Ollama</summary>

Pour connecter ollama à Tock studio, il vous faut renseigner l’accès à Ollama via cette url d’accès (**BaseUrl**) : http://ollama-server:11434..
Pour le modèle (**Model**), là c’est à vous de renseigner le nom du modèle que vous utilisez dans ce CodeLab (ici nous avons tinyllama). Enfin pour la température, vous pouvez laisser la valeur par défaut à 0.7.

⚠️ Si Ollama est lancé en local depuis votre ordinateur vous devez changer la valeur de base url de défaut par "http://host.docker.internal:11434"

<img src="img/rag-settings-example-ollama.png" alt="rag settings ollama">
</details>


### Configurer OpenAi pour LLM Engine
<details>
  <summary>Voir la configuration OpenAi</summary>

Si vous souhaitez utiliser openAI, vous devez vous inscrire sur la plateforme [OpenAI](https://platform.openai.com/docs/introduction)
pour obtenir une clé d'API. Une fois cela fait rendez-vous à cette page [https://platform.openai.com/api-keys](https://platform.openai.com/api-keys) pour générer votre clé d'API.

Dès que vous avez votre clé d'API, vous pouvez la renseigner dans le champ **API Key** et choisir le model (**Model name**) que vous souhaitez utiliser.
Par exemple vous pourriez avoir ce genre de rendu.

<img src="img/rag-settings-example-openai.png" alt="rag settings  openai">
</details>


### Configurer AzureOpenAI pour LLM Engine
<details>
  <summary>Voir la configuration AzureOpenAI</summary>

Si vous souhaitez utiliser Azure OpenAI, vous devez vous inscrire sur la plateforme
[Azure OpenAI](https://azure.microsoft.com/fr-fr/products/ai-services/openai-service) et d'avoir un compte professionnel  
afin d'avoir une clé d'API.
Une fois cela fait, vous pouvez renseigner votre clé d'API dans le champ **API Key** et choisir le model (**Model name**)
que vous souhaitez utiliser.

<img src="img/rag-settings-example-azure.png" alt="rag settings azure">
</details>

## Emdedding

### Configurer Ollama pour Emdedding

<details>
  <summary>Voir la configuration Ollama</summary>

Pour connecter Ollama à Tock studio sur la partie embedding, il vous faut renseigner l’accès à Ollama via cette url d’accès (**BaseUrl**) : http://ollama-server:11434.
Pour le modèle (**Model**), là c’est à vous de renseigner le nom du modèle que vous utilisez dans ce CodeLab
(ici nous avons **nomic-embed-text**).

⚠️ Si Ollama est lancé en local depuis votre ordinateur vous devez changer la valeur de base url de défaut par "http://host.docker.internal:11434"

<img src="img/embedding-ollama-setting.png" alt="embedding ollama">

Pour le reste de configuration, nous vous invitons à aller directement au chapitre [Configuration final et activation](#configuration-final-et-activation)
</details>



### Configurer OpenAi pour Emdedding
<details>
  <summary>Voir la configuration OpenAi</summary>

Si vous souhaitez utiliser openAI, vous devez vous inscrire sur la plateforme [OpenAI](https://platform.openai.com/docs/introduction)
pour obtenir une clé d'API. Une fois cela fait rendez-vous à cette page [https://platform.openai.com/api-keys](https://platform.openai.com/api-keys)
pour générer votre clé d'API.

Dès que vous avez votre clé d'API, vous pouvez la renseigner dans le champ **API Key** et choisir le model
(**Model name**) actuellement disponible : **text-embedding-ada-002**.
Par exemple vous pourriez avoir ce genre de rendu.

<img src="img/embedding-openai-settings.png" alt="embedding openai">

Pour le reste de configuration, nous vous invitons à aller directement au chapitre [Configuration final et activation](#configuration-final-et-activation)
</details>

### Configurer AzureOpenAI pour Emdedding

<details>
  <summary>Voir la configuration AzureOpenAI</summary>

Si vous souhaitez utiliser Azure OpenAI, vous devez vous inscrire sur la plateforme
[Azure OpenAI](https://azure.microsoft.com/fr-fr/products/ai-services/openai-service) et d'avoir un compte professionnel  
afin d'avoir une clé d'API.
Une fois cela fait, vous pouvez renseigner votre clé d'API dans le champ **API Key** et choisir le model (**Model name**)
que vous souhaitez utiliser.

<img src="img/embedding-azureopenai-settings.png" alt="embedding azure">

Pour le reste de configuration, nous vous invitons à aller directement au chapitre [Configuration final et activation](#configuration-final-et-activation)
</details>


### Configuration final et activation
Cette partie s’attarde sur les intitulés **Indexing session** et **Conversation flow**.

<img src="img/indexing-and-conversation-flow.png" alt="indexing and conversation flow">

> **Note importante :** 
>
> Il faut que l’ingestion de données et cette configuration finale utilise le même LLM

En [Étape 4](step_4.md), vous avez réalisé une ingestion de données, via un programme en python.
Normalement, si l’ingestion a été correctement réalisé le programme a terminé avec un succès qui affiche des Id, comme dans l’exemple suivant :

<img src="img/python-ingestion-result.png" alt="résultat de l'ingestion en python">

Dans ce résultat, vous avez une variable nommée **Index session ID** qui fournit un identifiant unique.
Copier cet identifiant pour le coller dans le champ **Indexing session id**.


Dans l’intitulé **Conversation flow** et dans le champ **No answer sentence**, vous devez spécifier une phrase lorsque l’IA n’est pas capable de répondre.
Par la même occasion, vous pouvez aussi rediriger vers une story spécifique dans le champ **Unanswered story redirection**

Par exemple si on met à jour les différents éléments et que vous sauvegardez en cliquant en haut sur le bouton bleu 
**SAVE**, vous devriez voir apparaitre une bannière verte signifiant que tout est correcte.

<img src="img/rag-settings-success.png" alt="rag settings final">

Dès que cela est bon, vous pouvez activer le RAG, en revenant en haut de page (par défaut celui-ci est désactivé).

<img src="img/active-rag.png" alt="activation du rag">


## Interroger le bot

Maintenant vous pouvez discuter avec le bot et lui poser des questions.

<img src="img/rag-question.png" alt="question avec le rag">

## Étape suivante

- [Étape 6](step_6.md)
