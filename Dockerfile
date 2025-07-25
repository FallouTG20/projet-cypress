FROM cypress/included:12.17.4

WORKDIR /e2e

COPY . .

RUN npm install

# Crée le dossier results pour stocker les rapports JUnit
RUN mkdir -p results

# Lance Cypress avec génération de rapport JUnit dans results/
CMD ["npx", "cypress", "run", "--reporter", "junit", "--reporter-options", "mochaFile=results/results-[hash].xml,toConsole=true"]
