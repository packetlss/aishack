#!/usr/bin/python

import aisparser


s = [	

	"!AIVDM,1,1,,A,13u<qr0000Q7GONP8B>blSI800S9,0*1C",
	"!AIVDM,1,1,,B,13u<pF000117EnVP8M58bpW<06BL,0*7B",
	"!AIVDM,1,1,,A,402R3UAufQjW`17JdpP9::Q000S:,0*43",
	"!AIVDM,1,1,,A,14`aNe002K17Em6P4Gs6DE7B00Rb,0*4A",
	"!AIVDM,1,1,,B,13uw889P0017Cf4P8`05E?wF26BL,0*17",
	"!AIVDM,1,1,,B,13uB8eP000Q7EjHP8N<`SpOF0hIu,0*18",
	"!AIVDM,1,1,,A,802R5Ph0Bk;iGPGkw0O@Owwwwwwwwwwwwwwwww0F:<1JAgwwwwwwwtwgwwt,2*0B",
	"!AIVDM,1,1,,B,13u=`gPP0017HbhP8T:00?wH0<0F,0*50",
	"!AIVDM,1,1,,A,802R5Ph0Bk;jb0GkJ`O@2OsHwwwwwwwwwwwwww0Fv<1Kqgwwwwwwwttgwwt,2*20",
	"!AIVDM,1,1,,B,177AS8001u19PW`Owr69i7oJ0HK?,0*27",
	"!AIVDM,1,1,,A,802R5Ph0Bk;nQPGgd0O@2gshwwwwwwwwwwwwww00j<1cagwwwwwwwttOwwt,2*77",
	"!AIVDM,1,1,,B,13u<qr0000Q7GOPP8B>iwSIL06BL,0*07",
	"!AIVDM,1,1,,B,13uM0R700017A?`P8iEFNF5N08Kh,0*38",

 	]


ais_state = aisparser.ais_state()

for p in s:
	result = aisparser.assemble_vdm( ais_state, p )
	if( result == 0):
		ais_state.msgid = aisparser.get_6bit( ais_state.six_state, 6 )
		print "msgid = %d" % (ais_state.msgid)

		if ais_state.msgid == 1:
			msg = aisparser.aismsg_1()
			aisparser.parse_ais_1( ais_state, msg )

			print "mmsi     : %d" % (msg.userid)
			print "latitude : %f" % (msg.latitude/600000.0)
			print "longitude: %f" % (msg.longitude/600000.0)
			print "pos_acc  : %d" % (ord(msg.pos_acc))

		elif ais_state.msgid == 2:
			msg = aisparser.aismsg_2()
			aisparser.parse_ais_2( ais_state, msg )

			print "mmsi     : %d" % (msg.userid)
			print "latitude : %f" % (msg.latitude/600000.0)
			print "longitude: %f" % (msg.longitude/600000.0)
			print "pos_acc  : %d" % (ord(msg.pos_acc))

		elif ais_state.msgid == 3:
			msg = aisparser.aismsg_3()
			aisparser.parse_ais_3( ais_state, msg )

			print "mmsi     : %d" % (msg.userid)
			print "latitude : %f" % (msg.latitude/600000.0)
			print "longitude: %f" % (msg.longitude/600000.0)
			print "pos_acc  : %d" % (ord(msg.pos_acc))

		elif ais_state.msgid == 4:
			msg = aisparser.aismsg_4()
			aisparser.parse_ais_4( ais_state, msg )

			print "mmsi     : %d" % (msg.userid)
			print "latitude : %f" % (msg.latitude/600000.0)
			print "longitude: %f" % (msg.longitude/600000.0)
			print "pos_acc  : %d" % (ord(msg.pos_acc))

		elif ais_state.msgid == 5:
			msg = aisparser.aismsg_5()
			aisparser.parse_ais_5( ais_state, msg )

			print "mmsi       : %d" % (msg.userid)
			print "callsign   : %s" % (msg.callsign)
			print "name       : %s" % (msg.name)
			print "destination: %s" % (msg.dest)

		elif ais_state.msgid == 8:
			msg = aisparser.aismsg_8()
			aisparser.parse_ais_8( ais_state, msg )
			
			dac = msg.app_id >> 6;
			fi = msg.app_id & 0x3F;

			print "dac       : %d" % (dac)
			print "fi        : %d" % (fi)

			sixbit = msg.data
			spare = aisparser.get_6bit( sixbit, 2 )
			msgid = aisparser.get_6bit( sixbit, 6 )
			print "msgid     : %d" % (msgid)

			if fi==1 and msgid==3:
				msg1_3 = aisparser.seaway1_3()
				aisparser.parse_seaway1_3( sixbit, msg1_3 )
				
				for i in xrange(0,6):
					report = aisparser.get_water_level_report( msg1_3, i)
					utc_time = report.utc_time
					print "month     : %d" % (ord(utc_time.month))
					print "day       : %d" % (ord(utc_time.day))
					print "hours     : %d" % (ord(utc_time.hours))
					print "minutes   : %d" % (ord(utc_time.minutes))
					print "station   : %s" % (report.station_id)
					print "longitude : %ld" % (report.longitude)
					print "latitude  : %ld" % (report.latitude)
					print "type      : %d" % (ord(report.type))
					print "level     : %d" % (report.level)
					print "datum     : %d" % (ord(report.datum))
					print "spare     : %d" % (report.spare)
					print "\n"
				
	print ""			
