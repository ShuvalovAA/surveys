# Требования
- docker
- ОC: Ubuntu

# Деплой
## Local
Прописать хост для резолва
```bash
sudo sh -c 'echo "127.0.0.1 local.survey" >> /etc/hosts'
```

Из корня проета выполнить команду
```bash
make project_up
```
_Документация доступна по адресу: http://local.survey:8080/api/docs/_
