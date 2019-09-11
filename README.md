# AccountingOCR

This repository is still under development and is no working example yet!

## format

Datum (1) / Beleg (2) / Konto (3) / BuchText (4) / Betrag (5) / GKonto (6) / StCode (7).

To detect: 1, 2, 4, 5.

Das Feld 4 soll zwei Angaben liefern: Lieferantennamen (4a) und Bezeichnung der gelieferten Ware (4b), durch einen Komma getrennt, aber in einem Textfeld ausgegeben.

Kontierungsregeln (Mapping):

If "Unitymedia" or "Vodafone":
 Feld 3 - "4920", 
 Feld 6 - "1371", 
 Feld 7 - "01" (note the zero!).

Für jeden Beleg: 
wenn auf dem Beleg 19% erscheint, dann soll im Feld 7 "01" ausgegeben werden, wenn auf dem Beleg 7% erscheint - dann "02". Wenn beide Steuerarten vorhanden sind, wäre es nicht schlecht, dass das Programm zwei Zeilen mit den selben Inhalten in den Feldern 1, 2 und 4 erzeugt. Im Feld 7 würde dann jeweils 01 und 02 erscheinen für 19% und 7% und im Feld 5 soll der entsprechende Bruttobetrag errechnet werden, anhand von Steuersumme durch Hochrechnung auf Bruttosumme oder als Summe vom Netto + USt-Betrag (was dir am möglichsten erscheint. Den Fall hast du auf dem Combi Verbrauchermarkt-Beleg). 

Wenn auf dem Beleg keine Angaben über den USt-Satz sind, soll das Feld 7 frei gelassen werden.
