"""Thsi is file creation"""
import json
file = open("example.txt","w")

file.write("Hello, this is my first file operation!")
file.close()
print("file created")

""" This is for file reading which alredy exists"""

file = open("example.txt","r")
content = file.read()
print("file content : "+ content)

""" This is for file appending or adding  which alredy exists"""
file = open("example.txt","a")
file.write("\nThis is appended line")


data = {"name":"siva"}
file = open("file.json","w")
json.dump(data,file)