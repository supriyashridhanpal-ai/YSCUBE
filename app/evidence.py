class EvidenceValidator:

    def __init__(self, graph):
        self.graph = graph

    def record_exists(self, record_ref):
        domain = record_ref.get("domain")
        usubjid = record_ref.get("usubjid")
        seq = record_ref.get("seq")

        records = self.graph.data.get(domain, [])

        for record in records:
            if record.get("USUBJID") != usubjid:
                continue

            if seq is None or str(record.get("SEQ")) == str(seq):
                return True

        return False

    def validate(self, evidence):
        valid = []

        for record_ref in evidence:
            if self.record_exists(record_ref):
                valid.append(record_ref)

        return valid
