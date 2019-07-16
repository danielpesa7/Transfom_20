#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def read_file(route):
    '''This function reads the spreadsheet into a pandas dataframe'''
    sheet = pd.read_excel(route, sheet_name = 'Daniel')
    sheet = sheet.dropna()
    return sheet

def plot_subplots(sheet_name,columns_list):
    '''This function plots every exercise into a different barplot in separated subplots'''
    plt.figure(figsize = (20,10))
    for i in range(len(columns_list)):
        plt.subplot(6,4,i+1)
        sns.barplot(data = sheet_name, x = 'WEEK', y = columns_list[i])
        plt.subplots_adjust(hspace = 1, wspace = 1)
        plt.tight_layout()
    plt.title('Exercise Progress')
    plt.savefig('output_files/Exercises Progress')

def plot_mean(mean_values):
    '''This function plot a barplot with the mean of every exercise'''
    plt.figure(figsize = (20,10))
    sns.barplot(data = mean_values, x = mean_values.index, y = 'mean')
    plt.xticks(rotation = 45)
    plt.ylabel('Quantity')
    plt.title('Exercises Mean')
    plt.savefig('output_files/Exercises Mean')

sheet = read_file('excel_files/Transform_20.xlsx')
columns_list = sheet.columns[1:]
describe_table = sheet.describe().round(1)
mean_values = pd.DataFrame(describe_table.loc['mean'])
mean_values.sort_values(by = 'mean', inplace = True, ascending = False)
plot_subplots(sheet,columns_list)
plot_mean(mean_values)          