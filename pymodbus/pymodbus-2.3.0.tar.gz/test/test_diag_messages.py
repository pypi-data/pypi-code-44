#!/usr/bin/env python
import unittest
from pymodbus.exceptions import *
from pymodbus.constants import ModbusPlusOperation
from pymodbus.diag_message import *
from pymodbus.diag_message import DiagnosticStatusRequest
from pymodbus.diag_message import DiagnosticStatusResponse
from pymodbus.diag_message import DiagnosticStatusSimpleRequest
from pymodbus.diag_message import DiagnosticStatusSimpleResponse

class SimpleDataStoreTest(unittest.TestCase):
    '''
    This is the unittest for the pymodbus.diag_message module
    '''

    def setUp(self):
        self.requests = [
            #(DiagnosticStatusRequest,                      b'\x00\x00\x00\x00'),
            #(DiagnosticStatusSimpleRequest,                b'\x00\x00\x00\x00'),
            (RestartCommunicationsOptionRequest,            b'\x00\x01\x00\x00', b'\x00\x01\xff\x00'),
            (ReturnDiagnosticRegisterRequest,               b'\x00\x02\x00\x00', b'\x00\x02\x00\x00'),
            (ChangeAsciiInputDelimiterRequest,              b'\x00\x03\x00\x00', b'\x00\x03\x00\x00'),
            (ForceListenOnlyModeRequest,                    b'\x00\x04\x00\x00', b'\x00\x04'),
            (ReturnQueryDataRequest,                        b'\x00\x00\x00\x00', b'\x00\x00\x00\x00'),
            (ClearCountersRequest,                          b'\x00\x0a\x00\x00', b'\x00\x0a\x00\x00'),
            (ReturnBusMessageCountRequest,                  b'\x00\x0b\x00\x00', b'\x00\x0b\x00\x00'),
            (ReturnBusCommunicationErrorCountRequest,       b'\x00\x0c\x00\x00', b'\x00\x0c\x00\x00'),
            (ReturnBusExceptionErrorCountRequest,           b'\x00\x0d\x00\x00', b'\x00\x0d\x00\x00'),
            (ReturnSlaveMessageCountRequest,                b'\x00\x0e\x00\x00', b'\x00\x0e\x00\x00'),
            (ReturnSlaveNoResponseCountRequest,             b'\x00\x0f\x00\x00', b'\x00\x0f\x00\x00'),
            (ReturnSlaveNAKCountRequest,                    b'\x00\x10\x00\x00', b'\x00\x10\x00\x00'),
            (ReturnSlaveBusyCountRequest,                   b'\x00\x11\x00\x00', b'\x00\x11\x00\x00'),
            (ReturnSlaveBusCharacterOverrunCountRequest,    b'\x00\x12\x00\x00', b'\x00\x12\x00\x00'),
            (ReturnIopOverrunCountRequest,                  b'\x00\x13\x00\x00', b'\x00\x13\x00\x00'),
            (ClearOverrunCountRequest,                      b'\x00\x14\x00\x00', b'\x00\x14\x00\x00'),
            (GetClearModbusPlusRequest,                     b'\x00\x15\x00\x00', b'\x00\x15\x00\x00' + b'\x00\x00' * 55),
        ]

        self.responses = [
            #(DiagnosticStatusResponse,                     b'\x00\x00\x00\x00'),
            #(DiagnosticStatusSimpleResponse,               b'\x00\x00\x00\x00'),
            (ReturnQueryDataResponse,                      b'\x00\x00\x00\x00'),
            (RestartCommunicationsOptionResponse,          b'\x00\x01\x00\x00'),
            (ReturnDiagnosticRegisterResponse,             b'\x00\x02\x00\x00'),
            (ChangeAsciiInputDelimiterResponse,            b'\x00\x03\x00\x00'),
            (ForceListenOnlyModeResponse,                  b'\x00\x04'),
            (ReturnQueryDataResponse,                      b'\x00\x00\x00\x00'),
            (ClearCountersResponse,                        b'\x00\x0a\x00\x00'),
            (ReturnBusMessageCountResponse,                b'\x00\x0b\x00\x00'),
            (ReturnBusCommunicationErrorCountResponse,     b'\x00\x0c\x00\x00'),
            (ReturnBusExceptionErrorCountResponse,         b'\x00\x0d\x00\x00'),
            (ReturnSlaveMessageCountResponse,              b'\x00\x0e\x00\x00'),
            (ReturnSlaveNoReponseCountResponse,            b'\x00\x0f\x00\x00'),
            (ReturnSlaveNAKCountResponse,                  b'\x00\x10\x00\x00'),
            (ReturnSlaveBusyCountResponse,                 b'\x00\x11\x00\x00'),
            (ReturnSlaveBusCharacterOverrunCountResponse,  b'\x00\x12\x00\x00'),
            (ReturnIopOverrunCountResponse,                b'\x00\x13\x00\x00'),
            (ClearOverrunCountResponse,                    b'\x00\x14\x00\x00'),
            (GetClearModbusPlusResponse,                   b'\x00\x15\x00\x04' + b'\x00\x00' * 55),
        ]

    def tearDown(self):
        ''' Cleans up the test environment '''
        del self.requests
        del self.responses

    def testDiagnosticRequestsDecode(self):
        ''' Testing diagnostic request messages encoding '''
        for msg,enc,exe in self.requests:
            handle = DiagnosticStatusRequest()
            handle.decode(enc)
            self.assertEqual(handle.sub_function_code, msg.sub_function_code)

    def testDiagnosticSimpleRequests(self):
        ''' Testing diagnostic request messages encoding '''
        request = DiagnosticStatusSimpleRequest(b'\x12\x34')
        request.sub_function_code = 0x1234
        self.assertRaises(NotImplementedException, lambda: request.execute())
        self.assertEqual(request.encode(), b'\x12\x34\x12\x34')

        response = DiagnosticStatusSimpleResponse(None)

    def testDiagnosticResponseDecode(self):
        ''' Testing diagnostic request messages encoding '''
        for msg,enc,exe in self.requests:
            handle = DiagnosticStatusResponse()
            handle.decode(enc)
            self.assertEqual(handle.sub_function_code, msg.sub_function_code)

    def testDiagnosticRequestsEncode(self):
        ''' Testing diagnostic request messages encoding '''
        for msg,enc,exe in self.requests:
            self.assertEqual(msg().encode(), enc)

    #def testDiagnosticResponse(self):
    #    ''' Testing diagnostic request messages '''
    #    for msg,enc in self.responses:
    #        self.assertEqual(msg().encode(), enc)

    def testDiagnosticExecute(self):
        ''' Testing diagnostic message execution '''
        for message, encoded, executed in self.requests:
            encoded = message().execute().encode()
            self.assertEqual(encoded, executed)

    def testReturnQueryDataRequest(self):
        ''' Testing diagnostic message execution '''
        message = ReturnQueryDataRequest([0x0000]*2)
        self.assertEqual(message.encode(), b'\x00\x00\x00\x00\x00\x00');
        message = ReturnQueryDataRequest(0x0000)
        self.assertEqual(message.encode(), b'\x00\x00\x00\x00');

    def testReturnQueryDataResponse(self):
        ''' Testing diagnostic message execution '''
        message = ReturnQueryDataResponse([0x0000]*2)
        self.assertEqual(message.encode(), b'\x00\x00\x00\x00\x00\x00');
        message = ReturnQueryDataResponse(0x0000)
        self.assertEqual(message.encode(), b'\x00\x00\x00\x00');

    def testRestartCommunicationsOption(self):
        ''' Testing diagnostic message execution '''
        request = RestartCommunicationsOptionRequest(True);
        self.assertEqual(request.encode(), b'\x00\x01\xff\x00')
        request = RestartCommunicationsOptionRequest(False);
        self.assertEqual(request.encode(), b'\x00\x01\x00\x00')

        response = RestartCommunicationsOptionResponse(True);
        self.assertEqual(response.encode(), b'\x00\x01\xff\x00')
        response = RestartCommunicationsOptionResponse(False);
        self.assertEqual(response.encode(), b'\x00\x01\x00\x00')

    def testGetClearModbusPlusRequestExecute(self):
        ''' Testing diagnostic message execution '''
        request = GetClearModbusPlusRequest(data=ModbusPlusOperation.ClearStatistics);
        response = request.execute()
        self.assertEqual(response.message, ModbusPlusOperation.ClearStatistics)

        request = GetClearModbusPlusRequest(data=ModbusPlusOperation.GetStatistics);
        response = request.execute()
        resp = [ModbusPlusOperation.GetStatistics]
        self.assertEqual(response.message, resp+[0x00] * 55)

#---------------------------------------------------------------------------#
# Main
#---------------------------------------------------------------------------#
if __name__ == "__main__":
    unittest.main()
