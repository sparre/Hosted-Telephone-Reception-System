# ${WIKI_URL}

from incoming_calls import Test_Case
from config         import queued_reception as Reception

class Sequence_Diagram (Test_Case):
    def test_Run (self):
        try:
            self.Preconditions (Reception = Reception)

            self.Step (Message = "Receptionist-N     ->> Klient-N          [genvejstast-ring-til-primaert-nummer]")
            self.Receptionist_Places_Call (Number = self.Callee.Number)
            self.Step (Message = "Call-Flow-Control  ->> FreeSWITCH        [ring-op: telefon-N, nummer]")
            self.Callee.Wait_For_Call ()
            self.Step (Message = "FreeSWITCH         ->> FreeSWITCH        [forbind opkald\nog telefon-N]")