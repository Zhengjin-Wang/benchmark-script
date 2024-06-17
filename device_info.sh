#!/bin/bash

lscpu > device.log
sudo dmidecode -t memory > mem_info.log