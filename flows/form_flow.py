from pages.form_page import form_page
import time
def run_form(diver, table, fast=False):
    form = form_page(diver)
    form.start_challenge_fast()
    for index, row in table.iterrows():
        if fast:
            form.fill_all_fields_fast(
                nombre=row["Nombres"],
                apellidos=row["Apellidos"],
                pais=row["Pais"],
                empresa=row["Empresa"],
                email=row["Email"],
                numero=row["Numero"],
                web=row["Web"]
            )
            form.send_form_fast()

        
        else:
            form.fill_company(row["Empresa"])
            form.fill_country(row["Pais"])
            form.fill_email(row["Email"])
            form.fill_name(row["Nombres"])
            form.fill_numbre_phone(row["Numero"])
            form.fill_surname(row["Apellidos"])
            form.fill_web(row["Web"])
            form.send_form()