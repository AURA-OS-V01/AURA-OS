from agents.product.product_planner_v01 import (

    ProductPlanner

)

def test_product_planner():

    planner = ProductPlanner()

    result = planner.create_plan(

        "Create a fitness app for beginners"

    )

    print("Product Planner Test")

    print("--------------------")

    print(result)

if __name__ == "__main__":

    test_product_planner()