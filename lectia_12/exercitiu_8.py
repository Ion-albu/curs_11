"""
Task: Creați o funcție cu numele "task_8" care calculează costul unei călătorii.
Parametri: distanta_km (obligatoriu), pret_pe_km (default 2.5), 
          numar_pasageri (default 1), reducere_grup (default False).
Logica: cost_baza = distanta_km * pret_pe_km * numar_pasageri
        dacă reducere_grup=True și numar_pasageri >= 3: aplicați 15% reducere
        dacă reducere_grup=True și numar_pasageri >= 5: aplicați 25% reducere
Returnează costul final rotunjit la 2 zecimale.
"""
