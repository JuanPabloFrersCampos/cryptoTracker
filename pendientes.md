Deuda técnica
- Inyección de dependencias
- Tests unitarios
- Refactor de la wallet
- Handleo errores API externa

Performance
- /wallet:
  - Consumo API de Cryptos:
    - Crear una task que corra cada N, fetchee el precio de los símbolos en la instancia y persista en memoria. Cuando se haga un GET a /wallet, usar este objeto.
- Caché cryptos disponibles:
  - Al consultar las cryptos creadas en la instancia, hacerlo contra un caché y no contra la BDD. Invalidar el caché al crear una nueva crypto.

Investigación
- Versionamiento de APIs