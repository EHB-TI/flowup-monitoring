# flowup-monitoring
Integration Project - Groep 2 - Monitoring
## First setup
Deze twee commando's runnen:
```
sysctl -w vm.max_map_count=262144
docker-compose -f docker-compose.setup.yml run --rm keystore
docker-compose -f docker-compose.setup.yml run --rm certs
```

De .env file aanpassen om de password/username te veranderen.

## Opstarten
Om de hele service te opstarten is er maar een commando nodig:
```
docker-compose up -d
```
## Stoppen
```
docker-compose down
```
### Stoppen + volumes verwijderen
```
docker-compose down -v
```