from unittest.mock import MagicMock
from src.controllers.receipecontroller import ReceipeController
from src.static.diets import Diet

@pytest.mark.unit
@patch("src.util.calculator")
def test_get_receipe_readiness_with_invalid_diet(calculate_readiness_mock):
    # test cases to get the readincess for a recipe that has wrong diet
    calculate_readiness_mock.return_value = 0
    controller = ReceipeController(items_dao=None)

    receipe = {
        "name": "cake",
        "diets": ["vegetarian"],
    }
    available_items = {
        "flour": 100,
        "egg": 50,
    }
    diet = Diet.VEGAN
    readiness = controller.get_receipe_readiness(receipe, available_items, diet)

    assert readiness is None


@pytest.mark.unit
@patch("src.util.calculator")
def test_get_receipe_readiness_with_valid_receipe_ingredients_available(calculate_readiness_mock):
    # test cases to get readiness for a valid recipe with necessary ingredients in the pantry
    calculate_readiness_mock.return_value = 0.5
    controller = ReceipeController(items_dao=None)

    receipe = {
        "name": "cake",
        "diets": ["vegetarian"],
    }
    available_items = {
        "flour": 100,
        "egg": 50,
    }

    diet = Diet.VEGETARIAN
    readiness = controller.get_receipe_readiness(receipe, available_items, diet)
    assert readiness == 0.5

@pytest.mark.unit
@patch("src.util.calculator")
def test_get_receipe_readiness_with_valid_receipe_ingredients_NOT_available(calculate_readiness_mock):
    # test cases to get readiness for a valid recipe with ingredients taht are not in the pantry
    calculate_readiness_mock.return_value = 0.05
    controller = ReceipeController(items_dao=None)

    receipe = {
        "name": "cake",
        "diets": ["vegetarian"],
    }
    available_items = {
        "flour": 100,
        "egg": 50,
    }

    diet = Diet.VEGETARIAN
    readiness = controller.get_receipe_readiness(receipe, available_items, diet)
    assert readiness is None