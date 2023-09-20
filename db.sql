-- Creazione della tabella Utenti
CREATE TABLE Utenti (
    userID INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
);

-- Creazione della tabella Prodotti
CREATE TABLE Prodotti (
    prodottoID INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_prodotto VARCHAR(255) NOT NULL,
    codice VARCHAR(255) NOT NULL,
    quantità INT NOT NULL,
    prezzo DECIMAL(10, 2) NOT NULL
);

-- Creazione della tabella Ordini
CREATE TABLE Ordini (
    ordineID INTEGER PRIMARY KEY AUTOINCREMENT,
    prodottoID INT,
    quantità_ordinata INT NOT NULL,
    codice_spedizione VARCHAR(255) NOT NULL,
    FOREIGN KEY (prodottoID) REFERENCES Prodotti(prodottoID)
);

-- Creazione della tabella Notifiche
CREATE TABLE Notifiche (
    notificaID INTEGER PRIMARY KEY AUTOINCREMENT,
    messaggio TEXT NOT NULL,
    data_ora TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
INSERT INTO Utenti (username, password)
VALUES ('your_username', 'your_password');
INSERT INTO Utenti (username, password)
VALUES ('lallo', 'password');
INSERT INTO Prodotti (nome_prodotto, codice, quantità, prezzo) 
VALUES ('Pc', '1aswert', 2, 3.5);
INSERT INTO Prodotti (nome_prodotto, codice, quantità, prezzo) 
VALUES ('scanner', '1aswert3a', 1, 3.5);
INSERT INTO Ordini (prodottoID, quantità_ordinata, codice_spedizione)
VALUES (1, 10, 'ABC12345');
