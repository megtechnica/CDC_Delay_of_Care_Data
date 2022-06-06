
def isolate_total_stub(data):
    isolated_data = data[data.STUB_NAME == 'Total']
    isolated_data = isolated_data[['YEAR', 'ESTIMATE','STUB_NAME','AGE','PANEL']]
    return isolated_data

def isolate_age_stub(data):
    isolated_data = data[data.STUB_NAME == 'Total']
    return isolated_data

