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