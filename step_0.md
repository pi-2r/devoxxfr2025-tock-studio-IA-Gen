# Tock: The Open Conversation Kit
[<img src="img/Indiana-Jones.png"  alt="Indiana-Jones">](https://www.youtube.com/watch?v=mC1ikwQ5Zgc)

> Belloq: How odd that it should end this way for us after so many stimulating encounters. I almost regret it. Where shall I find a new adversary so close to my own level?
>
> Indiana: Try the local sewer. 
>
>Indiana Jones and the Raiders of the Lost Ark , Steven Spielberg, 1981


Tock (https://doc.tock.ai/) est une plateforme conversationnelle ouverte.
La solution fut créée par SNCF Connect and Tech en 2016 pour motoriser le chatbot Voyages-sncf.com (puis OUI.sncf avant de devenir
SNCF Connect utilisé quotidiennement par des millions de français). Partagée en opensource sur GitHub dès 2017,
la solution a depuis été reprise par de nombreuses entreprises et une communauté d'utilisateurs et de contributeurs s'est créée.

Conçue comme une plateforme d'intégration de briques NLP (Natural Language Processing) sans dépendance forte et apportant
à la fois des interfaces graphiques utilisateur et un framework conversationnel en Kotlin, la plateforme a ensuite bien
évolué : connecteurs à de nombreux canaux texte et voix, création de bots en mode "low code" dans Tock Studio,
compatibilité avec d'autres langages de programmation comme Javascript ou Python, ajout de fonctionnalités analytiques,
gestion multilingue, etc.

Plus récemment, avec l'essor de l'IA Générative et des LLM, Tock s'est révélée une plateforme efficace pour tester
et intégrer de nouvelles technologies conversationnelles, permettant des approches hybrides tout en restant en maîtrise
de la stack technique et des données. Certaines de ses fonctionnalités ont encore peu d'équivalents dans les solutions du marché :
- Combiner dans un même agent conversationnel IA Générative et arbres de décisions traditionnels
- Intégrer des solutions CSP utilisées par les équipes de Relation Client, pour passer facilement de l'IA Générative
- à un humain dans la même conversation
- Mécanismes pour activer/désactiver le RAG, exclure certains sujets, reconfigurer les prompts, etc.

A noter : c'est notamment grâce à des contributions ambitieuses des équipes Crédit Mutuel Arkéa (qui utilisent également
Tock depuis plusieurs années) que Tock a intégré ces dernières années des fonctionnalités autour des LLM et du RAG.
Cela montre toute la force de l'opensource et l'effet levier de la communauté pour une innovation qui profite à tous.

Dans ce codelab, on utilisera Tock et Ollama pour construire un agent conversationnel et expérimenter les nombreuses
possibilités offertes par ces solutions ouvertes.

En guise d'illustration, Tock a permis de concevoir de nombreux chatbots et assistants vocaux en 8 ans d'existence :
e-commerce, énergie, banque en ligne, bots internes (RH, support informatique, juridique, achats), assistants téléphoniques
comme AlloCovid en 2020 avec Allo-Media, avatars virtuels et événementiel avec SPooN, digital workplace et jeu video
avec WorkAdventure... A vous d'inventer de nouveaux usages !


> Ci-dessous une illustration du premier chatbot OUI.sncf motorisé par Tock, permettant de rechercher, réserver et
> même payer un billet de train en conversationnel (2018)
>
><center><img src="img/ouibot.png" alt="Ancienne page web de OUIbot"></center>


## Étape suivante

- [Étape 1](step_1.md)
