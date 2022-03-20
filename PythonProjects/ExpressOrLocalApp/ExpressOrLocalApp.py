#! /usr/bin/python3

import glob
from google.protobuf import json_format
from google.transit import gtfs_realtime_pb2
from google.protobuf.json_format import MessageToDict
import requests
from requests.auth import AuthBase
from datetime import *
import pprint
import pandas as pd
import time
import xlsxwriter
import sqlite3
import dataset
import attr
import typing
import pendulum
from tabulate import tabulate
import logging
import os

# Declare Train Data Classes:
# Refer to basicOOP.py for basic use:
@attr.dataclass
class LiveTrain:
    id_key: str
    trip_update_key: dict
    trip_key: str
    trip_id_key: str
    location_bound: str
    start_time_key:str
    start_date_key:str
    start_date_day:int
    start_date_month:int
    start_date_year:int
    start_date_hour:int
    start_date_min:int
    start_date_sec:int
    start_date_meridiem:str
    start_date_timezone:str
    route_id_key: str
    stop_time_update_key_list: typing.Optional[list] = attr.ib(default=None)
    arrival_key: typing.Optional[dict] = attr.ib(default=None)
    arrival_time_key: typing.Optional[str] = attr.ib(default=None)
    arr_month: typing.Optional[str] = attr.ib(default=None)
    arr_day: typing.Optional[int] = attr.ib(default=None)
    arr_year: typing.Optional[int] = attr.ib(default=None)
    arr_hour: typing.Optional[int] = attr.ib(default=None)
    arr_min: typing.Optional[int] = attr.ib(default=None)
    arr_sec: typing.Optional[int] = attr.ib(default=None)
    arr_meridiem: typing.Optional[str] = attr.ib(default=None)
    arr_timezone: typing.Optional[str] = attr.ib(default=None)
    departure_key: typing.Optional[dict] = attr.ib(default=None)
    departure_time_key: typing.Optional[str] = attr.ib(default=None)
    dep_month: typing.Optional[str] = attr.ib(default=None)
    dep_day: typing.Optional[int] = attr.ib(default=None)
    dep_year: typing.Optional[int] = attr.ib(default=None)
    dep_hour: typing.Optional[int] = attr.ib(default=None)
    dep_min: typing.Optional[int] = attr.ib(default=None)
    dep_sec: typing.Optional[int] = attr.ib(default=None)
    dep_meridiem: typing.Optional[str] = attr.ib(default=None)
    dep_timezone: typing.Optional[str] = attr.ib(default=None)
    stop_time_update_stop_id_key: typing.Optional[str] = attr.ib(default=None)
    arr_dep_stop_location: typing.Optional[str] = attr.ib(default=None)
    arr_dep_location_bound: typing.Optional[str] = attr.ib(default=None)
live_train_object_list = []

@attr.dataclass
class ScheduleTrain:
    id_key: str
    vehicle_key: dict
    trip_key: str
    trip_id_key: str
    location_bound: str
    start_time_key:str
    start_date_key:str
    start_date_day:int
    start_date_month:int
    start_date_year:int
    start_date_hour:int
    start_date_min:int
    start_date_sec:int
    start_date_meridiem:str
    start_date_timezone:str
    route_id_key: str
    current_stop_sequence_key: typing.Optional[int] = attr.ib(default=None)
    current_stop_location: typing.Optional[str] = attr.ib(default=None)
    timestamp_key: typing.Optional[str] = attr.ib(default=None)
    cur_month: typing.Optional[str] = attr.ib(default=None)
    cur_day: typing.Optional[int] = attr.ib(default=None)
    cur_year: typing.Optional[int] = attr.ib(default=None)
    cur_hour: typing.Optional[int] = attr.ib(default=None)
    cur_min: typing.Optional[int] = attr.ib(default=None)
    cur_sec: typing.Optional[int] = attr.ib(default=None)
    cur_meridiem: typing.Optional[str] = attr.ib(default=None)
    cur_timezone: typing.Optional[str] = attr.ib(default=None)
    vehicle_stop_id_key: typing.Optional[str] = attr.ib(default=None)
schedule_train_object_list = []

# Basic Logging:

# Remove the log if it already exists because it has to be fresh with every run:

# Normal log file location on a local machine:
# localLogfile = 'C:/ExpressOrLocalApp/expressOrLocalAppLog.txt'

# if os.path.isfile(logfile):
    # os.remove(localLogfile)

serverLogfile = '/var/www/musimatic/pythonprojectwebsites/ExpressOrLocalApp/expressOrLocalAppLog.txt'

# Logfile location on a server:
if os.path.isfile(serverLogfile):
    os.remove(serverLogfile)

# Create the new fresh log called 'expressOrLocalApplog.txt':
logging.basicConfig(filename='/var/www/musimatic/pythonprojectwebsites/ExpressOrLocalApp/expressOrLocalAppLog.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


def get_request(MTADataFeed):
    # Updated this app to include API Key reference from this Google Group Post:
    # https://groups.google.com/g/mtadeveloperresources/c/t8anoGP5S8U
    r = requests.get('https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-7', headers={'x-api-key':''})
    
    return r


def create_feed(r):
    feed = gtfs_realtime_pb2.FeedMessage()
    
    return feed


def convert_to_dict_feed(r, feed):
    feed.ParseFromString(r.content)
    dict_feed = MessageToDict(feed)
    
    return dict_feed


def pprint_dict_feed(dict_feed):
    logging.debug('pprint Version of dict_feed: ')
    logging.debug(pprint.pprint(dict_feed))


def print_item_info(item):
    logging.debug('\n\nitem = ' + str(item))
    logging.debug('type(item) = ' + str(type(item)))


def createTrainLists(dict_feed):
    live_train_data = []
    scheduled_train_data = []
    i = 0

    for item in dict_feed['entity']:
        # Live Train Data
        if i % 2 == 0:
            logging.debug('\n\nLIVE TRAIN DATA:')
            print_item_info(item)
            live_train_data.append(item)
        # Scheduled Train Data
        else:
            logging.debug('\n\nSCHEDULED TRAIN DATA:')
            print_item_info(item)
            scheduled_train_data.append(item)
        i += 1

    return live_train_data, scheduled_train_data

def create_object_lists(live_train_data, scheduled_train_data):
    logging.debug('live_train_data = ' + str(live_train_data))
    logging.debug('scheduled_train_data = ' + str(scheduled_train_data))

    # Uncomment for debugging purposes:
    # print('\n\nGOING THROUGH live_train_data list:')

    for item in live_train_data:
        print_item_info(item)
        if item['id']:
            id_key = item['id']
            logging.debug('\nid_key = ' + str(id_key))
            logging.debug('\ntype(id_key) = ' + str(type(id_key)))
        trip_update_key = item['tripUpdate']
        logging.debug('\ntrip_update_key = ' + str(trip_update_key))
        logging.debug('\ntype(trip_update_key) = ' + str(type(trip_update_key)))
        trip_key = trip_update_key['trip']
        logging.debug('\ntrip_key = ' + str(trip_key))
        logging.debug('\ntype(trip_key) = ' + str(type(trip_key)))
        trip_id_key = trip_key['tripId']
        logging.debug('\ntrip_id_key = ' + str(trip_id_key))
        logging.debug('\ntype(trip_id_key) = ' + str(type(trip_id_key)))
        if str(trip_id_key)[-1] == 'S':
            location_bound = '34 St - 11 Av'
        if str(trip_id_key)[-1] == 'N':
            location_bound = 'Flushing - Main St'
        logging.debug('location_bound = ' + str(location_bound))
        start_time_key = trip_key['startTime']
        logging.debug('\nstart_time_key = ' + str(start_time_key))
        logging.debug('\ntype(start_time_key) = ' + str(type(start_time_key)))
        start_date_key = trip_key['startDate']
        logging.debug('\nstart_date_key = ' + str(start_date_key))
        logging.debug('\ntype(start_date_key) = ' + str(type(start_date_key)))
        logging.debug('\n\n\nTEST TEST TEST')
        date_time_object = str(start_date_key) + str(start_time_key)
        logging.debug('date_time_object = ' + str(date_time_object))
        # DTO = Date Time Object
        start_date_pendulum_dto = pendulum.from_format(date_time_object, 'YYYYMMDDHH:mm:ss', tz='UTC').in_timezone('America/New_York')
        logging.debug('start_date_pendulum_dto = ' + str(start_date_pendulum_dto))
        start_date_day = start_date_pendulum_dto.day
        start_date_month = start_date_pendulum_dto.month
        start_date_year = start_date_pendulum_dto.year
        start_date_hour = start_date_pendulum_dto.format('h')
        start_date_min = start_date_pendulum_dto.format('mm')
        start_date_sec = start_date_pendulum_dto.format('ss')
        start_date_meridiem = start_date_pendulum_dto.strftime('%p')
        start_date_timezone = start_date_pendulum_dto.strftime('%Z')
        logging.debug('start_date_day = ' + str(start_date_day))
        logging.debug('start_date_month = ' + str(start_date_month))
        logging.debug('start_date_year = ' + str(start_date_year))
        logging.debug('start_date_hour = ' + str(start_date_hour))
        logging.debug('start_date_min = ' + str(start_date_min))
        logging.debug('start_date_sec = ' + str(start_date_sec))
        route_id_key = trip_key['routeId']
        logging.debug('\nroute_id_key = ' + str(route_id_key))
        logging.debug('\ntype(route_id_key) = ' + str(type(route_id_key)))
        live_train_object_list.append(LiveTrain(id_key=id_key, 
                                           trip_update_key=trip_update_key,
                                           trip_key=trip_key,
                                           trip_id_key=trip_id_key,
                                           location_bound=location_bound,
                                           start_time_key=start_time_key,
                                           start_date_key=start_date_key,
                                           start_date_day=start_date_day,
                                           start_date_month=start_date_month,
                                           start_date_year=start_date_year,
                                           start_date_hour=start_date_hour,
                                           start_date_min=start_date_min,
                                           start_date_sec=start_date_sec,
                                           start_date_meridiem=start_date_meridiem,
                                           start_date_timezone=start_date_timezone,
                                           route_id_key=route_id_key,
                                           stop_time_update_key_list=None,
                                           arrival_key=None,
                                           arrival_time_key=None,
                                           arr_month=None,
                                           arr_day=None,
                                           arr_year=None,
                                           arr_hour=None,
                                           arr_min=None,
                                           arr_sec=None,
                                           arr_meridiem=None,
                                           arr_timezone=None,
                                           departure_key=None,
                                           departure_time_key=None,
                                           dep_month=None,
                                           dep_day=None,
                                           dep_year=None,
                                           dep_hour=None,
                                           dep_min=None,
                                           dep_sec=None,
                                           dep_meridiem=None,
                                           dep_timezone=None,
                                           stop_time_update_stop_id_key=None,
                                           arr_dep_stop_location=None,
                                           arr_dep_location_bound=None))
        if 'stopTimeUpdate' in trip_update_key:
            stop_time_update_key_list = trip_update_key['stopTimeUpdate']
            logging.debug('\nstop_time_update_key_list = ' + str(stop_time_update_key_list))
            logging.debug('\ntype(stop_time_update_key_list) = ' + str(type(stop_time_update_key_list)))
            for listItem in stop_time_update_key_list:
                arrival_key = listItem['arrival']
                logging.debug('\narrival_key = ' + str(arrival_key))
                logging.debug('\ntype(arrival_key) = ' + str(type(arrival_key)))
                arrival_time_key = arrival_key['time']
                logging.debug('\narrival_time_key = ' + str(arrival_time_key))
                logging.debug('\ntype(arrival_time_key) = ' + str(type(arrival_time_key)))
                # This proves that the time data that the MTA gives is in UTC-0 timezone
                pendulum_unconverted_arrival_time_key = pendulum.from_timestamp(int(arrival_time_key))
                logging.debug('\npendulum_unconverted_arrival_time_key = ' + str(pendulum_unconverted_arrival_time_key))
                logging.debug('\ntype(pendulum_unconverted_arrival_time_key = ' + str(type(pendulum_unconverted_arrival_time_key)))
                logging.debug('\ndatetime version of arrival_time_key = ' + str(datetime.fromtimestamp(int(arrival_time_key))))
                pendulum_arrival_time_key = pendulum.from_timestamp(int(arrival_time_key)).in_timezone('America/New_York')
                logging.debug('\npendulum_arrival_time_key = ' + str(pendulum_arrival_time_key))
                logging.debug('\ntype(pendulum_arrival_time_key) = ' + str(type(pendulum_arrival_time_key)))
                # pendulum_arrival_time_key.set(tz='America/New_York')
                # arr_month = pendulum_arrival_time_key.strftime('%-m')
                arr_month = pendulum_arrival_time_key.month
                arr_day = int(pendulum_arrival_time_key.strftime('%d'))
                arr_year = int(pendulum_arrival_time_key.strftime('%Y'))
                arr_hour = int(pendulum_arrival_time_key.strftime('%I'))
                # arr_min = int(pendulum_arrival_time_key.strftime('%M'))
                arr_min = pendulum_arrival_time_key.format('mm')
                arr_sec = pendulum_arrival_time_key.format('ss')
                arr_meridiem = pendulum_arrival_time_key.strftime('%p')
                arr_timezone = pendulum_arrival_time_key.strftime('%Z')
                logging.debug('\narr_month = ' + str(arr_month))
                logging.debug('\ntype(arr_month) = ' + str(type(arr_month)))
                logging.debug('\narr_day = ' + str(arr_day))
                logging.debug('\ntype(arr_day) = ' + str(type(arr_day)))
                logging.debug('\narr_year = ' + str(arr_year))
                logging.debug('\ntype(arr_year) = ' + str(type(arr_year)))
                logging.debug('\narr_hour = ' + str(arr_hour))
                logging.debug('\ntype(arr_hour) = ' + str(type(arr_hour)))
                logging.debug('\narr_min = ' + str(arr_min))
                logging.debug('\ntype(arr_min) = ' + str(type(arr_min)))
                logging.debug('\narr_sec = ' + str(arr_sec))
                logging.debug('\ntype(arr_sec) = ' + str(type(arr_sec)))
                logging.debug('\narr_meridiem = ' + str(arr_meridiem))
                logging.debug('\ntype(arr_meridiem) = ' + str(type(arr_meridiem)))
                logging.debug('\narr_timezone = ' + str(arr_timezone))
                logging.debug('\ntype(arr_timezone) = ' + str(type(arr_timezone)))
                departure_key = listItem['departure']
                logging.debug('\ndeparture_key = ' + str(departure_key))
                logging.debug('\ntype(departure_key) = ' + str(type(departure_key)))
                departure_time_key = departure_key['time']
                logging.debug('\ndeparture_time_key = ' + str(departure_time_key))
                logging.debug('\ntype(departure_time_key) = ' + str(type(departure_time_key)))
                pendulum_departure_time_key = pendulum.from_timestamp(int(departure_time_key)).in_timezone('America/New_York')
                logging.debug('\npendulum_departure_time_key = ' + str(pendulum_departure_time_key))
                dep_month = pendulum_departure_time_key.month
                dep_day = int(pendulum_departure_time_key.strftime('%d'))
                dep_year = int(pendulum_departure_time_key.strftime('%Y'))
                dep_hour = int(pendulum_departure_time_key.strftime('%I'))
                # dep_min = int(pendulum_departure_time_key.strftime('%M'))
                dep_min = pendulum_departure_time_key.format('mm')
                dep_sec = pendulum_departure_time_key.format('ss')
                dep_meridiem = pendulum_departure_time_key.strftime('%p')
                dep_timezone = pendulum_departure_time_key.strftime('%Z')
                logging.debug('\ndep_month = ' + str(dep_month))
                logging.debug('\ntype(dep_month) = ' + str(type(dep_month)))
                logging.debug('\ndep_day = ' + str(dep_day))
                logging.debug('\ntype(dep_day) = ' + str(type(dep_day)))
                logging.debug('\ndep_year = ' + str(dep_year))
                logging.debug('\ntype(dep_year) = ' + str(type(dep_year)))
                logging.debug('\ndep_hour = ' + str(dep_hour))
                logging.debug('\ntype(dep_hour) = ' + str(type(dep_hour)))
                logging.debug('\ndep_min = ' + str(dep_min))
                logging.debug('\ntype(dep_min) = ' + str(type(dep_min)))
                logging.debug('\ndep_sec = ' + str(dep_sec))
                logging.debug('\ntype(dep_sec) = ' + str(type(dep_sec)))
                logging.debug('\ndep_meridiem = ' + str(dep_meridiem))
                logging.debug('\ntype(dep_meridiem = ' + str(type(dep_meridiem)))
                logging.debug('\ndep_timezone = ' + str(dep_timezone))
                logging.debug('\ntype(dep_timezone) = ' + str(type(dep_timezone)))
                stop_time_update_stop_id_key = listItem['stopId']
                filtered_stop_id_key = str(stop_time_update_stop_id_key)[0:3]
                # Have a default N/A value in case the data feed messes up                
                arr_dep_stop_location = 'N/A'
                logging.debug('\nstop_time_update_stop_id_key = ' + str(stop_time_update_stop_id_key))      
                logging.debug('\ntype(stop_time_update_stop_id_key) = ' + str(type(stop_time_update_stop_id_key)))
                logging.debug('\nfiltered_stop_id_key = ' + str(filtered_stop_id_key))
                TrainStopsFile = open('/projects_private/PythonProjects/ExpressOrLocalApp/7TrainStops.txt', 'r')
                logging.debug('stop_time_update_stop_id_key = ' + str(stop_time_update_stop_id_key))
                for line in TrainStopsFile:
                    logging.debug(line)
                    split_line = line.strip().split(',')
                    stop_name = split_line[0]
                    filtered_stop_name = stop_name[0:3]
                    stop_location = split_line[2]
                    logging.debug('stop_name = ' + str(split_line[0]))
                    logging.debug('filtered_stop_name = ' + str(filtered_stop_name))
                    logging.debug('stop_location = ' + str(stop_location))
                    if str(filtered_stop_id_key) == str(filtered_stop_name):
                        arr_dep_stop_location = stop_location
                        logging.debug('arr_dep_stop_location found!')
                        logging.debug('arr_dep_stop_location = ' + str(arr_dep_stop_location))
                TrainStopsFile.close()
                if str(stop_time_update_stop_id_key)[-1] == 'S':
                    arr_dep_location_bound = '34 St - 11 Av'
                if str(stop_time_update_stop_id_key)[-1] == 'N':
                    arr_dep_location_bound = 'Flushing - Main St'
                logging.debug('arr_dep_location_bound = ' + str(arr_dep_location_bound))
                live_train_object_list.append(LiveTrain(id_key=id_key,
                                                        trip_update_key=None,
                                                        trip_key=None,
                                                        trip_id_key=None,
                                                        location_bound=None,
                                                        start_time_key=None,
                                                        start_date_key=None,
                                                        start_date_day=None,
                                                        start_date_month=None,
                                                        start_date_year=None,
                                                        start_date_hour=None,
                                                        start_date_min=None,
                                                        start_date_sec=None,
                                                        start_date_meridiem=None,
                                                        start_date_timezone=None,
                                                        route_id_key=None,
                                                        stop_time_update_key_list=stop_time_update_key_list,
                                                        arrival_key=arrival_key,
                                                        arrival_time_key=arrival_time_key,
                                                        arr_month=arr_month,
                                                        arr_day=arr_day,
                                                        arr_year=arr_year,
                                                        arr_hour=arr_hour,
                                                        arr_min=arr_min,
                                                        arr_sec=arr_sec,
                                                        arr_meridiem=arr_meridiem,
                                                        arr_timezone=arr_timezone,
                                                        departure_key=departure_key,
                                                        departure_time_key=departure_time_key,
                                                        dep_month=dep_month,
                                                        dep_day=dep_day,
                                                        dep_year=dep_year,
                                                        dep_hour=dep_hour,
                                                        dep_min=dep_min,
                                                        dep_sec=dep_sec,
                                                        dep_meridiem=dep_meridiem,
                                                        dep_timezone=dep_timezone,
                                                        stop_time_update_stop_id_key=stop_time_update_stop_id_key,
                                                        arr_dep_stop_location=arr_dep_stop_location,
                                                        arr_dep_location_bound=arr_dep_location_bound))

    # Uncomment for debugging purposes:
    # print('\n\nGOING THROUGH scheduled_train_data list:')
    for item in scheduled_train_data:
        print_item_info(item)
        id_key = item['id']
        logging.debug('\nid_key = ' + str(id_key))
        logging.debug('\ntype(id_key) = ' + str(type(id_key)))
        vehicle_key = item['vehicle']
        logging.debug('\nvehicle_key = ' + str(vehicle_key))
        logging.debug('\ntype(vehicle_key) ' + str(type(vehicle_key)))
        trip_key = vehicle_key['trip']
        logging.debug('\ntrip_key = ' + str(trip_key))
        logging.debug('\ntype(trip_key) = ' + str(type(trip_key)))
        trip_id_key = trip_key['tripId']
        logging.debug('\ntrip_id_key = ' + str(trip_id_key))
        logging.debug('\ntype(trip_id_key) = ' + str(type(trip_id_key)))
        if str(trip_id_key)[-1] == 'S':
            location_bound = '34 St - 11 Av'
        if str(trip_id_key)[-1] == 'N':
            location_bound = 'Flushing - Main St'
        logging.debug('location_bound = ' + str(location_bound))
        start_time_key = trip_key['startTime']
        logging.debug('\nstart_time_key = ' + str(start_time_key))
        logging.debug('\ntype(start_time_key) = ' + str(type(start_time_key)))
        start_date_key = trip_key['startDate']
        logging.debug('\nstart_date_key = ' + str(start_date_key))
        logging.debug('\ntype(start_date_key) = ' + str(type(start_date_key)))
        date_time_object = str(start_date_key) + str(start_time_key)
        logging.debug('date_time_object = ' + str(date_time_object))
        # DTO = Date Time Object
        start_date_pendulum_dto = pendulum.from_format(date_time_object, 'YYYYMMDDHH:mm:ss', tz='UTC').in_timezone('America/New_York')
        logging.debug('start_date_pendulum_dto = ' + str(start_date_pendulum_dto))
        start_date_day = start_date_pendulum_dto.day
        start_date_month = start_date_pendulum_dto.month
        start_date_year = start_date_pendulum_dto.year
        start_date_hour = start_date_pendulum_dto.format('h')
        start_date_min = start_date_pendulum_dto.format('mm')
        start_date_sec = start_date_pendulum_dto.format('ss')
        start_date_meridiem = start_date_pendulum_dto.strftime('%p')
        start_date_timezone = start_date_pendulum_dto.strftime('%Z')
        logging.debug('start_date_day = ' + str(start_date_day))
        logging.debug('start_date_month = ' + str(start_date_month))
        logging.debug('start_date_year = ' + str(start_date_year))
        logging.debug('start_date_hour = ' + str(start_date_hour))
        logging.debug('start_date_min = ' + str(start_date_min))
        logging.debug('start_date_sec = ' + str(start_date_sec))
        route_id_key = trip_key['routeId']
        logging.debug('\nroute_id_key = ' + str(route_id_key))
        logging.debug('\ntype(route_id_key) = ' + str(type(route_id_key)))
        schedule_train_object_list.append(ScheduleTrain(id_key=id_key,
                                           vehicle_key=vehicle_key,
                                           trip_key=trip_key,
                                           trip_id_key=trip_id_key,
                                           location_bound=location_bound,
                                           start_time_key=start_time_key,
                                           start_date_key=start_date_key,
                                           start_date_day=start_date_day,
                                           start_date_month=start_date_month,
                                           start_date_year=start_date_year,
                                           start_date_hour=start_date_hour,
                                           start_date_min=start_date_min,
                                           start_date_sec=start_date_sec,
                                           start_date_meridiem=start_date_meridiem,
                                           start_date_timezone=start_date_timezone,
                                           route_id_key=route_id_key,
                                           current_stop_sequence_key=None,
                                           current_stop_location=None,
                                           timestamp_key=None,
                                           cur_month=None,
                                           cur_day=None,
                                           cur_year=None,
                                           cur_hour=None,
                                           cur_min=None,
                                           cur_sec=None,
                                           cur_meridiem=None,
                                           cur_timezone=None,
                                           vehicle_stop_id_key=None))
        if 'currentStopSequence' in vehicle_key:
            # Set a default current_stop_location in case the data feed screws up for some weird reason to an N/A value:
            current_stop_location = 'N/A'
            current_stop_sequence_key = vehicle_key['currentStopSequence']
            logging.debug('\ncurrent_stop_sequence_key = ' + str(current_stop_sequence_key))
            logging.debug('\ntype(current_stop_sequence_key) = ' + str(type(current_stop_sequence_key)))
            TrainStopsFile = open('/projects_private/PythonProjects/ExpressOrLocalApp/7TrainStops.txt', 'r')
            logging.debug('current_stop_sequence_key = ' + str(current_stop_sequence_key))
            if current_stop_sequence_key > 0 and current_stop_sequence_key < 10:
                converted_stop_sequence = str('0' + str(current_stop_sequence_key))
            # Because stops begin with '701', '719' etc, we have to conform to the format:
            converted_stop_sequence = str('7' + str(current_stop_sequence_key))
            logging.debug('converted_stop_sequence = ' + str(converted_stop_sequence))
            for line in TrainStopsFile:
                logging.debug(line)
                split_line = line.strip().split(',')
                stop_name = split_line[0]
                filtered_stop_name = stop_name[0:3]
                stop_location = split_line[2]
                logging.debug('stop_name = ' + str(split_line[0]))
                logging.debug('filtered_stop_name = ' + str(filtered_stop_name))
                logging.debug('stop_location = ' + str(stop_location))
                if converted_stop_sequence == str(filtered_stop_name):
                    current_stop_location = stop_location
                    logging.debug('current_stop_location found!')
                    logging.debug('current_stop_location = ' + str(current_stop_location))
            TrainStopsFile.close()
            schedule_train_object_list.append(ScheduleTrain(id_key=id_key,
                                           vehicle_key=None,
                                           trip_key=None,
                                           trip_id_key=None,
                                           location_bound=None,
                                           start_time_key=None,
                                           start_date_key=None,
                                           start_date_day=None,
                                           start_date_month=None,
                                           start_date_year=None,
                                           start_date_hour=None,
                                           start_date_min=None,
                                           start_date_sec=None,
                                           start_date_meridiem=None,
                                           start_date_timezone=None,                 
                                           route_id_key=None,
                                           current_stop_sequence_key=current_stop_sequence_key,
                                           current_stop_location=current_stop_location,
                                           timestamp_key=None,
                                           cur_month=None,
                                           cur_day=None,
                                           cur_year=None,
                                           cur_hour=None,
                                           cur_min=None,
                                           cur_sec=None,
                                           cur_meridiem=None,
                                           cur_timezone=None,
                                           vehicle_stop_id_key=None))
        if 'timestamp' in vehicle_key:
            timestamp_key = vehicle_key['timestamp']
            logging.debug('\ntimestamp_key = ' + str(timestamp_key))
            logging.debug('\ntype(timestamp_key = ' + str(type(timestamp_key)))
            pendulum_current_timestamp = pendulum.from_timestamp(int(timestamp_key)).in_timezone('America/New_York')
            cur_month = pendulum_current_timestamp.month
            cur_day = int(pendulum_current_timestamp.strftime('%d'))
            cur_year = int(pendulum_current_timestamp.strftime('%Y'))
            cur_hour = int(pendulum_current_timestamp.strftime('%I'))
            # cur_min = int(pendulum_current_timestamp.strftime('%M'))
            cur_min = pendulum_current_timestamp.format('mm')
            cur_sec = pendulum_current_timestamp.format('ss')
            cur_meridiem = pendulum_current_timestamp.strftime('%p')
            cur_timezone = pendulum_current_timestamp.strftime('%Z')
            logging.debug('\ncur_month = ' + str(cur_month))
            logging.debug('\ntype(cur_month) = ' + str(type(cur_month)))
            logging.debug('\ncur_day = ' + str(cur_day))
            logging.debug('\ntype(cur_day) = ' + str(type(cur_day)))
            logging.debug('\ncur_year = ' + str(cur_year))
            logging.debug('\ntype(cur_year) = ' + str(type(cur_year)))
            logging.debug('\ncur_hour = ' + str(cur_hour))
            logging.debug('\ntype(cur_hour) = ' + str(type(cur_hour)))
            logging.debug('\ncur_min = ' + str(cur_min))
            logging.debug('\ntype(cur_min) = ' + str(type(cur_min)))
            logging.debug('\ncur_sec = ' + str(cur_sec))
            logging.debug('\ntype(cur_sec) = ' + str(type(cur_sec)))
            logging.debug('\ncur_meridiem = ' + str(cur_meridiem))
            logging.debug('\ntype(cur_meridiem) = ' + str(type(cur_meridiem)))
            logging.debug('\ncur_timezone) = ' + str(cur_timezone))
            logging.debug('\ntype(cur_timezone) = ' + str(type(cur_timezone)))
            schedule_train_object_list.append(ScheduleTrain(id_key=id_key,
                                           vehicle_key=None,
                                           trip_key=None,
                                           trip_id_key=None,
                                           location_bound=None,
                                           start_time_key=None,
                                           start_date_key=None,
                                           start_date_day=None,
                                           start_date_month=None,
                                           start_date_year=None,
                                           start_date_hour=None,
                                           start_date_min=None,
                                           start_date_sec=None,
                                           start_date_meridiem=None,
                                           start_date_timezone=None,                 
                                           route_id_key=None,
                                           current_stop_sequence_key=None,
                                           current_stop_location=None,
                                           timestamp_key=timestamp_key,
                                           cur_month=cur_month,
                                           cur_day=cur_day,
                                           cur_year=cur_year,
                                           cur_hour=cur_hour,
                                           cur_min=cur_min,
                                           cur_sec=cur_sec,
                                           cur_meridiem=cur_meridiem,
                                           cur_timezone=cur_timezone,
                                           vehicle_stop_id_key=None))
        vehicle_stop_id_key = vehicle_key['stopId']
        logging.debug('\nvehicle_stop_id_key = ' + str(vehicle_stop_id_key))
        logging.debug('\ntype(vehicle_stop_id_key) = ' + str(type(vehicle_stop_id_key)))
        schedule_train_object_list.append(ScheduleTrain(id_key=id_key,
                                           vehicle_key=None,
                                           trip_key=None,
                                           trip_id_key=None,
                                           location_bound=None,
                                           start_time_key=None,
                                           start_date_key=None,
                                           start_date_day=None,
                                           start_date_month=None,
                                           start_date_year=None,
                                           start_date_hour=None,
                                           start_date_min=None,
                                           start_date_sec=None,
                                           start_date_meridiem=None,
                                           start_date_timezone=None,                 
                                           route_id_key=None,
                                           current_stop_sequence_key=None,
                                           current_stop_location=None,
                                           timestamp_key=None,
                                           cur_month=None,
                                           cur_day=None,
                                           cur_year=None,
                                           cur_hour=None,
                                           cur_min=None,
                                           cur_sec=None,
                                           cur_meridiem=None,
                                           cur_timezone=None,
                                           vehicle_stop_id_key=vehicle_stop_id_key))
    return live_train_object_list, schedule_train_object_list


def tabulate_data(live_train_object_list, schedule_train_object_list):
    # Create content variable for Flask:
    # NOTE: I removed the print statements so that everything can be added to a overall content variable
    # that is responsible for printing out everything

    content = '<link rel="stylesheet" href="css/output.css" type="text/css"/>'
    
    content += '<h1 id="program_header">Express Or Local App</h1>'

    content += '\n'

    current_date_eastern = pendulum.now('America/New_York').format('dddd, MMMM D, YYYY')

    current_time_eastern = pendulum.now('America/New_York').format('hh:mm:ss A')

    content += '<h2 id="updated_header">Last Time Updated: ' + str(current_date_eastern) + ' at ' + str(current_time_eastern) + ' EST</h2>'

    content += '\n'

    content += '<h2 class="description_headers">Live Routes</h2>'

    content += '\n'

    live_route_trip_headers=['TrainID', 'Location Bound', 'RouteID', 'Start Date', 'Start Time']
    
    content += tabulate([[o.id_key, o.location_bound, o.route_id_key, str(str(o.start_date_month) + '-' + str(o.start_date_day) + '-' + str( o.start_date_year)), str(str(o.start_date_hour) + ':' + str(o.start_date_min) + ':' + str(o.start_date_sec) + ' ' + str(o.start_date_meridiem) + ' ' +  str(o.start_date_timezone))] for o in live_train_object_list if o.start_date_month is not None], headers=live_route_trip_headers, tablefmt="html", numalign="center", stralign="center")

    content += '\n'

    content += '<h2 class="description_headers">Arrivals</h2>'

    content += '\n'
    
    live_arrival_headers=['Train ID', 'Location Bound', 'Stop Location', 'Arrival Date', 'Arrival Time']
    
    content += tabulate([[o.id_key, o.arr_dep_location_bound, o.arr_dep_stop_location, str(str(o.arr_month) + '-' + str(o.arr_day) + '-' + str( o.arr_year)), str(str(o.arr_hour) + ':' + str(o.arr_min) + ':' + str(o.arr_sec) + ' ' + str(o.arr_meridiem) + ' ' +  str(o.arr_timezone)) ] for o in live_train_object_list if o.arr_month is not None], headers=live_arrival_headers, tablefmt="html", numalign="center", stralign="center")

    content += '\n'

    content += '<h2 class="description_headers">Departures</h2>'

    content += '\n'
    
    live_departure_headers=['Train ID', 'Location Bound', 'Stop Location', 'Departure Date', 'Departure Time']
    
    content += tabulate([[o.id_key, o.arr_dep_location_bound, o.arr_dep_stop_location, str(str(o.dep_month) + '-' + str(o.dep_day) + '-' + str(o.dep_year)), str(str(o.dep_hour) + ':' + str(o.dep_min) + ':' + str(o.dep_sec) + ' ' + str(o.dep_meridiem) + ' ' +  str(o.dep_timezone)) ] for o in live_train_object_list if o.dep_month is not None], headers=live_departure_headers, tablefmt="html", numalign="center", stralign="center")

    content += '\n'

    content += '<h2 class="description_headers">Future Routes</h2>'

    content += '\n'

    schedule_route_trip_headers=['TrainID', 'Location Bound', 'RouteID', 'Start Date', 'Start Time']

    content += tabulate([[o.id_key, o.location_bound, o.route_id_key, str(str(o.start_date_month) + '-' + str(o.start_date_day) + '-' + str(o.start_date_year)), str(str(o.start_date_hour) + ':' + str(o.start_date_min) + ':' + str(o.start_date_sec) + ' ' + str(o.start_date_meridiem) + ' ' +  str(o.start_date_timezone))] for o in schedule_train_object_list if o.start_date_day is not None], headers=schedule_route_trip_headers, tablefmt="html", numalign="center", stralign="center")

    content += '\n'

    content += '<h2 class="description_headers">Future Stops</h2>'

    content += '\n'
    
    schedule_stop_sequence_headers=['Train ID', 'Stop Sequence', 'Stop Location']
    
    content += tabulate([[o.id_key, o.current_stop_sequence_key, o.current_stop_location] for o in schedule_train_object_list if o.current_stop_location], headers=schedule_stop_sequence_headers, tablefmt="html", numalign="center", stralign="center")

    content += '\n'

    print(content)

    # Write content variable to a file

    with open('/var/www/musimatic/pythonprojectwebsites/ExpressOrLocalApp/output.html', 'w') as f:
        f.write(content)

    f.close()
                
    return content

    
def main():
    MTADataFeed = 'https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-7'
    
    r = get_request(MTADataFeed)

    print('r: \n\n' + str(r))

    feed = create_feed(r)

    print('feed: \n\n' + str(feed))

    dict_feed = convert_to_dict_feed(r, feed)

    print('dict_feed: \n\n' + str(dict_feed))

    # Uncomment for debugging purposes:
    # pprint_dict_feed(dict_feed)

    live_train_data, scheduled_train_data = createTrainLists(dict_feed)

    live_train_object_list, schedule_train_object_list = create_object_lists(live_train_data, scheduled_train_data)

    content = tabulate_data(live_train_object_list, schedule_train_object_list)

    return content


if __name__ == '__main__':
    main()
