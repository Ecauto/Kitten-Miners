import base64, codecs
magic = '77u/IyBNaW5lcjMgQnkgTWF0eGQvSXppa3V0DQojVXBkYXRlIFNvb24gKE9uIGEgbWl0IHJhbmRvbSBvbiBhdmFpdCBsYSBmbGVtbWUgZGUgbGUgZmluaXIgbWRyKQ0KI3NyeSB3aHlub3QNCg0KaW1wb3J0IG9zDQppbXBvcnQgb3MNCmltcG9ydCBzeXMNCmZyb20gY29sb3JhbWEgaW1wb3J0IEZvcmUNCmltcG9ydCB0aW1lDQppbXBvcnQgc2VjcmV0cw0KZnJvbSByYW5kb20gaW1wb3J0IHJhbmRpbnQNCg0Kb3Muc3lzdGVtKCJ0aXRsZSBLaXR0ZW4gTWluZXIgKEJ5IEl6aWt1dCkiKQ0KICAgIA0KaWYgc3lzLnBsYXRmb3JtLmxvd2VyKCkgPT0gIndpbjMyIjogDQogICAgb3Muc3lzdGVtKCdjb2xvcicpDQoNCnByaW50KCkNCnByaW50KEZvcmUuTElHSFRNQUdFTlRBX0VYICsgJyQkXCAgICQkXCAkJFwgICAkJFwgICAgICQkXCAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAkJFwgICAgICAkJFwgJCRcICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAnKQ0KcHJpbnQoRm9yZS5MSUdIVE1BR0VOVEFfRVggKyAnJCQgfCAkJCAgfFxfX3wgICQkIHwgICAgJCQgfCAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICQkJFwgICAgJCQkIHxcX198ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICcpDQpwcmludChGb3JlLkxJR0hUTU'
love = 'SUEH5HDI9SJPNeVPpxWPO8WPDtVP8tWPEpVPDxWPDxWSjtWPDxWPDxKPNtVPNxWPDxWPEpVPNxWPDxWPDxKPNtVPNtVPNtWPDxWSjtVPDxWPDtsPDxKPNxWPDxWPDxKPNtVPDxWPDxWSjtVPNxWPDxWPEpVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtWlxAPaOlnJ50XRMipzHhGRyUFSEADHqSGyEOK0ILVPftWlDxWPDxVPNiVPNxWPO8KS8xWPNtK3kpKlDxVPOssPNtWPDtVS9sWPEpVPDxVPOsKlDxKPNtVPNtVPNxWSjxWSjxWPNxWPO8WPDtsPDxVPOsKlDxKPNxWPNtK18xWSjtWPDtVS9sWPEpVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNaXD0XpUWcoaDbEz9lMF5ZFHqVIR1OE0IBIRSsEIttXlNaWPDtVPDxCPNtVPDxVUjtVPDxVUjtVPNtWPDtsPNtVPNxWPDxWPDxWPO8WPDtsPNtWPDtsPNtVPNtVPDxVSjxWPDtVPDxVUjxWPO8WPDtsPNtWPDtsPDxWPDxWPDxVUjxWPO8VPOpK198VPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPpcQDcjpzyhqPuTo3WyYxkWE0uHGHSUEH5HDI9SJPNeVPpxWPO8KPDxKPNtWPDtsPNtWPDtsPDxKPNxWPO8WPEpVPDxVPNtK19sK3jxWPO8VPNxWPO8VPNtVPNtWPDtsSjxVPNiWPDtsPDxVUjxWPO8VPNxWPO8WPDtVPOsK19ssPDxVUjtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtWlxAPaOlnJ50XRMipzHhGRyU'
god = 'SFRNQUdFTlRBX0VYICsgJyQkIHwgXCQkXCAkJCB8ICBcJCQkJCAgfFwkJCQkICB8XCQkJCQkJCRcICQkIHwgICQkIHwgICAgICAkJCB8IFxfLyAkJCB8JCQgfCQkIHwgICQkIHxcJCQkJCQkJFwgJCQgfCAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgJykNCnByaW50KEZvcmUuTElHSFRNQUdFTlRBX0VYICsgJyQkIHwgXCQkXCAkJCB8ICBcJCQkJCAgfFwkJCQkICB8XCQkJCQkJCRcICQkIHwgICQkIHwgICAgICAkJCB8IFxfLyAkJCB8JCQgfCQkIHwgICQkIHxcJCQkJCQkJFwgJCQgfCAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgJykNCnByaW50KEZvcmUuTElHSFRNQUdFTlRBX0VYICsgJ1xfX3wgIFxfX3xcX198ICAgXF9fX18vICBcX19fXy8gIFxfX19fX19ffFxfX3wgIFxfX3wgICAgICBcX198ICAgICBcX198XF9ffFxfX3wgIFxfX3wgXF9fX19fX198XF9ffCAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAnKQ0KcHJpbnQoKQ0KcHJpbnQoKQ0KYWRyZXNzID0gaW5wdXQoRm9yZS5MSUdIVE1BR0VOVEFfRVggKyAnPiBFVEggYWRyZXNzIDonKQ0KDQpjb250aW51aW5nID0gVHJ1ZQ0KDQpidGN2YWwgPSAxODY4LjI2DQoNCndoaWxlIFRydWU6DQogIGlmIGNvbnRpbnVpbmcgPT0gVHJ1ZToNCiAgICB0aW1lLnNsZWVwKDAuMjUpDQogICAgcmFuSW50ID0gcm'
destiny = 'ShMTyhqPtkZQNjZQNfZwNjZQNjXD0XVPNtVTyzVUWuoxyhqPN8CFNkBt0XVPNtVPNtpzShMT9gDyEQVQ0tpzShMTyhqPtkYQRjXF8kZQNAPvNtVPNtVUOlnJ50XRMipzHhL3yuovNeVPWoVvNeVRMipzHhE1WSEH4tXlNvD2uyL2gcozptFTSmnPVtXlOTo3WyYxWZIHHtXlNvKFNvXlOTo3WyYxqFEHIBVPftp2IwpzI0pl50o2gyoy9bMKtbZwVcVPftEz9lMF5PGSISVPftVvN+VPVtXlOmqUVbpzShMT9gDyEQXFNeVPVtEIEVVPtxVvNeVUA0pvtvrmbfsFVhMz9loJS0XUWiqJ5xXTW0L3MuoPclLJ5xo21PIRZfZvxcXFNeVPVcVvxAPvNtVPNtVTShp3qypvN9VTyhpUI0XRMipzHhI0uWIRHtXlNvCvOKo3IfMPO5o3HtoTyeMFO0olOwo250nJ51MG8tXPVtXlOTo3WyYxqFEHIBVPftVyxvVPftEz9lMF5KFRyHEFNeVPViVvNeVRMipzHhHxIRVPftVx4vVPftEz9lMF5KFRyHEFNeVPVcVvxAPvNtVPNtVTyzVTShp3qypv5fo3qypvtcVQ09VPW5VwbAPvNtVPNtVPNtL29hqTyhqJyhMlN9VSElqJHAPvNtVPNtVTIfp2H6QDbtVPNtVPNtL29hqTyhqJyhMlN9VRMuoUAyQDbtVPNtMJkmMGbAPvNtVPNtVUOlnJ50XRMipzHhDxkIEFNeVPWoVvNeVRMipzHhI0uWIRHtXlNvD2uyL2gcozptFTSmnPVtXlOTo3WyYxWZIHHtXlNvKFNvVPftEz9lMF5FEHDtXlOmMJAlMKEmYaEin2IhK2uyrPtlZvxtXlOTo3WyYyqVFIESVPftVvN9VvNeVRMipzHhHxIRVPftVvNjYwNjVRIHFPNbWQNhZQNcVvxAPvNtMJkmMGbAPvNtVPOvpzIunj0XVPNAPt0X'
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))
