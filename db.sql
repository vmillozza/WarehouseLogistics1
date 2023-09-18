-- Creazione della tabella Utenti
CREATE TABLE Utenti (
    userID INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
);

-- Creazione della tabella Prodotti
CREATE TABLE Prodotti (
    prodottoID INT AUTO_INCREMENT PRIMARY KEY,
    nome_prodotto VARCHAR(255) NOT NULL,
    codice VARCHAR(255) NOT NULL,
    quantità INT NOT NULL,
    prezzo DECIMAL(10, 2) NOT NULL
);

-- Creazione della tabella Ordini
CREATE TABLE Ordini (
    ordineID INT AUTO_INCREMENT PRIMARY KEY,
    prodottoID INT,
    quantità_ordinata INT NOT NULL,
    codice_spedizione VARCHAR(255) NOT NULL,
    FOREIGN KEY (prodottoID) REFERENCES Prodotti(prodottoID)
);

-- Creazione della tabella Notifiche
CREATE TABLE Notifiche (
    notificaID INT AUTO_INCREMENT PRIMARY KEY,
    messaggio TEXT NOT NULL,
    data_ora TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
