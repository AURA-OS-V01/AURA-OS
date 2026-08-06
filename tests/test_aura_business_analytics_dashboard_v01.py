from core.business.analytics.aura_business_analytics_dashboard_v01 import (

    AURABusinessAnalyticsDashboard

)

def test_business_analytics_dashboard():

    dashboard = AURABusinessAnalyticsDashboard()

    dashboard.record_metric(

        "sales",

        "customers_acquired",

        25

    )

    dashboard.record_metric(

        "sales",

        "revenue_generated",

        50000

    )

    report = dashboard.generate_report(

        "sales"

    )

    data = dashboard.get_dashboard_data()

    print(

        "AURA Business Analytics Dashboard Test"

    )

    print(

        "-------------------------------------"

    )

    print(data)

    print(report)

    assert report["total"] == 50025

    assert report["metric_count"] == 2

if __name__ == "__main__":

    test_business_analytics_dashboard()
    