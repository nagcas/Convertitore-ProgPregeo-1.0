"""
+----------------------------------------------------------------------------------+
|  Programma converti file (csv) o (txt) in formato (dat) leggibile da Pregeo 10   |
|  ver. 1.0 (testuale)                                                             |
+----------------------------------------------------------------------------------+

 ...14.04.2016
 ...by Gianluca Chiaravalloti

 ...rev. 28/04/2016
 ...rev. 14/11/2024


Esempio di ingresso dati iniziali:

file.csv o file.txt (origine)

STN     100       ,1.430,CHIODO    
XYZ     0.000,0.000,0.000
SS      101       ,3.600,SPIG.FABBR
SD      100.2380,323.5725,38.944
SS      102       ,5.000,SPIG.FABBR
SD      97.4713,359.7077,24.686    


per ottenere il seguente risultato pregeo.dat

0|DATA RILIEVO|PROTOCOLLO|CODICE COMUNE|FOGLIO|PARTICELLE|COGNOME NOME|QUALIFICA|COMUNE|
9|QUOTA|20|10|EST MEDIA|10.00-G,APAG 2.03|MA|STAZIONE TOTALE KEYTOP 335|
1|100|1.430|CHIODO|
2|101|323.5725|100.2380|38.944|3.600|SPIG.FABBR.|
2|102|359.7077|97.4713|24.686|5.00|SPIG.FABBR.|


"""

import os
import time
import random

def menu():
    scelta = True
    ok = False
    while scelta:
        print('+' + '*' * 78 + '+')
        print('\nProgramma converti file (.csv) o (.txt) in file leggibile da Pregeo (pregeo.dat)\n')
        print('+' + '*' * 78 + '+')
        print('\n')
        print('1]....................Carica file (tipo csv o txt)')
        print('2].......Visualizza file caricato tipo (csv o txt)')
        print('3]........................Elabora il file caricato')
        print('4].........Crea il file dettaglio.txt e pregeo.dat')
        print('5]...................Visualizza il file pregeo.dat')
        print('6]................Visualizza il file dettaglio.txt')
        print('7]..............................Info sul programma')
        print('8]............................................Esci\n')
        
        scelta = input('Scegli >>  ')
        if scelta in '12345678':
            
            if scelta == '1':
                # carica il file originale csv o txt
                print('\nCarica file (tipo csv o txt)\n')
                dati, ok = leggi(scriviNome(), ok)
    
            if scelta == '2':
                #visualizza il file caricato riga per riga
                print('\nVisualizza file caricato tipo (csv o txt)\n')
                if ok:
                    visualizza(dati, ok)
                else:
                    print('\nNon è possibile visualizzare il file origine in quanto non è stato caricato...\n')
                    
            if scelta == '3':
                # elabora il file caricato
                print('\nElabora il file caricato\n')
                if ok:
                    rm = random.randint( 1, 5000)
                    os.mkdir('Rilievo_' + time.strftime("%d_%m_%Y") + '_' + str(rm))
                    os.chdir('Rilievo_' + time.strftime("%d_%m_%Y") + '_' + str(rm))
                    content, ok = eliminaACapo(dati, ok)
                    content, ok = insVirgola(content, ok)
                    content, ok = creaLista(content, ok)
                    content, ok = elementiNull(content, ok)
                    content, ok = crea(content, ok)
                
                    # elaborazione dettagliata
                    dat, ok = leggi('dati_puliti.txt', ok)
                    dat, ok = eliminaACapo(dat, ok)
                    dat, ok = creaLista(dat, ok)
                    dat, ok = creaCoppia(dat, ok)
                    dat, ok = creaDiz(dat, ok)
                    dat, ok = registra(dat, ok)
                    print('\nElaborazione avvenuta con successo\n')
                else:
                    print('\nNon è possibile effettuare l''elaborazione in quanto non è stato caricato nessun file iniziale...\n')
                    
            if scelta == '4':
                # crea il file dettaglio.txt e pregeo.dat
                print('\nCrea il file dettaglio.txt e pregeo.dat\n')
                if ok:
                    creaFileDettaglio(dat, ok)
                    creaPregeo(dat, ok)
                else:
                    print('\nNon è possibile creare il file pregeo.dat e dettaglio.txt in quanto non è stato caricato nessun file iniziale...\n')
                                                    
            if scelta == '5':
                # caricare se esiste il file pregeo.dat
                print('\nVisualizza il file pregeo.dat\n')
                if ok:
                    ris, ok = leggi('pregeo.dat', ok)
                    visualizza(ris, ok)
                else:
                    print('\nNon è possibile visualizzare il file pregeo.dat in quanto non è stato creato...\n')

            if scelta == '6':
                # carica il file dettaglio.dat
                print('\nVisualizza il file dettaglio.txt\n')
                if ok:
                    ris, ok = leggi('dettaglio.txt', ok)
                    visualizza(ris, ok)
                else:
                    print('\nNon è possibile visualizzare il file dettaglio.txt in quanto non è stato creato...\n')


            if scelta == '7':
                print('\nInfo sul programma\n')
                      
            if scelta == '8':
                print('\nSei uscito dal programma...\n')
                scelta = False
                
        else:
            print('\nHai selezionato un tasto errato...\n')
            scelta = True
    

def scriviNome():                               # inserisci da tastiera il nome del file
    nome_file = input('Inserisci il nome del file >> ')
    return nome_file
    

def leggi(nome_file, ok):                       # legge il file di ingresso
    try:
        with open(nome_file) as fin:
            content = fin.readlines()           # organizza il contenuto del file in liste
        print('\nFile letto correttamente.\n')
        ok = True
        fin.close()
        return content, ok
    except:
        print('\nFile inesistente!\n')
        ok = False
        return -1, ok
        
            

def eliminaACapo(val, ok):                     # elimina da ogni singola riga il carattere speciale ( \n )
    esito = False
    if ok:
        for elem in range(len(val)):
            val[elem] = val[elem].strip()
        esito = True

        if esito:
            fout = open('esito.dat', 'a')
            fout.write('eliminaACapo: ' + str(esito) + '\n')
    #print('Funzione eliminaACapo - Numero di righe elaborate: ' + len(val()))
    return val, ok


def insVirgola(val, ok):                        # elimina gli spazi di ogni singola linea e li sostituisce con il carettere ( , )
    esito = False
    if ok:
        for elem in range(len(val)):
            val[elem] = val[elem].replace(' ', ',')
        esito = True

        if esito:
            fout = open('esito.dat', 'a')
            fout.write('insVirgola: ' + str(esito) + '\n')
    #print('Funzione insVirgola - Numero di righe elaborate: ' + len(val()))
    return val, ok


def creaLista(val, ok):                        # crea la lista a partire dal carattere ( , )
    esito = False
    if ok:
        for elem in range(len(val)):
            val[elem] = val[elem].split(',')
        esito = True

        if esito:
            fout = open('esito.dat', 'a')
            fout.write('creaLista: ' + str(esito) + '\n')
    #print('creaLista - Numero di righe elaborate: ' + len(val()))
    return val, ok


def elementiNull(val, ok):                     # sostituisce in ogni riga il valore nullo ( "" ) con la stringa ( NULL )
    esito = False
    if ok:
        for elem in range(len(val)):
            for i in range(len(val[elem])):
                if val[elem][i] == '':
                    val[elem][i] = 'NULL'
        esito = True

        if esito:
            fout = open('esito.dat', 'a')
            fout.write('elementiNull: ' + str(esito) + '\n')
    #print('Funzione elementiNull - Numero di righe elaborate: ' + len(val()))
    return val, ok


#funzione al momento non utilizzata
'''
def eliminaNull(val, ok):
    for elem in range(len(dati[0])):
        vai = range(len(dati[elem]))
        for i in vai:
            if dati[elem][i] == 'NULL':
                del dati[elem][i]
                vai = range(len(dati[elem]))

    return val, ok
'''


def crea(val, ok):                             # crea il file in modo ordinato e separato da virgola
    esito = False
    if ok:
        fout = open('dati_puliti.txt', 'w')
        for elem in range(len(val)):
            c = val.count('NULL')
            d = ((len(val[elem])) - c - 1)
            for i in range(len(val[elem])):
                if val[elem][i] != 'NULL':
                    fout.write(str(val[elem][i]))
                    if i < d:
                        fout.write(',')
            fout.write('\n')
        fout.close()
        esito = True

        if esito:
            fout = open('esito.dat', 'a')
            fout.write('crea(dati_puliti.txt): ' + str(esito) + '\n')
            fout.close()

    return val, ok


def visualizza(val, ok):                       # visualizza il file
    if ok:
        for elem in range(len(val)):
            print('Riga[',elem,']: ', val[elem], sep = '', end = '\n')
    else:
        print('\nFile non caricato...\n')


def creaDiz(val, ok):                          # crea il dizionario 
    esito = False
    if ok:
        res = []
        for elem in range(len(val)):
            if 'STN' in val[elem] and 'XYZ' in val[elem]:
                for i in range(len(val[elem])):
                    diz = { 'Stazione'         : val[elem][1],
                            'Altezza_Stazione' : val[elem][2],
                            'Note'             : val[elem][3],
                            'Coordinata_X'     : val[elem][5],
                            'Coordinata_Y'     : val[elem][6],
                            'Coordinata_Z'     : val[elem][7] }

            if 'SS' in val[elem] and 'SD' in val[elem]:
                for i in range(len(val[elem])):
                    diz = { 'Punto_Dettaglio'     : val[elem][1],
                            'Altezza_Prisma'      : val[elem][2],
                            'Note'                : val[elem][3],
                            'Direzione_Zenitale'  : val[elem][5],
                            'Direzione_Azimutale' : val[elem][6],
                            'Distanza_Inclinata'  : val[elem][7] }
     
            res.append(diz)
        esito = True

        if esito:
            fout = open('esito.dat', 'a')
            fout.write('creaDiz: ' + str(esito) + '\n')
            fout.close()
                
    return res, ok


def creaCoppia(val, ok):                       # unisce due righe del file (STN + XYZ) e (SS + SD) in una nuova riga STN 
    esito = False
    if ok:
        res = []
        riga_1 = 0
        riga_2 = 1
        for elem in range(len(val)):
            if riga_2 < len(val):
                res.append(val[riga_1] + val[riga_2])
                riga_1 += 2
                riga_2 += 2
        esito = True

        if esito:
            fout = open('esito.dat', 'a')
            fout.write('creaCoppia: ' + str(esito) + '\n')
            fout.close()
        
    return res, ok


def registra(val, ok):                         # crea il file dizionario
    esito = False
    if ok:
        fout = open('dati_diz.txt', 'w')
        for elem in range(len(val)):
            fout.write(str(val[elem]) + '\n')

        fout.close()
        esito = True

        if esito:
            fout = open('esito.dat', 'a')
            fout.write('registra(dati_diz.txt): ' + str(esito) + '\n')
            fout.close()
        
    return val, ok


def mostra(val):                             # mostra a video il risultato dei dizionari creati
    for elem in range(len(val)):
        if 'Stazione' in val[elem]:
            print('Stazione: ', val[elem]['Stazione'], sep = '', end = '')
            print(' Altezza Stazione: ', val[elem]['Altezza_Stazione'], sep = '', end = '')
            print(' Note: ',val[elem]['Note'])
        if 'Punto_Dettaglio' in val[elem]:
            print('Punto di Dettaglio: ', val[elem]['Punto_Dettaglio'], sep = '', end = '')
            print(' Altezza Prisma: ', val[elem]['Altezza_Prisma'], sep = '', end = '')
            print(' Direzione Zenitale: ', val[elem]['Direzione_Zenitale'], sep = '', end = '')
            print(' Direzione Azimutale: ', val[elem]['Direzione_Azimutale'], sep = '', end = '')
            print(' Distanza Inclinata: ', val[elem]['Distanza_Inclinata'], sep = '', end = '')
            print(' Note: ', val[elem]['Note'], sep = '')
          
    
def creaFileDettaglio(val, ok):             # crea un file dettagliato a partire dal dizionario creato
    # creazione del file dettaglio.txt
    esito = False
    if ok:
        fout = open('dettaglio.txt', 'w')
        fout.write('Rilievo Celerimetrico\n')
        for elem in range(len(val)):
            if 'Stazione' in val[elem]:
                fout.write('Stazione: ' + (str(val[elem]['Stazione'])) + '\t')
                fout.write('Altezza Stazione: ' + (str(val[elem]['Altezza_Stazione'])) + '\t')
                fout.write('Note: ' + (str(val[elem]['Note'])) + '\n')
            if 'Punto_Dettaglio' in val[elem]:
                fout.write('Punto di Dettaglio: ' + (str(val[elem]['Punto_Dettaglio'])) + '\t')
                fout.write('Altezza Prisma: ' + (str(val[elem]['Altezza_Prisma'])) + '\t')
                fout.write('Direzione Zenitale: ' + (str(val[elem]['Direzione_Zenitale'])) + '\t')
                fout.write('Direzione Azimutale: ' + (str(val[elem]['Direzione_Azimutale'])) + '\t')
                fout.write('Distanza Inclinata: ' + (str(val[elem]['Distanza_Inclinata'])) + '\t')
                fout.write('Note: ' + (str(val[elem]['Note'])) + '\n')
            
        # chiusura del file dettagglio.txt
        fout.close()
        esito = True

        if esito:
            fout = open('esito.dat', 'a')
            fout.write('creaFileDettaglio(dettaglio.txt): ' + str(esito) + '\n')
            fout.close()
            
    return val, ok

def creaPregeo(val, ok):                    # crea il file pregeo.dat a partire dal dizionario creato
    esito = False
    if ok:
        fout = open('pregeo.dat', 'w')

        data_rilievo = input('Inserisci data rilievo >> ')
    
        # elimina il carattere (/), (.), (-) dalla data
        if '/' in data_rilievo:
            data_rilievo = data_rilievo.replace('/', '')
        if '.' in data_rilievo:
            data_rilievo = data_rilievo.replace('.', '')
        if '-' in data_rilievo:
            data_rilievo = data_rilievo.replace('-', '')

        # inserisci protocollo
        conv_protocollo = False
        while not conv_protocollo:
            protocollo = input('Inserisci numero di protocollo >> ')
            conv_protocollo = protocollo.isdecimal()
        protocollo = int(protocollo)

        # inserisci codice Comune
        codice = False
        while not codice:
            cc = input('Inserisci il Codice Comune >> ')
            cc = cc.capitalize()
            codice = (cc[0] in 'QWERTYUIOPASDFGHJKLZXCVBNM' and cc[1:].isdecimal())

        # inserisci foglio di mappa
        conv_mappa = False
        while not conv_mappa:
            foglio = input('Inserisci foglio di mappa >> ')
            conv_mappa = foglio.isdecimal()
            # il foglio deve contenere 4 caratteri 0000 es foglio 10 ---> 0010
            if len(foglio) == 1:
                foglio = '00' + foglio + '0'
            if len(foglio) == 2:
                foglio = '0' + foglio + '0'
            if len(foglio) == 3:
                foglio = foglio + '0'  
        #foglio = int(foglio)
            print(foglio)

        # inserisci mappale
        conv_mappale = False
        while not conv_mappale:
            mappale = input('Inserisci una o più particella separata da virgola (es. 12,34,56) >> ')
            conv_mappale = mappale.isdecimal()
        mappale = int(mappale)

        # inserisci cognome e nome
        conv_operatore = False
        while not conv_operatore:
            cognome = input('Inserisci il cognome (max 12 caratteri) >> ')
            nome = input('Inserisci il nome (max 12 caratteri)  >> ')
            conv_operatore = (cognome.isalpha() and nome.isalpha()
                        and (len(cognome) <= 12) and (len(nome) <= 12))
        cognome = cognome.upper()
        nome = nome.upper()
        
        # inserisci qualifica
        conv_qualifica = False
        while not conv_qualifica:
            qualifica = input('Inserisci qualifica >> ')
            conv_qualifica = qualifica.isalpha()
        qualifica = qualifica.upper()

        # inserisci comune
        conv_comune = False
        while not conv_comune:
            comune = input('Inserisci comune >> ')
            conv_comune = comune.isalpha()
        comune = comune.upper()

        #inserisci quota in metri
        conv_quota = False
        while not conv_quota:
            quota = input('Inserisci quota in metri >> ')
            conv_quota = quota.isdecimal()
        quota = int(quota)

        #inserisci est-media
        conv_estMedia = False
        while not conv_estMedia:
            estMedia = input('Inserisci est media >> ')
            conv_estMedia = estMedia.isdecimal()
        estMedia = int(estMedia)
      
        # dati statistici (riga 0)
        fout.write('0' + '|' + data_rilievo + '|' + str(protocollo) + '|' +
                   cc + '|' + str(foglio) + '|' + str(mappale) + '|' +
                   cognome + ' ' + nome + '|' + qualifica + '|' +
                   comune + '|' + '\n')
    
        # quota, precisioni, est media, nota (riga 9)
        fout.write('9' + '|' + str(quota) + '|' + '10' + '|' + '20' + '|' +
                   str(estMedia) + '|' + '10.00-G,APAG 2.03' + '|' + 'MA' + '|' +
                   'STAZIONE TOTALE KEYTOP 335' + '|' + '\n')

    
        for elem in range(len(val)):
            if 'Stazione' in val[elem]:
                
                # rilievo celerimetrico: punto stazione (riga 1)
                fout.write('1' + '|' + val[elem]['Stazione'] + '|' +
                   val[elem]['Altezza_Stazione'] + '|' + val[elem]['Note'] + '|' + '\n')
    
            if 'Punto_Dettaglio' in val[elem]:
                # rilievo celerimetrico: punto osservato (riga 2)
                fout.write('2' + '|' + val[elem]['Punto_Dettaglio'] + '|' + val[elem]['Direzione_Azimutale'] +
                   '|' + val[elem]['Direzione_Zenitale'] + '|' + val[elem]['Distanza_Inclinata'] +
                   '|' + val[elem]['Altezza_Prisma'] + '|' + val[elem]['Note'] + '|' + '\n')
    
    
        # chiusura del file
        fout.close()
        esito = True

        if esito:
            fout = open('esito.dat', 'a')
            fout.write('creaPregeo(pregeo.dat): ' + str(esito) + '\n')
            fout.close()

        


'''   
#dati = leggi("Rilievo_13042016.txt")
dati = eliminaACapo(leggi('Rilievo_13042016.txt'))
dati = insVirgola(dati)
dati = creaLista(dati)
dati = elementiNull(dati)

#dati = eliminaNull(dati) funzione non utilizzata

dati = crea(dati)


temp = eliminaACapo(leggi('dati_puliti.txt'))
temp = creaLista(temp)
temp = creaCoppia(temp)
temp = creaDiz(temp)

#registra(temp)

#visualizza(temp)

mostra(temp)
creaMostraFile(temp)

creaPregeo(temp)
'''

menu()
