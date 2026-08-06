from core.business.finance.aura_finance_operations_layer_v01 import (

    AURAFinanceOperationsLayer

)

def test_finance_operations_layer():

    finance = AURAFinanceOperationsLayer()

    finance.record_transaction(

        "revenue",

        "Client payment",

        100000

    )

    finance.record_transaction(

        "expense",

        "Software costs",

        20000

    )

    summary = finance.calculate_summary()

    data = finance.get_finance_data()

    print(

        "AURA Finance Operations Layer Test"

    )

    print(

        "----------------------------------"

    )

    print(data)

    assert summary["revenue"] == (

        100000

    )

    assert summary["expenses"] == (

        20000

    )

    assert summary["profit"] == (

        80000

    )

if __name__ == "__main__":

    test_finance_operations_layer()