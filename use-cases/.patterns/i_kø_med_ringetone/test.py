            self.Step (Message = "FreeSWITCH: checks dial-plan => to queue")
            self.Step (Message = "FreeSWITCH->Call-Flow-Control: call queued with dial-tone")
            self.Step (Message = "FreeSWITCH: pauses dial-plan processing for # seconds")
            Call_ID, Reception_ID = self.Call_Announced ()
            self.Step (Message = "Client-N->Receptionist-N: shows call (with dial-tone)")
