from behave import given, when, then

from src.condominium import Condominium
from src.environment import Environment
from src.utils import get_encoded_photo_by_name


@given("o ambiente foi configurado corretamente")
def given_successfully_environment_loading(context):
    environment = Environment()
    context.condominium = Condominium(environment)

    assert context.condominium.get_settings() is not None


@when("a foto {person_photo} for capturada")
def when_photo_is_captured(context, person_photo):
    context.person_photo = person_photo
    assert True


@then("a pessoa deverá ser reconhecida")
def then_person_should_be_recognized(context):
    encoded_photo = get_encoded_photo_by_name(context.person_photo)
    person = context.condominium.recognize_person(encoded_photo)
    context.condominium.add_recognized_person(person)
    assert person is not None


@then("a pessoa não deverá ser reconhecida")
def then_person_should__not_be_recognized(context):
    encoded_photo = get_encoded_photo_by_name(context.person_photo)
    person = context.condominium.recognize_person(encoded_photo)
    assert person is None
