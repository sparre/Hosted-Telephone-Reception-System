# ${WIKI_URL}

from send_message import Test_Case
from config       import queued_reception as Reception

class Sequence_Diagram (Test_Case):
    def test_Run (self):
        try:
            self.Preconditions (Reception = Reception)

            self.Step (Message = "Receptionist-N     ->> Klient-N          [taster: navn]")