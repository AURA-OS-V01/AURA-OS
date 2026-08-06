from core.agents.goals.aura_agent_goal_management_engine_v01 import (

    AURAAgentGoalManagementEngine

)

from core.agents.reasoning.aura_agent_planning_reasoning_engine_v01 import (

    AURAAgentPlanningReasoningEngine

)

from core.agents.autonomy.aura_autonomous_decision_agent_v01 import (

    AURAAutonomousDecisionAgent

)

from core.agents.safety.aura_agent_safety_governance_layer_v01 import (

    AURAAgentSafetyGovernanceLayer

)

from core.agents.actions.aura_agent_action_execution_engine_v01 import (

    AURAAgentActionExecutionEngine

)

from core.agents.optimization.aura_agent_self_optimization_engine_v01 import (

    AURAAgentSelfOptimizationEngine

)

def run_demo():

    print("\n==============================")

    print(" AURA Autonomous Demo v0.1 ")

    print("==============================\n")

    # Goal

    goals = AURAAgentGoalManagementEngine()

    goal = goals.create_goal(

        "sales_agent",

        "Acquire customers",

        "Find and convert new business leads"

    )

    print("🎯 Goal Created:")

    print(goal)

    # Planning

    planner = AURAAgentPlanningReasoningEngine()

    plan = planner.create_plan(

        goal["title"],

        "Research prospects and execute outreach"

    )

    planner.add_step(

        plan["id"],

        "Research companies"

    )

    planner.add_step(

        plan["id"],

        "Send outreach"

    )

    planner.finalize_plan(

        plan["id"]

    )

    print("\n🧠 Plan Created:")

    print(plan)

    # Decision

    decision_engine = AURAAutonomousDecisionAgent()

    decision = decision_engine.analyze_options(

        "Choose customer acquisition method",

        [

            {

                "action": "AI Email Outreach",

                "score": 90

            },

            {

                "action": "Manual Calling",

                "score": 60

            }

        ]

    )

    decision_result = decision_engine.choose_action(

        decision["id"]

    )

    print("\n⚡ Decision:")

    print(decision_result)

    # Safety

    safety = AURAAgentSafetyGovernanceLayer()

    safety.grant_permission(

        "sales_agent",

        "AI Email Outreach"

    )

    approval = safety.validate_action(

        "sales_agent",

        "AI Email Outreach"

    )

    print("\n🛡️ Safety Check:")

    print(approval)

    # Execute

    executor = AURAAgentActionExecutionEngine()

    action = executor.create_action(

        "sales_agent",

        "outreach",

        "AI Email Outreach"

    )

    result = executor.execute_action(

        action["id"]

    )

    print("\n⚙️ Action Result:")

    print(result)

    # Optimization

    optimizer = AURAAgentSelfOptimizationEngine()

    optimizer.record_performance(

        "sales_agent",

        "Customer acquisition",

        True,

        95

    )

    report = optimizer.analyze_performance(

        "sales_agent"

    )

    print("\n📈 Performance Report:")

    print(report)

    print("\n==============================")

    print(" AURA Demo Complete 🚀 ")

    print("==============================")

if __name__ == "__main__":

    run_demo()