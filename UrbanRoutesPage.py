from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class UrbanRoutesPage:
    # Prueba 1 : colocar direcciones
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    call_taxi_button = (By.CSS_SELECTOR, '#root > div > div.workflow > div.workflow-subcontainer > div.type-picker.shown > div.results-container > div.results-text > button')

  
    # Prueba 2 : tarifa comfort
    # localizador para tarifa comfort
    comfort_tariff = (By.CSS_SELECTOR, '#root > div > div.workflow > div.workflow-subcontainer > div.tariff-picker.shown > div.tariff-cards > div:nth-child(5)')
    # Localizador para comfort extras
    comfort_extras = (
        By.CSS_SELECTOR, '#root > div > div.workflow > div.workflow-subcontainer > div.tariff-picker.shown > div.form > div.reqs.open > div.reqs-body > div.r.r-type-group > div > div.r-group-items > div:nth-child(2) > div > div.r-counter-label')

  
    #  Prueba 3:  colocar num de telefono
    #  localizador para colocar num de telefono
    phone_field = (By.CLASS_NAME, 'np-text')
    # localizador para pop up window del numero de telefono
    input_for_phone = (By.ID, 'phone')
    #enviar num de telefono
    button_send_phone_number = (By.CSS_SELECTOR, '#root > div > div.number-picker.open > div.modal > div.section.active > form > div.buttons > button')
    #escribir codigo, NO SE CAMBIO EL XPATH PORQUE HAY OTRO ID DE CODE.
    input_for_code = (By.XPATH, '/html/body/div/div/div[1]/div[2]/div[2]/form/div[1]/div[1]/input')
    #botón de comfirmar codigo
    button_confirm_code = (By.CSS_SELECTOR, '#root > div > div.number-picker.open > div.modal > div.section.active > form > div.buttons > button:nth-child(1)')

  
    #Prueba 4: introducir payment method
    #localizador para selecionar metodo de pago
    payment_method = (By.CSS_SELECTOR, '#root > div > div.workflow > div.workflow-subcontainer > div.tariff-picker.shown > div.form > div.pp-button.filled')
    #loc para agregar metodo de pago
    add_payment_method = (By.CSS_SELECTOR, '#root > div > div.payment-picker.open > div.modal > div.section.active > div.pp-selector > div.pp-row.disabled > div.pp-title')
    #input card number
    input_card_number = (By.ID, 'number')
    #inpunt card code NO SE CAMBIO EL XPATH PORQUE HAY OTRO ID DE CODE.
    input_card_code = (By.XPATH, '/html/body/div/div/div[2]/div[2]/div[2]/form/div[1]/div[2]/div[2]/div[2]/input')
    #afuera de la tarjeta
    outside_card = (By.CLASS_NAME, 'card-wrapper')
    #boton para agregar tarjeta
    add_card_button = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[2]/form/div[3]/button[1]')
    close_payment_method = (By.XPATH, '/html/body/div/div/div[2]/div[2]/div[1]/button')
    #forma de pago
    selected_payment_method = (By.CLASS_NAME, 'pp-value-text')

  
    #Prueba 5: escribir mensaje para el conductor
    #campo donde se escribe el mensaje
    input_write_comment = (By.ID, 'comment')

  
    #Prueba 6: pedir manta y pañuelos
    #toggle button manta y pañuelos
    blanket_toggle_button = (
        By.CSS_SELECTOR, '#root > div > div.workflow > div.workflow-subcontainer > div.tariff-picker.shown > div.form > div.reqs.open > div.reqs-body > div:nth-child(1) > div > div.r-sw > div')
    #toggle button activo manta y pañuelos
    blanket_toggle_button_on = (By.CSS_SELECTOR,
                                '#root > div > div.workflow > div.workflow-subcontainer > div.tariff-picker.shown > div.form > '
                                'div.reqs.open > div.reqs-body > div:nth-child(1) > div > div.r-sw > div > input')

  
    #Prueba 7 :  agregar 2 helados
    add_ice_cream_button = (By.CSS_SELECTOR,
                            '#root > div > div.workflow > div.workflow-subcontainer > div.tariff-picker.shown > div.form > div.reqs.open > div.reqs-body > div.r.r-type-group > div > div.r-group-items > div:nth-child(1) > div > div.r-counter > div > div.counter-plus')
    ice_cream_number = (By.CSS_SELECTOR,
                        '#root > div > div.workflow > div.workflow-subcontainer > div.tariff-picker.shown > div.form > div.reqs.open > div.reqs-body > div.r.r-type-group > div > div.r-group-items > div:nth-child(1) > div > div.r-counter > div > div.counter-value')

  
    #Prueba 8: aparece ventana emergente de buscando taxi
    #boton de buscar taxi
    search_taxi_button = (By.CLASS_NAME, 'smart-button-secondary')
    #Ventana emergente buscando taxi
    search_taxi_pop_up = (By.CSS_SELECTOR, '#root > div > div.order.shown > div.order-body > div.order-header > div > div.order-header-title')

  
    #Prueba 9:  información del conductor
    driver_information_pop_up = (By.CLASS_NAME, 'order-btn-rating')


  
    def __init__(self, driver):
        self.driver = driver

  
    # Prueba 1 :  Configurar la dirección.
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

    def wait_for_load_directions_input(self):
        WebDriverWait(self.driver, 2).until(expected_conditions.visibility_of_element_located(self.to_field))

    def wait_for_taxi_button(self):
        WebDriverWait(self.driver, 1).until(expected_conditions.visibility_of_element_located(self.call_taxi_button))



  
    # Prueba 2: Seleccionar tarifa comfort
    # selecciona tarifa comfort
    def select_comfort_tariff(self):
        self.driver.find_element(*self.comfort_tariff).click()

    # ubica extras de comfort
    def get_comfort_extras(self):
        return self.driver.find_element(*self.comfort_extras).text

    def wait_for_taxi_tariff(self):
        WebDriverWait(self.driver, 1).until(expected_conditions.visibility_of_element_located(self.comfort_tariff))



  
    # Prueba 3:  colocar numero de telefono
    # click en campo num de telefono
    def click_phone_field(self):
        self.driver.find_element(*self.phone_field).click()

    # escribir num de telefono
    def set_phone_number(self, phone):
        self.driver.find_element(*self.input_for_phone).send_keys(phone)

    # click en botón "siguiente"
    def click_continue_button(self):
        self.driver.find_element(*self.button_send_phone_number).click()

    # def para introducir codigo
    def add_phone_code(self, code):
        self.driver.find_element(*self.input_for_code).send_keys(code)

    # click en botón confirmar codigo
    def click_confirm_button(self):
        self.driver.find_element(*self.button_confirm_code).click()

    # devolver el valor del phone field
    def get_phone(self):
        return self.driver.find_element(*self.phone_field).text



  
    # Prueba 4: introducir payment method
    # click en seleccionar metodo de pago
    def click_payment_method(self):
        self.driver.find_element(*self.payment_method).click()

    # click agregar tarjeta
    def click_add_card(self):
        self.driver.find_element(*self.add_payment_method).click()

    # agregar num tarjeta
    def add_card_number(self, card_number):
        self.driver.find_element(*self.input_card_number).send_keys(card_number)

    # agregar card code
    def add_card_code(self, card_code):
        self.driver.find_element(*self.input_card_code).send_keys(card_code)

    # click fuera de los campos
    def click_outside_card_fields(self):
        self.driver.find_element(*self.outside_card).click()

    # click para guardar card
    def click_add_card_button(self):
        self.driver.find_element(*self.add_card_button).click()

    #devolver el valor del payment method seleccionado
    def get_payment_method_selected(self):
        return self.driver.find_element(*self.selected_payment_method).text

    # cerrar payment method

    def click_close_payment_method(self):
        self.driver.find_element(*self.close_payment_method).click()



  
    # Prueba 5: mensaje para el conductor
    # escribir mensaje para driver
    def add_driver_comment(self, comment):
        self.driver.find_element(*self.input_write_comment).send_keys(comment)

    # devolver el valor del input del comment
    def get_driver_comment(self):
        return self.driver.find_element(*self.input_write_comment).get_property('value')



  
    # Prueba 6 : pedir manta y pañuelos
    def click_blanket_toggle_button(self):
        self.driver.find_element(*self.blanket_toggle_button).click()

    def get_toggle_button_on(self):
        return self.driver.find_element(*self.blanket_toggle_button_on).get_property('value')



  
    # Prueba 7: agregar 2 helados
    def click_add_ice_cream(self):
        self.driver.find_element(*self.add_ice_cream_button).click()

    def get_ice_cream_number(self):
        return self.driver.find_element(*self.ice_cream_number).text




  
    # Prueba 8: esperar por taxi
    # click boton buscar taxi
    def click_search_taxi(self):
        self.driver.find_element(*self.search_taxi_button).click()

    # ventana emergente buscando taxi
    def get_taxi_status(self):
        return self.driver.find_element(*self.search_taxi_pop_up).text

    def wait_for_taxi_status(self):
        WebDriverWait(self.driver, 2).until(expected_conditions.visibility_of_element_located(self.search_taxi_pop_up))




  
    # Prueba 9: información del taxista
    # ventana emergente informacion del taxista
    def get_driver_information(self):
        return self.driver.find_element(*self.driver_information_pop_up).text

    def wait_for_driver_information(self):
        WebDriverWait(self.driver,40).until(
            expected_conditions.visibility_of_element_located(self.driver_information_pop_up))
