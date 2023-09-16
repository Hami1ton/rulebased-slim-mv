from pathlib import Path
import zen
import os


class PointRuleEngine:
    def __init__(self):
        # load rules
        print("Rule Loading...")
        RULE_ASSET_FILE = os.path.join(Path(__file__).resolve().parent.parent.parent, './asset/Name.json')
        with open(RULE_ASSET_FILE, "r") as f:
            content = f.read()
        self.engine = zen.ZenEngine()
        self.decision = self.engine.create_decision(content)
        result = self.decision.evaluate({"input": 15})
        print("Rule Load Completed!")

    def calculate_point(self):
        result = self.decision.evaluate({"input": 15})
        return result


point_engine = PointRuleEngine()
