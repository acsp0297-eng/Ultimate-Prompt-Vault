import os, asyncio
from dotenv import load_dotenv
from temporalio.worker import Worker
from temporalio.client import Client
from workflows.workflows import OrderFulfillmentWorkflow
import activities.index as acts

load_dotenv()

async def main():
    address = os.getenv('TEMPORAL_ADDRESS', 'localhost:7233')
    namespace = os.getenv('TEMPORAL_NAMESPACE', 'uphigh-online')
    task_queue = os.getenv('TEMPORAL_TASK_QUEUE', 'uphigh-tq')

    client = await Client.connect(address, namespace=namespace)
    worker = Worker(
        client,
        task_queue=task_queue,
        workflows=[OrderFulfillmentWorkflow],
        activities=[
            acts.verify_payment,
            acts.assign_uid,
            acts.send_receipt,
            acts.log_to_crm,
            acts.wait_for_human_approval
        ]
    )
    print(f"[UPHIGH] Python worker on {task_queue}")
    await worker.run()

if __name__ == '__main__':
    asyncio.run(main())
