# Lab server

Ce dossier contiens des indication sur le montage du serveur du lab contenant :
- Registry Docker
- Serveur d'inférence Ollama avec proxy de registry ollama
- Stack Tock complète avec 60+ comptes

Ces différents serveur sont à utilisé pour les participants qui n'arrivent pas à le faire tourner en local.

## Checklist avant lab

- [ ] Bien configuré l'IP gpu-server.lan `192.168.20.2` pour pointer vers la machine servant de serveur ollama
- [ ] Bien configuré l'IP tock.lan `192.168.20.3` pour pointer vers la machine servant de stack TOCK, s'il s'agit de la même machine bien mettre à jour la config host dans [step_1.md](../step_1.md)
- [ ] Pull les images sur la registry docker local.
- [ ] Pull les modèle ollama sur la registry local / proxy ollama.
- [ ] Initier un fichier Google Sheet pour que les gens puissent choisir les identifiants sur la stack tock de backup.

## Lancer la stack tock de backup

```bash
cp template.env .env
source .env
docker compose -p devoxx_lab_server -f docker-compose-tock-registry-reranker.yml up -d
```
