            self.Step (Message = "Receptionist-N     ->> Klient-N          [genvejstast-stil-igennem]")
            self.Step (Message = "Klient-N           ->> Call-Flow-Control [stil-igennem]")
            self.Step (Message = "Klient-N           ->> Klient-N          [ny tilstand:\nledig]")
            self.Step (Message = "Call-Flow-Control  ->> FreeSWITCH        [connect: incoming, outgoing]")
            self.Step (Message = "FreeSWITCH         ->> Telefon-N         [SIP: hang-up]")
            self.Step (Message = "FreeSWITCH         ->> Call-Flow-Control [free: telefon-N]")
            self.Step (Message = "FreeSWITCH         ->> FreeSWITCH        [connect: incoming, outgoing]")

            self.Postprocessing ()
        except:
            self.Postprocessing ()
            raise

