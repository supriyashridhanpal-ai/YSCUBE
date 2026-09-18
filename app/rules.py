class RuleEngine:

    def check_hys_law(self, patient_data):
        """
        Placeholder for Hy's Law evaluation.

        Actual implementation should use:
        - ALT / AST
        - ULN
        - Total bilirubin
        - Time window
        - Alternative explanations
        """

        return {
            "meets_criteria": False,
            "reason": "Rule implementation pending protocol data.",
            "evidence": []
        }

    def check_wrong_dose(self, patient_data):
        """
        Placeholder for dose validation.
        """

        return {
            "wrong_dose": False,
            "reason": "Dose rule implementation pending protocol data.",
            "evidence": []
        }
