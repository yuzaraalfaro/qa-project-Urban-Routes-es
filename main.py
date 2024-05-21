import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import data


# no modificar
def retrieve_phone_code(driver) -> str:
    """Este código devuelve un número de confirmación de teléfono y lo devuelve como un string.
    Utilízalo cuando la aplicación espere el código de confirmación para pasarlo a tus pruebas.
    El código de confirmación del teléfono solo se puede obtener después de haberlo solicitado en la aplicación."""

    import json
    import time
    from selenium.common import WebDriverException
    code = None
    for i in range(10):
        try:
            logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                    and 'api/v1/number?number' in log.get("message")]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
        except WebDriverException:
            time.sleep(1)
            continue
        if not code:
            raise Exception("No se encontró el código de confirmación del teléfono.\n"
                            "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu aplicación.")
        return code


class UrbanRoutesPage:
    # Prueba 1 : colocar direcciones
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    call_taxi_button = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[1]/div[3]/div[1]/button')

    # Prueba 2 : tarifa comfort
    # localizador para tarifa comfort
    comfort_tariff = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[1]/div[5]')
    # Localizador para comfort extras
    comfort_extras = (
        By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[2]/div/div[1]')

    #  Prueba 3:  colocar num de telefono
    #  localizador para colocar num de telefono
    phone_field = (By.CLASS_NAME, 'np-text')
    # localizador para pop up window del numero de telefono
    input_for_phone = (By.ID, 'phone')
    #enviar num de telefono
    button_send_phone_number = (By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[1]/form/div[2]/button')
    #escribir codigo
    input_for_code = (By.XPATH, '/html/body/div/div/div[1]/div[2]/div[2]/form/div[1]/div[1]/input')
    #botón de comfirmar codigo
    button_confirm_code = (By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[2]/form/div[2]/button[1]')

    #Prueba 4: introducir payment method
    #localizador para selecionar metodo de pago
    payment_method = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[2]')
    #loc para agregar metodo de pago
    add_payment_method = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[2]')
    #input card number
    input_card_number = (By.ID, 'number')
    #inpunt card code
    input_card_code = (By.XPATH, '/html/body/div/div/div[2]/div[2]/div[2]/form/div[1]/div[2]/div[2]/div[2]/input')
    #afuera de la tarjeta
    outside_card = (By.CLASS_NAME, 'card-wrapper')
    #boton para agregar tarjeta
    add_card_button = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[2]/form/div[3]/button[1]')
    close_payment_method = (By.XPATH, '/html/body/div/div/div[2]/div[2]/div[1]/button')


    #Prueba 5: escribir mensaje para el conductor
    #campo donde se escribe el mensaje
    input_write_comment = (By.ID, 'comment')


    #Prueba 6: pedir manta y pañuelos
    #toggle button manta y pañuelos
    blanket_toggle_button = (
        By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[1]/div/div[2]/div')
    #toggle button activo manta y pañuelos
    blanket_toggle_button_on = (By.CSS_SELECTOR,
                     '#root > div > div.workflow > div.workflow-subcontainer > div.tariff-picker.shown > div.form > '
                     'div.reqs.open > div.reqs-body > div:nth-child(1) > div > div.r-sw > div > input')


    #Prueba 7 :  agregar 2 helados
    add_ice_cream_button = (By.XPATH, '/html/body/div/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[1]/div/div[2]/div/div[3]')
    ice_cream_number = (By.XPATH, '/html/body/div/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[1]/div/div[2]/div/div[2]')


    #Prueba 8: aparece ventana emergente de buscando taxi
    #boton de buscar taxi
    search_taxi_button = (By.CLASS_NAME, 'smart-button-secondary')
    #Ventana emergente buscando taxi
    search_taxi_pop_up = (By.XPATH, '//*[@id="root"]/div/div[5]/div[2]/div[1]/div/div[1]')


    #Prueba 9:  información del conductor
    driver_information_pop_up = (By.XPATH, '//*[@id="root"]/div/div[5]/div[2]/div[2]/div[1]/div[1]/div[1]/div')



    def __init__(self, driver):
        self.driver = driver

    #Prueba 1 :  Configurar la dirección.
    def set_from(self, from_address):
        self.driver.find_element(*self.from_field).send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property(
            'value')  # obtiene el relleno que se escribió en el input to

    def set_route(self, from_address, to_address):
        self.set_from(from_address)
        self.set_to(to_address)

    def click_call_taxi(self):
        self.driver.find_element(*self.call_taxi_button).click()



    
    #Prueba 2: Seleccionar tarifa comfort

    #selecciona tarifa comfort
    def select_comfort_tariff(self):
        self.driver.find_element(*self.comfort_tariff).click()

    #ubica extras de comfort
    def get_comfort_extras(self):
        return self.driver.find_element(*self.comfort_extras).text



    
    #Prueba 3:  colocar numero de telefono

    #click en campo num de telefono
    def click_phone_field(self):
        self.driver.find_element(*self.phone_field).click()

    #escribir num de telefono
    def set_phone_number(self, phone):
        self.driver.find_element(*self.input_for_phone).send_keys(phone)

    #click en botón "siguiente"
    def click_continue_button(self):
        self.driver.find_element(*self.button_send_phone_number).click()

    #def para introducir codigo
    def add_phone_code(self, code):
        #time.sleep(1)
        self.driver.find_element(*self.input_for_code).send_keys(code)

    #click en botón confirmar codigo
    def click_confirm_button(self):
        self.driver.find_element(*self.button_confirm_code).click()

    # devolver el valor del input de phone
    def get_phone(self):
        return self.driver.find_element(*self.input_for_phone).get_property('value')



    
    #Prueba 4: introducir payment method
    #click en seleccionar metodo de pago
    def click_payment_method(self):
        self.driver.find_element(*self.payment_method).click()

    #click agregar tarjeta
    def click_add_card(self):
        self.driver.find_element(*self.add_payment_method).click()

    #agregar num tarjeta
    def add_card_number(self, card_number):
        self.driver.find_element(*self.input_card_number).send_keys(card_number)

    # agregar card code
    def add_card_code(self, card_code):
        self.driver.find_element(*self.input_card_code).send_keys(card_code)

    #click fuera de los campos
    def click_outside_card_fields(self):
        self.driver.find_element(*self.outside_card).click()

    #click para guardar card
    def click_add_card_button(self):
        self.driver.find_element(*self.add_card_button).click()

    # devolver el valor del input de card number
    def get_card_number(self):
        return self.driver.find_element(*self.input_card_number).get_property('value')

    # devolver el valor del input de card number
    def get_card_code(self):
        return self.driver.find_element(*self.input_card_code).get_property('value')

    # cerrar payment method

    def click_close_payment_method(self):
        self.driver.find_element(*self.close_payment_method).click()



    
    #Prueba 5: mensaje para el conductor

    #escribir mensaje para driver
    def add_driver_comment(self, comment):
        self.driver.find_element(*self.input_write_comment).send_keys(comment)

    #devolver el valor del input del comment
    def get_driver_comment(self):
        return self.driver.find_element(*self.input_write_comment).get_property('value')




    #Prueba 6 : pedir manta y pañuelos
    def click_blanket_toggle_button(self):
        self.driver.find_element(*self.blanket_toggle_button).click()

    def get_toggle_button_on(self):
        return self.driver.find_element(*self.blanket_toggle_button_on).get_property('value')




    #Prueba 7: agregar 2 helados
    def click_add_ice_cream(self):
        self.driver.find_element(*self.add_ice_cream_button).click()

    def get_ice_cream_number(self):
        return self.driver.find_element(*self.ice_cream_number).text




    #Prueba 8: esperar por taxi
    #click boton buscar taxi
    def click_search_taxi(self):
        self.driver.find_element(*self.search_taxi_button).click()

    #ventana emergente buscando taxi
    def get_taxi_status(self):
        return self.driver.find_element(*self.search_taxi_pop_up).text




    # Prueba 9: información del taxista
    # ventana emergente informacion del taxista
    def get_driver_information(self):
        return self.driver.find_element(*self.driver_information_pop_up).text




class TestUrbanRoutes:
    driver = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        from selenium.webdriver.chrome.options import Options as ChromeOptions
        chrome_options = ChromeOptions()
        chrome_options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(options=chrome_options)



    
    # Test de prueba 1
    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        time.sleep(1)
        routes_page.set_route(address_from,
                              address_to) 

        assert routes_page.get_from() == address_from  
        assert routes_page.get_to() == address_to
        time.sleep(2)
        routes_page.click_call_taxi()



    
    #Test de prueba 2
    def test_select_tariff(self):
        routes_page = UrbanRoutesPage(self.driver)
        time.sleep(2)

        routes_page.select_comfort_tariff()
        comfort_selected = routes_page.get_comfort_extras()

        #assert para verificar que se seleccionó la tarifa comfort
        assert comfort_selected == "Chocolate"



    
    #Test prueba 3
    def test_provide_phone_number(self):
        routes_page = UrbanRoutesPage(self.driver)
        phone_number = data.phone_number

        routes_page.click_phone_field()
        routes_page.set_phone_number(phone_number)
        time.sleep(1)

        routes_page.click_continue_button()
        time.sleep(1)
        code = retrieve_phone_code(driver=self.driver)
        routes_page.add_phone_code(code)
        time.sleep(1)
        routes_page.click_confirm_button()

        assert routes_page.get_phone() == phone_number



    
    #Test Prueba 4
    def test_payment_method(self):
        routes_page = UrbanRoutesPage(self.driver)
        card_number = data.card_number
        card_code = data.card_code

        routes_page.click_payment_method()
        routes_page.click_add_card()
        routes_page.add_card_number(card_number)
        routes_page.add_card_code(card_code)

        assert routes_page.get_card_number() == card_number
        assert routes_page.get_card_code() == card_code

        routes_page.click_outside_card_fields()
        routes_page.click_add_card_button()
        routes_page.click_close_payment_method()



    
    #Prueba 5
    def test_add_driver_comment(self):
        routes_page = UrbanRoutesPage(self.driver)
        driver_comment = data.message_for_driver

        time.sleep(1)
        routes_page.add_driver_comment(driver_comment)

        assert routes_page.get_driver_comment() == driver_comment



    
    #Prueba 6
    def test_blanket_selected(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_blanket_toggle_button()
        #toggle_button_on = routes_page.blanket_toggle_button_on

        assert routes_page.get_toggle_button_on() == 'on'



    
    #Prueba 7
    def test_add_ice_cream(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_add_ice_cream()
        time.sleep(2)
        routes_page.click_add_ice_cream()

        ice_cream_selected = routes_page.get_ice_cream_number()

        assert ice_cream_selected == '2'



    
    #Prueba 8
    def test_search_taxi(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_search_taxi()
        time.sleep(1)
        waiting_taxi = routes_page.get_taxi_status()

        assert waiting_taxi == 'Car search' #en inglés



    
    # Prueba 9
    def test_driver_information(self):
        routes_page = UrbanRoutesPage(self.driver)
        time.sleep(40)

        driver_information = routes_page.get_driver_information()

        assert driver_information == '4,9'  # en inglés


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
