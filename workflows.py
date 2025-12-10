from temporalio import workflow
from temporalio.common import RetryPolicy

with workflow.unsafe.imports_passed_through():
    from activities.index import verify_payment, assign_uid, send_receipt, log_to_crm, wait_for_human_approval

@workflow.defn
class OrderFulfillmentWorkflow:
    @workflow.run
    async def run(self, input: dict):
        try:
            verified = await workflow.execute_activity(
                verify_payment, input,
                start_to_close_timeout=300, heartbeat_timeout=30,
                retry_policy=RetryPolicy(maximum_attempts=3)
            )
            approval = True
            if not verified.get('autoApproved', True):
                approval = await workflow.execute_activity(
                    wait_for_human_approval, {"orderId": input["orderId"], "reason": verified.get("reason")},
                    start_to_close_timeout=3600
                )
            if not approval:
                raise RuntimeError("Order not approved")
            uid = await workflow.execute_activity(
                assign_uid, {"userId": input["userId"], "system": input.get("system","UltraPanda")},
                start_to_close_timeout=120
            )
            await workflow.execute_activity(
                send_receipt, {"orderId": input["orderId"], "uid": uid, "amount": input["amount"]},
                start_to_close_timeout=120
            )
            await workflow.execute_activity(
                log_to_crm, {"orderId": input["orderId"], "userId": input["userId"], "status":"fulfilled"},
                start_to_close_timeout=120
            )
            return {"status":"completed","uid": uid}
        except Exception as e:
            await workflow.execute_activity(
                log_to_crm, {"orderId": input["orderId"], "userId": input["userId"], "status":"needs_refund", "reason": str(e)},
                start_to_close_timeout=120
            )
            raise
