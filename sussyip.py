import geoip2.database

# This creates a Reader object. You should use the same object
# across multiple requests as creation of it is expensive.
with geoip2.database.Reader('/path/to/GeoLite2-City.mmdb') as reader:

    # Replace "city" with the method corresponding to the database
    # that you are using, e.g., "country".
    response = reader.city('203.0.113.0')

    response.country.iso_code
    # 'US'
    response.country.name
    # 'United States'
    response.country.names['zh-CN']
    # u'美国'

    response.subdivisions.most_specific.name
    # 'Minnesota'
    response.subdivisions.most_specific.iso_code
    # 'MN'

    response.city.name
    # 'Minneapolis'

    response.postal.code
    # '55455'

    response.location.latitude
    # 44.9733
    response.location.longitude
    # -93.2323

    response.traits.network
    # IPv4Network('203.0.113.0/24')


    
import geoip2.database

# This creates a Reader object. You should use the same object
# across multiple requests as creation of it is expensive.
with geoip2.database.Reader('/path/to/GeoLite2-ASN.mmdb') as reader:
    response = reader.asn('203.0.113.0')
    response.autonomous_system_number
    # 1221
    response.autonomous_system_organization
    # 'Telstra Pty Ltd'
    response.ip_address
    # '203.0.113.0'
    response.network
    # IPv4Network('203.0.113.0/24')