# Utilise une image officielle Cypress
FROM cypress/included:12.17.4

# Crée un dossier pour ton code
WORKDIR /e2e

# Copie ton projet dans le conteneur
COPY . .

# Installe les dépendances
RUN npm install

# Commande par défaut pour lancer les tests
CMD ["npx", "cypress", "run"]
