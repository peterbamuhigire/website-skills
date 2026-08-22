import json
import unittest
from pathlib import Path


class ApprovalAdapterTests(unittest.TestCase):
    def test_adapter_declares_fail_closed_actions(self):
        payload = json.loads((Path(__file__).parents[1] / "docs" / "approval-adapter.json").read_text(encoding="utf-8"))
        self.assertEqual(payload["engine"], "website")
        self.assertGreaterEqual(len(payload["actions"]), 6)
        self.assertIn("website.publish", {item["action_type"] for item in payload["actions"]})
        for action in payload["actions"]:
            if action["class"] in {"L2", "L3"}:
                self.assertTrue(action["preview_required"] and action["idempotency_required"])
                self.assertTrue(action["rollback"] and action["verification"])


if __name__ == "__main__":
    unittest.main()
