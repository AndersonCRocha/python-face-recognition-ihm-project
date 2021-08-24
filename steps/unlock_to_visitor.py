from behave import then


@then("a porta será aberta e o visitante estará com entrada permitida")
def then_should_be_unlock_door_to_visitor(context):
    waiting_visitors, visitors_in = context.condominium.unlock_to_visitors()
    length_visitors_in = len(set(map(lambda x: x['id'], visitors_in)))

    print('waiting_visitors', waiting_visitors)
    print('Visitors_in', visitors_in)
    assert len(waiting_visitors) == 0
    assert length_visitors_in == 1

