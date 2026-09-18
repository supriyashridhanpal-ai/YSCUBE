class Atlas:

    def __init__(self, graph):
        self.graph = graph

    def answer(self, question):
        text = question.lower()

        if "patient" in text or "subject" in text:
            return self.patient_query(question)

        if "hy" in text:
            return self.hys_law_query(question)

        if "dose" in text:
            return self.dose_query(question)

        return {
            "answer": "I need more information to answer this question.",
            "evidence": [],
            "confidence": 0.0
        }

    def patient_query(self, question):
        return {
            "answer": "Patient 360 query detected.",
            "evidence": [],
            "confidence": 0.5
        }

    def hys_law_query(self, question):
        return {
            "answer": "Hy's Law query detected.",
            "evidence": [],
            "confidence": 0.5
        }

    def dose_query(self, question):
        return {
            "answer": "Dose query detected.",
            "evidence": [],
            "confidence": 0.5
        }
