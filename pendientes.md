Deuda técnica
- Inyección de dependencias
- Tests unitarios
- Refactor de la wallet
- Handleo errores API externa

Performance

- Caché cryptos disponibles:
  - Al consultar las cryptos creadas en la instancia, hacerlo contra un caché y no contra la BDD. Invalidar el caché al crear una nueva crypto.

Investigación
- Versionamiento de APIs


HECHO:
- /wallet:
  - Caché contra API cotización cryptos, se crea al hittear, se invalida cada 30 segundos. > Request promedio pasa de 3seg a 600ms (aumento 80% performance)
- Caché cotización cryptos: Hacer cada 30 segundos el hit para todas las crypto registradas. > Resultado: Se bajó de 600ms a 8ms

PROBLEMAS:
  Para Redis se necesita levantar la máquina virtual de ubuntu (está automatizado para que arranque solo desde .bashrc):
    - wsl para inciar la vm