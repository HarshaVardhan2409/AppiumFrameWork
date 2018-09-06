

class BaseClass():
    
    altdriver = None
    driver = None


    def __init__(self, altdriver, driver):
        self.altdriver = altdriver
        self.driver = driver
        
    def start_game(self, game_name):
        self.altdriver.wait_for_element_where_name_contains(game_name).tap()
        
    def wait_for_scene(self, scene_name):
        self.altdriver.wait_for_current_scene_to_be(scene_name)
        
    def verify_scene(self, scene_name):
        assert scene_name in self.altdriver.get_current_scene()
        
    def verify_the_element_on_screen(self, element_name):
            self.altdriver.wait_for_element_where_name_contains(element_name)
            
    def get_object_location(self, object_name):
        x = self.altdriver.wait_for_element_where_name_contains(object_name).x
        y = self.altdriver.wait_for_element_where_name_contains(object_name).y
        value = {"x": x, "y": y}
        return value
    
    def get_object_name(self, object_name):
        value = self.altdriver.wait_for_element_where_name_contains(object_name).name
        return value

    def verify_question(self, object_name, question_number):
        name = self.get_object_name(question_number)
        assert question_number in name
    
    def verify_object_location(self, start_position, end_position, check_status):
        if 'same' in check_status:
            assert start_position == end_position
        elif 'different' in check_status:
            assert start_position != end_position
    