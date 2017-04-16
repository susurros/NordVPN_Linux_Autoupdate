#!/usr/bin/python3

import subprocess

username=""
password=""

def Replace_VPN(vpn_list):
	for vpn_uuid in vpn_list.splitlines():
		subprocess.call(['nmcli','con','del',vpn_uuid])
		
def Download_Import():
	N_URL="https://nordvpn.com/api/files/zip"
	subprocess.call(['rm','-rf','/tmp/Nord'])
	subprocess.call(['mkdir','/tmp/Nord'])
	subprocess.call(['wget','-P','/tmp/Nord',N_URL])
	subprocess.call(['unzip','/tmp/Nord/zip','-d','/tmp/Nord'])
	nord_files = subprocess.getoutput('ls /tmp/Nord/*')
	for item in nord_files.splitlines():
		subprocess.call(['nmcli','con','import','type','openvpn','file',item])


def Nord_VPN_CON():
	return subprocess.getoutput("nmcli connection | grep nord | awk '{print $2}'")

def VPN_USER_PASS(vpn_list,user,password):
	for vpn_uuid in vpn_list.splitlines():
		print("Adding User")
		subprocess.call(['nmcli','con','mod',vpn_uuid,'+vpn.user',user])
		print("Changing pass flag")
		subprocess.call(['nmcli','con','mod',vpn_uuid,'+vpn.data','password-flags=0'])
		print("Adding Pass")
		subprocess.call(['nmcli','con','mod',vpn_uuid,'+vpn.secrets','password='+password])




Replace_VPN(vpn_list=Nord_VPN_CON())
Download_Import()
VPN_USER_PASS(vpn_list=Nord_VPN_CON(),user=username,password=password)