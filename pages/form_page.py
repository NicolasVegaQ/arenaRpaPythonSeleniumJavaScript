from selenium.webdriver.common.by import By

class form_page:
    def __init__(self, driver):
        self.driver = driver

    def start_challenge(self):
       button_start= self.driver.find_element(By.XPATH, "//a[normalize-space(text())='Iniciar Reto']")
       button_start.click()

    def fill_country(self,country):
        field_country = self.driver.find_element(By.ID,"pais")
        field_country.clear()
        field_country.send_keys(country)

    def fill_surname(self,surname):
        field_surname= self.driver.find_element(By.ID,"apellidos")
        field_surname.clear()
        field_surname.send_keys(surname)

    def fill_name(self,name):
        field_name = self.driver.find_element(By.ID,"nombres")
        field_name.clear()
        field_name.send_keys(name)

    def fill_email(self,email):
        field_email = self.driver.find_element(By.ID,"email")
        field_email.clear()
        field_email.send_keys(email)

    def fill_company(self,company):
        field_company = self.driver.find_element(By.ID,"empresa")
        field_company.clear()
        field_company.send_keys(company)

    def fill_numbre_phone(self,number_phone):
        field_number_phone = self.driver.find_element(By.ID,"numero")
        field_number_phone.clear()
        field_number_phone.send_keys(number_phone)

    def fill_web(self,web):
        field_web = self.driver.find_element(By.ID,"web")
        field_web.clear()
        field_web.send_keys(web)

    def send_form(self):
       button_send = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
       button_send.click()

    def fill_all_fields_fast(self, nombre, apellidos, pais, empresa, email, numero, web):
        script = """
            function setInputValue(id, value) {
                const input = document.getElementById(id);
                input.value = value;
                input.dispatchEvent(new Event('input', { bubbles: true }));
                input.dispatchEvent(new Event('change', { bubbles: true }));
            }

            setInputValue('nombres', arguments[0]);
            setInputValue('apellidos', arguments[1]);
            setInputValue('pais', arguments[2]);
            setInputValue('empresa', arguments[3]);
            setInputValue('email', arguments[4]);
            setInputValue('numero', arguments[5]);
            setInputValue('web', arguments[6]);
        """
        self.driver.execute_script(script, nombre, apellidos, pais, empresa, email, numero, web)

    def send_form_fast(self):
        self.driver.execute_script("""
            const button = document.querySelector("button[type='submit']");
            if (button) {
                button.click();
            } else {
                console.warn("Botón no encontrado");
            }
        """)

    def start_challenge_fast(self):
        self.driver.execute_script("""
            const link = Array.from(document.querySelectorAll('a'))
                .find(el => el.textContent.trim() === 'Iniciar Reto');
            if (link) {
                link.click();
            } else {
                console.warn("Enlace 'Iniciar Reto' no encontrado");
            }
        """)