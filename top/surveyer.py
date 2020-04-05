#!/usr/bin/python
import os.path as path
import xml.etree.ElementTree as ET

read_path = "./config/survey.xml"
write_path = "./reports/report"

def try_file_open(filePath, exec):
    try:
        file = open(filePath,exec)
        print("File: \'" + filePath + "\' successfully opened.")
        return file
    except:
        print("File: \'" + filePath + "\' failed to open.")
        return 0

def try_file_close(filePath):
    try:
        filePath.close()
        print("File: \'" + filePath.name + "\' successfully closed.")
        return 1
    except:
        print("File: \'" + filePath.name + "\' failed to close.")
        return 0

def latest_file_name(filePath):
    count = 0
    available = False
    while not(available):
        count = count + 1
        newPath = filePath + str(count)
        print("Checking availabilty for path: "+ newPath)
        if not(path.exists(newPath)):
            available = True
    return count

def open_read_file(filePath):
    return try_file_open(filePath,"rt")

def open_write_file(filePath):
    return try_file_open(filePath,"wt")

def close_read_file(filePath):
    try_file_close(filePath)

def close_write_file(filePath):
    try_file_close(filePath)

def get_survey_quesions(survey_path):
    root = ET.parse(survey_path)
    list = root.findall("question")
    return list

def get_question_options(survey_question):
    options = list(survey_question.iter("option"))
    return options

def survey():
    global read_path
    global write_path

    #survey = open_read_file(read_path)
    survey = get_survey_quesions(read_path)
    report = open_write_file(write_path + str(latest_file_name(write_path)))

    for question in survey:
        print("\t" + question.get('name'))
        optionCount = 0
        for option in get_question_options(question):
            optionCount = optionCount + 1
            print("\t\t" +str(optionCount)+ ") "+ option.text)
        valid = False
        while not(valid):
            try:
                select = int(input("Select a number option: "))
                if select > 0 and select <= optionCount:
                    report.write(get_question_options(question)[select-1].text + "\n")
                    valid = True
                else:
                    print("Not an option")
            except ValueError:
                print("Please use a number")

    close_write_file(report)

survey()
