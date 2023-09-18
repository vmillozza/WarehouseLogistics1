Esercitazione corso Python

### Obiettivo
Creare un software per la gestione logistica del magazzino di un e-commerce utilizzando Python (Tkinter) e MySQL. Il software dovrà permettere un controllo accurato dello stock dei prodotti, generare codici di spedizione e inviare notifiche per diverse operazioni.

#### 1. Struttura del Database

Crea un database MySQL con almeno le seguenti tabelle:

- Utenti: Per memorizzare informazioni sugli utenti (es. username, password).
- Prodotti: Per memorizzare informazioni sui prodotti (es. ID prodotto, nome prodotto, codice, quantità, prezzo).
- Ordini: Per registrare gli ordini effettuati (es. ID ordine, ID prodotto, quantità ordinata, codice spedizione).
- Notifiche: Per registrare tutte le notifiche (es. ID notifica, messaggio, data e ora).

#### 2. Interfaccia Utente

Utilizza Tkinter per creare un'interfaccia grafica che contenga le seguenti pagine:

- Login: Pagina per l'autenticazione degli utenti.
- Gestione Prodotti: Pagina per visualizzare, aggiungere, modificare ed eliminare i prodotti.
- Pagina Ordini: Per visualizzare e gestire gli ordini.
- Pagina Notifiche: Per visualizzare tutte le notifiche.

#### 3. Funzionalità

Le seguenti funzionalità devono essere implementate:

- Login: Gli utenti devono autenticarsi per accedere al software.
- Gestione Prodotti: Aggiungere funzionalità per registrare i prodotti che entrano in magazzino con tutti i dettagli richiesti.
- Gestione Ordini: Quando un ordine viene effettuato, il sistema deve:
  - Ridurre automaticamente la quantità del prodotto in magazzino.
  - Generare un codice di spedizione casuale se il prodotto è disponibile.
  - Segnare la riga in rosso se il prodotto non è disponibile.
- Notifiche: Creare un sistema di notifiche che registri eventi importanti e li visualizzi nella pagina di notifiche.

#### 4. Notifiche

Implementare un sistema di notifiche che invii notifiche in diverse situazioni, ad esempio:

- Quando un nuovo prodotto entra in magazzino.
- Quando un prodotto viene ordinato.
- Quando un prodotto sta per esaurirsi.



PS si consiglia di creare una documentazione che spiega come utilizzare il software, con screenshot inclusi per illustrare le varie funzionalità.
PPS si consiglia di commentare TUTTO il codice python spiegando tutto ciò che quel codice /funzione sta facendo

