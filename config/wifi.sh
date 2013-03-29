#!/bin/bash

#####################################
#Author: Leon Lee                   #
#email: lendylongli@gmail.com       #
#QQ: 730395591                      #
#Version: 1.0                       #
#Note: If you have some good ideas  #
#	or advice, please mail me^^ #
#####################################
# https://gist.github.com/anonymous/1117004
#####################################
ShareNet=eth0
# Wmode=ad-hoc
Wmode=managed
Wchannel=auto
Wessid=askender_in_anwen #ssid自己改
WInterface=wlan0
WPasskey=androidworkab   #密码自己改
Wkey=restricted
Igateway=192.168.2.254
Inetmask=255.255.255.0
Inetwork=192.168.2.0
DhcpRangeMin=192.168.2.10
DhcpRangeMax=192.168.2.105
#####################################
adhocFolder=/etc/adhoc
dnsmasqFile=$adhocFolder/dnsmasq.conf
resolvFile=/etc/resolv.conf
dnsmasqPid=/var/run/dnsmasq.pid
dnsmasqLeases=/var/run/dnsmasq.leases

# start Ad-hoc
function adhoc_start
{
	echo "Starting Ad-hoc..."
	check_dnsmasq
	sleep 1
	sudo ifconfig $WInterface down
	echo -n "Setting $WInterface gateway and netmask."
	sudo ifconfig $WInterface $Igateway netmask $Inetmask
	sleep 1
	echo -n "    [ good ]"
	echo
	
	echo -n "Setting up $WInterface ..."
	sudo ifconfig $WInterface up
	sleep 1
	echo -n "    [ good ]"
	echo
	
	echo -n "Setting $WInterface mode...$Wmode"
	sudo iwconfig $WInterface mode $Wmode
	sleep 1
	echo -n "    [ good ]"
	echo
	
	echo -n "Setting $WInterface essid..."
	sudo iwconfig $WInterface essid $Wessid
	sleep 1
	echo -n "    [ good ]"
	echo
	
	echo -n "Setting $WInterface cannel..."
	sudo iwconfig $WInterface channel $Wchannel
	sleep 1
	echo -n "    [ good ]"
	echo
	
	echo -n "Setting $WInterface password..."
	sudo iwconfig $WInterface key s:$WPasskey
	sleep 1
	echo -n "    [ good ]"
	echo
	
	echo -n "Setting $WInterface key type..."
	sudo iwconfig $WInterface key $Wkey
	sleep 1
	echo -n "    [ good ]"
	echo
	echo
	echo -n "Setting iptable..."
	sleep 1
	#remove the old rules
	sudo iptables -N wireless-adhoc
  	sudo iptables -F wireless-adhoc
  	sudo iptables -t nat -F PREROUTING
  	sudo iptables -t nat -F POSTROUTING
  	sudo iptables -t nat -F
	#bring up the NAT rules
	sudo iptables -A wireless-adhoc -m state --state ESTABLISHED,RELATED -j ACCEPT
	sudo iptables -A wireless-adhoc -s $Inetwork/24 -j ACCEPT
	sudo iptables -A wireless-adhoc -p 47 -j ACCEPT
	sudo iptables -A wireless-adhoc -j DROP
	sudo iptables -A FORWARD -m state --state INVALID -j DROP
	sudo iptables -A FORWARD -j wireless-adhoc
	sudo iptables -t nat -I POSTROUTING -s $Inetwork/24 -j MASQUERADE
	sleep 1
	sudo sh -c "echo 1 > /proc/sys/net/ipv4/ip_forward"
	echo -n "."
	sleep 1
	sudo dnsmasq -i $WInterface --resolv-file=$resolvFile --conf-file=$dnsmasqFile
	echo
	echo "Success!^^"
}

# stop Ad-hoc
function adhoc_stop
{
	echo "Stopping adhoc ...$WInterface"
	sudo sh -c "echo 0 > /proc/sys/net/ipv4/ip_forward"
	echo -n "."
	# stop adhoc mode
	sudo iwconfig $WInterface mode managed
	sleep 1
	echo -n "."
	sudo iwconfig $WInterface key off
	sleep 1
	echo -n "."
	sudo iwconfig $WInterface essid any
	sleep 1
	echo -n "."
	sudo ifconfig $WInterface down
	sleep 1
	echo -n "."
	# remove iptabled rules
	sudo iptables -D FORWARD -j wireless-adhoc
	sudo iptables -D FORWARD -m state --state INVALID -j DROP
	sudo iptables -F wireless-adhoc
	sudo iptables -X wireless-adhoc
	sudo iptables -t nat -F PREROUTING
	sudo iptables -t nat -F POSTROUTING
	sudo iptables -t nat -F
	sleep 1
	if [ -f $dnsmasqPid ]; then
		dnsmasqID=`cat $dnsmasqPid`
		kill $dnsmasqID
		sleep 1
	fi
	if [ -f $dnsmasqLeases ]; then 
		rm $dnsmasqLeases
	fi
	echo
	echo "Wifi ad-hoc now stopped"
}

function adhoc_restart
{
	echo "Now, restart ad-hoc ..."
	adhoc_stop
	sleep 2
	adhoc_start
}
# check dnsmasq.conf
function check_dnsmasq
{

	if [ -f $dnsmasqPid ]; then
		echo "Dhcp is running!"
		echo "Now, restart Ad-hoc"
		adhoc_stop
		sleep 1
	fi
	if [ ! -d $adhocFolder ]; then
	mkdir $adhocFolder
	fi

	if [ ! -f $dnsmasqFile ]; then
	echo "$dnsmasqFile is not exist, now building."

	echo "dhcp-authoritative" > $dnsmasqFile
	echo "dhcp-range=$DhcpRangeMin,$DhcpRangeMax,12h" >> $dnsmasqFile
	echo "dhcp-leasefile=$dnsmasqLeases" >> $dnsmasqFile
	echo "pid-file=$dnsmasqPid" >> $dnsmasqFile
	echo "user=root" >> $dnsmasqFile
	echo "no-negcache" >> $dnsmasqFile
	fi
}

# is super user?
function super_user
{
	if [ "$UID" = "0" ]; then
	return 0
	else
	return 1
	fi
}

function usage
{
	echo "Wifi Ad-hoc control"
	echo "$1 [-h][-s]"
	echo "Default is start ad-hoc"
	echo "-h show the usage"
	echo "-s stop ad-hoc"
	echo "-r restart ad-hoc"
}

if ! super_user ; then
echo "Need super user permission!"
exit 1
fi
if [ $# -lt 1 ]; then
adhoc_start
elif [ "$1" = "-h" ]; then
usage
elif [ "$1" = "-s" ]; then
adhoc_stop
elif [ "$1" = "-r" ]; then
adhoc_restart
else
echo "Input error!"
echo "$1 -h gives usage information."
fi
