import subprocess
import re


cmd_output = subprocess.run(['netsh','wlan','show','profiles'],capture_output=true).stdout.decode()

profile_names = (re.findall("All user profile  : (.*)\r"),cmd_output)

if profile_names != 0:
	for name in profile_name:
		wifi_profile={}
		profile_info + subprocess.run(['netsh','wlan','show','profilea',name],capture_output=True).stdout.decode()

wifi_list=[]
		
		if re.search("Security key			:Absent",profile_info):continue
		
		else:
			wifi_profile['ssid'] = name
			profile_info_password = subprocess.run(['netsh','wlan','show','profiles',name,'key=clear'],capture_output=true).stdout.
			decore()
			password = re.search("key content			:(.*)\r",profile_info_password)
			if password == none:
				wifi_profile['password'] = None
			else:
				wifi_profile['password'] = password[1]
		wifi_list.append(wifi_profiles)
		
		
		
for i in range(len(wifi_list)):
	print(wifi_list[i])
