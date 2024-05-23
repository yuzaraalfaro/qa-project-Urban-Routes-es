from selenium import webdriver
import UrbanRoutesPage
import data
import helpers


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
        routes_page = UrbanRoutesPage.UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to

        # espera para cargar los inputs de la pagina
        routes_page.wait_for_load_directions_input()

        routes_page.set_route(address_from,
                              address_to)  

        assert routes_page.get_from() == address_from  
        assert routes_page.get_to() == address_to

        # espera para cargar el boton de llamar taxi
        routes_page.wait_for_taxi_button()

        routes_page.click_call_taxi()



    
    #Test de prueba 2
    def test_select_tariff(self):
        routes_page = UrbanRoutesPage.UrbanRoutesPage(self.driver)

        # espera para cargar las tarifas de taxi
        routes_page.wait_for_taxi_tariff()

        routes_page.select_comfort_tariff()
        comfort_selected = routes_page.get_comfort_extras()

        #assert para verificar que se seleccionó la tarifa comfort
        assert comfort_selected == "Chocolate"



    
    #Test prueba 3
    def test_provide_phone_number(self):
        routes_page = UrbanRoutesPage.UrbanRoutesPage(self.driver)
        phone_number = data.phone_number

        routes_page.click_phone_field()
        routes_page.set_phone_number(phone_number)
        routes_page.click_continue_button()

        code = helpers.retrieve_phone_code(driver=self.driver)
        routes_page.add_phone_code(code)
        routes_page.click_confirm_button()
        assert routes_page.get_phone() == phone_number



    
    #Test Prueba 4
    def test_payment_method(self):
        routes_page = UrbanRoutesPage.UrbanRoutesPage(self.driver)
        card_number = data.card_number
        card_code = data.card_code

        routes_page.click_payment_method()
        routes_page.click_add_card()
        routes_page.add_card_number(card_number)
        routes_page.add_card_code(card_code)

        routes_page.click_outside_card_fields()
        routes_page.click_add_card_button()
        routes_page.click_close_payment_method()

        assert routes_page.get_payment_method_selected() == "Card"



    
    #Prueba 5
    def test_add_driver_comment(self):
        routes_page = UrbanRoutesPage.UrbanRoutesPage(self.driver)
        driver_comment = data.message_for_driver

        routes_page.add_driver_comment(driver_comment)

        assert routes_page.get_driver_comment() == driver_comment




    
    #Prueba 6
    def test_blanket_selected(self):
        routes_page = UrbanRoutesPage.UrbanRoutesPage(self.driver)
        routes_page.click_blanket_toggle_button()

        assert routes_page.get_toggle_button_on() == 'on'




    
    #Prueba 7

    def test_add_ice_cream(self):
        routes_page = UrbanRoutesPage.UrbanRoutesPage(self.driver)
        routes_page.click_add_ice_cream()

        routes_page.click_add_ice_cream()

        ice_cream_selected = routes_page.get_ice_cream_number()

        assert ice_cream_selected == '2'



    
    #Prueba 8
    def test_search_taxi(self):
        routes_page = UrbanRoutesPage.UrbanRoutesPage(self.driver)
        routes_page.click_search_taxi()

        routes_page.wait_for_taxi_status()

        waiting_taxi = routes_page.get_taxi_status()

        assert waiting_taxi == 'Car search'  #en inglés




    
    # Prueba 9
    def test_driver_information(self):
        routes_page = UrbanRoutesPage.UrbanRoutesPage(self.driver)

        routes_page.wait_for_driver_information()

        driver_information = routes_page.get_driver_information()

        assert driver_information == '4,9'  


    
    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
