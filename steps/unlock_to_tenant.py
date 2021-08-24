from behave import then


@then("a porta será aberta e o inquilino estará com entrada permitida")
def then_should_be_unlock_door_to_tenant(context):
    waiting_tenants, tenants_in = context.condominium.unlock_to_tenants()
    length_tenants_in = len(set(map(lambda x: x['id'], tenants_in)))

    assert len(waiting_tenants) == 0
    assert length_tenants_in == 1

