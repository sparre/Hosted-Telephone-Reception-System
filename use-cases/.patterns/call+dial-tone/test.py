# ${WIKI_URL}

from incoming_calls import Test_Case
from config         import queued_reception as Reception

class Sequence_Diagram (Test_Case):
    def test_Run (self):
        try:
            self.Preconditions (Reception = Reception)

            self.Step (Message = "Opkalder           ->> FreeSWITCH        [SIP: <reception PSTN>]")
            self.Step (Message = "FreeSWITCH         ->> Opkalder          [ringetone]")