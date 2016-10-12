#!/usr/bin/env python

import csv
import restaurant_functions

restaurants = {}

finished = False

def search_on_distance(dist):
    for restaurant_name in restaurants.keys():
        rest_details = restaurants[restaurant_name]
        if int(rest_details["dist"]) <= int(dist):
            print restaurant_name + " is a " + rest_details["type"] + " place " + \
             rest_details["dist"] + " minutes from here"
      

def search_on_rating(rating):
    for restaurant_name in restaurants.keys():
        rest_details = restaurants[restaurant_name]
        if int(rest_details["fave"]) >= int(rating):
            print restaurant_name + " is a " + rest_details["fave"] + "/5 rated place " + \
              str(rest_details["dist"]) + " minutes from here"


def add_restaurant():
    name = raw_input("Enter Restaurant Name: ")
    cuisine = raw_input("Enter Restaurant type: ")
    cost = raw_input("Enter Restaurant cost (out of 5): ")
    fave = raw_input("Enter cost (out of 5): ")
    dist = raw_input("Enter distance (minutes' walk): ")
    restaurants[name] = {"name": name, "type": cuisine, "cost": cost, "fave": fave, "dist": dist}


def save_changes():
    with open("restaurants-lesson8.csv","w") as csvfile:
        csv_writer = csv.DictWriter(csvfile, fieldnames=['name', 'type', 'cost', 'fave', 'dist'])
        csv_writer.writeheader()
        for restaurant_name in restaurants.keys():
            rest_details = restaurants[restaurant_name]
            rest_details['name'] = restaurant_name
            csv_writer.writerow(rest_details) 


def read_csvfile():
    with open("restaurants-lesson8.csv") as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for rest_details in csv_reader: 
            restaurant_name = rest_details['name']
            del rest_details['name']
            restaurants[restaurant_name] = rest_details

read_csvfile()

while not finished:
    restaurant_functions.show_menu()
    choice = raw_input("Please enter choice: ")
    if choice == "1":
        search_on_distance(raw_input("Please enter max distance: "))
    elif choice == "2":
        search_on_rating(raw_input("Please enter minimum rating: "))
    elif choice == "3":
        add_restaurant()
    elif choice == "4":
        save_changes()
    elif choice == "5":
        finished = True
    else:
        print "That's not a valid choice - try again!"