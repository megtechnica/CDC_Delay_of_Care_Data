
def isolate_total_stub(data):
    isolated_data = data[data.STUB_NAME == 'Total']
    isolated_data = isolated_data[['YEAR', 'ESTIMATE','STUB_NAME','AGE','PANEL']]
    return isolaed_total_stub
