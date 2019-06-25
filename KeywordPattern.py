class KeywordPattern():

    def __init__(self):
        # [srcip,srcport,dstip,dstport]
        self.ruleset = ['', '', '', '']
        self.positionset = [0, 0, 0, 0]

    def setPositioSet(self, srcip, srcport, dstip, dstport):
        self.positionset = [srcip, srcport, dstip, dstport]

    def setRuleSet(self, srcip_expr, srcport_expr, dstip_expr, dstport_expr):
        self.ruleset = [srcip_expr, srcport_expr, dstip_expr, dstport_expr]