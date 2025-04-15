# Todo

- [ ] Rédac :
    - [X] Refaire le tuto avec la dernière version de TOCK et voir pour une autre release avec Julien si besoin.
    - [X] Tester de nouveaux LLMs en choisir 1-2.
    - [ ] Screenshot le nom du bot.
    - [ ] Compresseur introduit en plus (?)
    - [ ] Proposer les modèles suivants en terme de llm `qwen2.5:1.5b` (pour le gen sentence), `qwen2.5:3b`, `mistral:7b`.
    - [X] Step 4 capture d'écran à revoir.
    - [ ] Schéma de réseau en annexe pour ces histoire de docker et host internal.
    - [X] Step 5 refaire un test avec model Mistral.
    - [ ] Step 5 refaire un test avec model gemma.
    - [ ] Step 5 revoir les screenshot avec la nouvelle version de TOCK bien expliquer ce qu'est le prompt de condensation.
    - [X] Step 6 MAJ la capture d'écran.
    - [X] Mettre lien promptfoo dans la partie 7 -red teaming-
    - [ ] Lire promptfoo sur le hacking LLM
    - [X] Step 7 capture d'écran sur le ban de jailbreak / Rag Excluded avec un exemple de jailbreak. @Pierre
    - [ ] Step 7 revoir les reco prompt coté Arkéa @Benjamin ou faire un prompt personalisé
    - [ ] Step 7 ou bis ? ajouter la partie compresseur avec leur serveur amené chez nous.
    - [X] Step 9 où lancer les commandes scrapy
    - [X] Changement du dataset film horreur ?? ==> Séries.
    - [ ] Langfuse partie public URL et indiquer qu'il y a un lien dans tock.
    - [ ] Tock Vue Kit se base sur la locale du navigateur est doc le bot répond en FR. Changement dans le prompt possible.
    - [ ] Step 4 : Mettre à dispo le CSV `TMDB_tv_dataset_v3.csv` sur le serveur.
- [X] Activer le debug RAG par défaut dans le docker compose. Possible également via les RAG Settings.
- [ ] Voir avec l'orga :
  - [X] Prise réseau.
  - [ ] Nombre de participants : => répondre à l'orga
- [X] Revoir la page du tock vue kit `index-tvk.html` en mode Indiana Johnes @Rodolphe.
- [ ] Matériel :
  - [X] @Benjamin vient avec un Mac à la place de l'UC, bien penser à fixer son IP sur l'AP wifi.
  - [X] @Benjamin routeur Wifi
  - [ ] Pierre ou autre ? Avoir un 2ème switch 4p si possible.
  - [ ] Multiprises.
- Plan de backup :
  - [X] Azure OpenAI, @Benjamin voir avec l'équipe Data Archi pour avoir au moins une clé. ==> Orga de dev bis sinon ?
  - [X] Machine de backup avec tout le codelab, générer 20 indentifiants avec property et roles et prévoir un PAD pour que chaque personnes choissent son ID @Benjamin.
  - [X] Préparer le MAC en backup de l'UC.
  - [X] Tester une registry ollama locale : https://github.com/simonfrey/ollama-registry-pull-through-proxy KO remplacé.
  - [X] Voir pour gérer l'hébergement du nomic embed tiny (si la registry local ollama marche pas)
  - [ ] Test si registry:3 supporte ou pas mieux le multi architecture
  - [ ] Pré-ingérer des données dans tous les bots.
  - [ ] Check tout ce qui référence 192.168.20.3 .. tout sera sur la 20.2 gpu-server.lan



