from behave import then


@then("ela deverá ser classificada como inquilino")
def then_person_should_be_classified_as_tenant(context):
    tenants = context.condominium.classify_recognized_people()[0]
    assert len(tenants) == 1


@then("ela deverá ser classificada como visitante")
def then_person_should_be_classified_as_visitor(context):
    visitors = context.condominium.classify_recognized_people()[1]
    assert len(visitors) == 1
