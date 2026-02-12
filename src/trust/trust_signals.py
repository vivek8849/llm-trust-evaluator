# class TrustSignals:
#     """
#     Container for trust-related metrics and final trust computation.
#     """

#     def __init__(self, consistency_score=0.0, self_critique_score=0.0):
#         self.consistency_score = consistency_score
#         self.self_critique_score = self_critique_score
#         self.final_trust_score = 0.0

#     def compute_final_score(self):
#         """
#         Compute trust as stability penalized by vulnerability.
#         """
#         self.final_trust_score = (
#             self.consistency_score * (1 - self.self_critique_score)
#         )

#         return self.final_trust_score
# model trust as semantic stability penalized by self-identified vulnerability, using a multiplicative formulation to reflect compounded risk.

# Moved from linear model -> squared mode;

class TrustSignals:
    def __init__(self, consistency_score=0.0, vulnerability_score=0.0):
        self.consistency_score = consistency_score
        self.vulnerability_score = vulnerability_score
        self.final_trust_score = 0.0

    def compute_final_score(self):
        """
        Nonlinear vulnerability penalty.
        """
        penalty = 1 - (self.vulnerability_score ** 2)
        self.final_trust_score = self.consistency_score * penalty

        return self.final_trust_score