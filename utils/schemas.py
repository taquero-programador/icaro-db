"""
schemas.py: schemas para general la tablas dentro de la db,
tambien contien los querys para las consutlas.
"""

table_times = '''
        CREATE TABLE IF NOT EXISTS tiempos(
        mis_dt text,
        service_name text,
        hour text,
        dial text,
        tot_agent text,
        tot_account text,
        inicio text,
        fin text,
        trn_interval text,
        trn_field text,
        bucket text)'''


table_abandon = '''
        CREATE TABLE IF NOT EXISTS abandono(
        mis_dt text,
        service_name text,
        hour text,
        dial text,
        tot_agent text,
        tot_account text,
        attempts text,
        conections text,
        contacts text,
        direct_contact text,
        message text,
        promise text,
        abandon text,
        exclution text)'''


table_services = '''
        CREATE TABLE IF NOT EXISTS servicios(
        service_name text)'''


table_resulados = '''
        CREATE TABLE IF NOT EXISTS resultado_icaro(
        mis_dt text,
        service_name text,
        hour text,
        tot_agentes text,
        tot_accounts text,
        attempts text,
        conections text,
        direct_contact text,
        message text,
        promise text,
        exclution text,
        bucket text,
        start_hour text,
        end_hour text,
        trn_interval text,
        ov_number_dialed text,
        abandon text)'''


load_times = '''INSERT INTO tiempos(
            mis_dt,
            service_name,
            hour,
            dial,
            tot_agent,
            tot_account,
            inicio,
            fin,
            trn_interval,
            trn_field,
            bucket) VALUES(?,?,?,?,?,?,?,?,?,?,?)'''


load_abnd = '''INSERT INTO abandono(
            mis_dt,
            service_name,
            hour,
            dial,
            tot_agent,
            tot_account,
            attempts,
            conections,
            contacts,
            direct_contact,
            message,
            promise,
            abandon,
            exclution) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)'''


update_load = '''INSERT INTO resultado_icaro(
                        mis_dt,
                        service_name,
                        hour,
                        tot_agentes,
                        tot_accounts,
                        attempts,
                        conections,
                        direct_contact,
                        message,
                        promise,
                        exclution,
                        bucket,
                        start_hour,
                        end_hour,
                        trn_interval,
                        ov_number_dialed,
                        abandon) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'''