from restnavigator import Navigator

aep='http://demo.osdi.io/api/v1'
api_token='foobar'
rn= Navigator.hal(aep)
rn.headers['OSDI-API-Token']=api_token
people=rn['osdi:people']['osdi:people']
for person in people:
    state=person.state
    emails = ''
    for email in state['email_addresses']:
        emails += email['address']
    print state['given_name'], '\t', state['family_name'], '\t', emails
