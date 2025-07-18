# Utiliser l'image officielle Cypress
FROM cypress/included:latest

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers de configuration
COPY package*.json ./
COPY cypress.config.js ./

# Copier les tests et fixtures
COPY cypress ./cypress

# Installer les dépendances (si nécessaire)
RUN npm ci

# Commande par défaut pour lancer les tests
CMD ["npx", "cypress", "run"]