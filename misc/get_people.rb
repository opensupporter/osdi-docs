# gem install hyperclient
require 'hyperclient'

# The OSDI API entry point, listing the collections available
# View it in a browser: http://demo.osdi.io/hb2/browser.html#/api/v1
# Initialize the navigator with the AEP
osdi=Hyperclient.new('http://demo.osdi.io/api/v1')

# Security is important.  The OSDI example server doesn't require a token.
# Others do so here's how to do it
osdi.headers.update('OSDI-API-Token' => 'foobar')

# Navigate to the osdi:people collection from the AEP and get the people collection
people=osdi['osdi:people']

# Loop through the people, grab each persons state
people.each do |person|

    # People have more than one email, grab them all
	email_addresses=person['email_addresses']
	emails=[]
	email_addresses.each do |email|
		emails << email['address']
	end
	#print a tab separated set of fields
	puts "#{person['given_name']}\t#{person['family_name']}\t#{emails.join("\t")}"
end

