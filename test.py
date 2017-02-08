import pylutron

caseta = pylutron.Lutron("10.0.2.242", "lutron", "integration", "caseta")
#import pdb; pdb.set_trace()
caseta.load_json_db('config.json')
caseta.connect()
