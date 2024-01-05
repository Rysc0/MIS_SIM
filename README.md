### Generiranje dolazaka -> data.py
### Računanje vremena između dolazaka -> time_diff.py

Obje skripte kreiraju .json datoteke koje se kasnije mogu importati u excel za daljnju obradu.
Dan je primjer datoteka koje se generiraju. Kako bi se podaci mogli dalje koristiti za simulaciju potrebno je iz time_diff datoteke kreirati tablicu ulaznih vrijednosti (Broj dolazaka/Vrijeme između dolazaka).

Primjer tablice:

| Vrijeme usluživanja (u sekundama) 	|  0-99 	| 100-199 	| 200-299 	| 300-399 	| 400-499 	| 500-599 	| Ukupno 	|
|:---------------------------------:	|:-----:	|:-------:	|:-------:	|:-------:	|:-------:	|:-------:	|:------:	|
|             Učestalost            	|   70  	|   153   	|    80   	|    5    	|    13   	|    22   	|   343  	|
|            Reprezentant           	|   74  	|   148   	|   221   	|   378   	|   454   	|   551   	|        	|
|      Relativna učestalost (%)     	| 20.41 	|  44.61  	|  23.32  	|   1.46  	|   3.79  	|   6.41  	|   100  	|
|    Kumulativna distribucija (%)   	| 20.41 	|  65.02  	|  88.34  	|   89.8  	|  93.59  	|   100   	|        	|
|     Razredi slučajnih brojeva     	|   0   	|  20.41  	|  65.02  	|  88.34  	|   89.8  	|  93.59  	|        	|
|                                   	|  20.4 	|  65.01  	|  88.33  	|  89.79  	|  93.58  	|  99.99  	|        	|

---

Dan je primjer tablice za Vrijeme usluživanja! Po istom principu potrebno je obraditi podatke iz time_diff.json datoteke kako bi se dobila tablica za vremena između dolazaka!
