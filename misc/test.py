# pip install restnavigator
from restnavigator import Navigator

# The OSDI API entry point, listing the collections available
# View it in a browser: http://demo.osdi.io/hb2/browser.html#/api/v1
aep='http://demo.osdi.io/api/v1'

# Security is important.  The OSDI example server doesn't require a token.
# Others do so here's how to do it
api_token='foobar'

# Initialize the navigator with the AEP
rn= Navigator.hal(aep)

# Set the token
rn.headers['OSDI-API-Token']=api_token

# Navigate to the osdi:people collection from the AEP
# Then drill in to the osdi:people embedded in the response to the collection
# Stick the set of people that came back into a variable
people=rn['osdi:people']['osdi:people']

# Loop through the people, grab each persons state
for person in people:
    state=person.state

    # People have more than one email, grab them all
    emails = ''
    for email in state['email_addresses']:
        emails += email['address']

    #print a tab separated set of fields
    print state['given_name'], '\t', state['family_name'], '\t', emails
