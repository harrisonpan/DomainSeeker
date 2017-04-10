# -*- coding:utf-8 -*-
import dnslib.dnsfucation as dns
import socket, sys
import threading
import json
import base64
import logging

logging.basicConfig(level=logging.INFO)
dict_data = {}
dict_config = {}
Remote_dns_server = '114.114.114.114'
Remote_dns_port = 53
Local_dns_server = '127.0.0.1'
Local_dns_port = 53


def init():
    global dict_data
    global dict_config
    global Remote_dns_server
    global Remote_dns_port
    global Local_dns_server
    global Local_dns_port
    with open("./conf/config.json", 'r') as d:
        dict_config = json.load(d)

    with open(dict_config['Rpz_json_path'], 'r') as c:
        dict_data = json.load(c)

    with open("./data/wrcd.json", 'r') as f:
        dict_wdata = json.load(f)

    if dict_config['sni_proxy_on']:
        for key in dict_wdata:
            dict_wdata[key] = dict_config['sni_proxy_ip']
    dict_data.update(dict_wdata)

    Remote_dns_server = dict_config['Remote_dns_server']
    Remote_dns_port = dict_config['Remote_dns_port']
    Local_dns_server = dict_config['Local_dns_server']
    Local_dns_port = dict_config['Local_dns_port']

    logging.info("==========Config===========")
    logging.info("Local_dns_server:%s", Local_dns_server)
    logging.info("Local_dns_port:%s", Local_dns_port)
    logging.info("Remote_dns_server:%s", Remote_dns_server)
    logging.info("Remote_dns_port:%s", Remote_dns_port)
    logging.info("===========Config==========")


def sendDnsData(data, s, addr):
    global Remote_dns_server
    global Remote_dns_port
    global dict_data
    local, data = dns.analysis(data, dict_data)
    if local == 1:
        s.sendto(data, addr)
    else:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(data, (Remote_dns_server, Remote_dns_port))
        sock.settimeout(15)
        while True:
            try:
                rspdata = sock.recv(4096)
            except Exception as e:
                logging.warning("Recv:\t%s" % e)
                break
            s.sendto(rspdata, addr)
            break


def main():
    init()
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        logging.info("Trying start bind local IP：%s and port:%s",
                     str(Local_dns_server),
                     str(Local_dns_port))
        s.bind((Local_dns_server, Local_dns_port))
    except Exception as e:
        logging.info("\nBinding failed! Please run as administrator，\n"
                     "\nAnd check the local IP address and port is correct?\n\n")
        logging.info("==========Error message==========")
        logging.critical(e)
        return
    logging.info("Bind successfully! Running ...")
    while True:
        try:
            data, addr = s.recvfrom(2048)
            worker = threading.Thread(target=sendDnsData, args=(data, s, addr,))
            worker.setDaemon(True)
            worker.start()
        except Exception as e:
            logging.warning("Unknow error:\t%s" % e)


if __name__ == '__main__':
    main()
