[<img src="img/a-la-recherche-du-rag-perdu.png"  alt="A la recherche du RAG perdu 🤠🧭🤖 : créez votre IA Générative sans Internet">](https://www.devoxx.fr/agenda-2025/talk/?id=65062)

Ce tutorial est proposé en amont de la session [A la recherche du RAG perdu 🤠🧭🤖 : créez votre IA Générative sans Internet](https://www.devoxx.fr/agenda-2025/talk/?id=65062) à Devoxx France 2025.

## Prérequis

### Récupérer l'atelier
  - Récupérez le projet depuis votre terminal en faisant une git clone du projet
  ```bash
  git clone https://github.com/pi-2r/devoxxfr2025-tock-studio-IA-Gen.git
  ```
- Ou bien téléchargez le projet en zip et dézippez-le sur votre machine: https://github.com/pi-2r/devoxxfr2025-tock-studio-IA-Gen/archive/refs/heads/main.zip

### L'outil Docker
- Avoir installé [Docker Desktop](https://www.docker.com/products/docker-desktop/) sur votre machine
<img src="img/docker-desktop-install.png" alt="docker-desktop" >

### L'outil Ollama
- Avoir installé [Ollama](https://ollama.com/download) sur votre machine
<img src="img/ollama.png"  alt="ollama">


### Les modèles Ollama
- Avoir installé les principaux modèles pour l'atelier, commande à renseigner dans le terminal :
  ```bash
    ollama pull tinyllama
    ollama pull mistral
    ollama pull nomic-embed-text
  ```
Pour vérifier que nous avons les modèles sur notre machine, il suffit de taper cette commande dans notre terminal pour avoir ce type de rendu :

```bash
 ollama list
 ```

<img src="img/ ollama_list.png" alt="ollama list">


### Les images Docker

Rendez-vous dans le dossier **docker** de ce dossier et renommez le fichier **template-internet.env** en **.env**.
Toujours depuis ce dossier, lancez les commandes suivantes dans votre terminal :

```bash
source .env
docker compose -f docker-compose-genai.yml pull
```
