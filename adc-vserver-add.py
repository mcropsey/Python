#!/usr/bin/env python



import sys
from nssrc.com.citrix.netscaler.nitro.exception.nitro_exception import nitro_exception
from nssrc.com.citrix.netscaler.nitro.resource.config.lb.lbvserver import lbvserver
from nssrc.com.citrix.netscaler.nitro.service.nitro_service import nitro_service

#
# Main thread of execution
#

if __name__ == '__main__':

		s_ip = "192.168.1.31"
		s_username = "admin"
		s_password = "ZAQ!xsw2"

		try :

			#Create an instance of the nitro_service class to connect to the appliance
			ns_session = nitro_service(s_ip,"HTTP")

			ns_session.set_credential(s_username,s_password) #to make arguments more generic
			ns_session.timeout = 310
			# To skip invalid arguments for Add/Update/Delete Operations (HTTP POST/PUT/DELETE Request)
			# Set this argument to True when newer version of SDK is used with older version of Netscaler
			ns_session.skipinvalidarg = True
			# By setting this argument to True, add operation will take care of adding or updating the entity without throwing any error
			ns_session.idempotent = True
			# By setting this argument to True HTTP Basic Auth will be used and there is no need for login() and logout() calls
			ns_session.basic_auth = False
			#Log on to the appliance using your credentials
			ns_session.login()

			#Enable the load balancing feature.
			features_to_be_enabled = "lb"
			ns_session.enable_features(features_to_be_enabled)

			#Create an instance of the virtual server class
			new_lbvserver_obj = lbvserver()

			#Create a new virtual server
			new_lbvserver_obj.name = "RestAPICreatedVserver"
			new_lbvserver_obj.ipv46 = "192.168.1.90"
			new_lbvserver_obj.servicetype = "HTTP"
			new_lbvserver_obj.port = 80
			new_lbvserver_obj.lbmethod = "ROUNDROBIN"
			lbvserver.add(ns_session, new_lbvserver_obj)

			#Retrieve the details of the virtual server
			new_lbvserver_obj = lbvserver.get(ns_session,new_lbvserver_obj.name)
			print("Name : " + new_lbvserver_obj.name + "\n" + "Protocol : " + new_lbvserver_obj.servicetype)

			#Delete the virtual server
			#lbvserver.delete(ns_session, new_lbvserver_obj.name)

			#Save the configurations
			ns_session.save_config()

			#Logout from the NetScaler appliance
			ns_session.logout()

		except nitro_exception as  e:
			print("Exception::errorcode="+str(e.errorcode)+",message="+ e.message)
		except Exception as e:
			print("Exception::message="+str(e.args))
	
