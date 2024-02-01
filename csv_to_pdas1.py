"""
this file was created to plot matlab, .csv, python results for wssci spring technical meeting '24.
by michelle gee
"""

import os
import pandas as pd
import matplotlib.pyplot as plt

#simulated sugar data, algal and biomass tga

# input folder path containing the CSV files
folder_path = '/Users/michellegee/Desktop/skool/grad/CIRE:NRG/data f elliott/tga/tga2_csv'

# get list of CSV files in the folder
csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]

# initialize figure
plt.figure(figsize=(10, 6))

# iterate through each CSV file
for csv_file in csv_files:
    df = pd.read_csv(os.path.join(folder_path, csv_file))  # read the CSV file into a dataframe
    label_name = os.path.splitext(csv_file)[0].replace('_', ' ')  # format legend entries
    if 'sim' in df.columns:
        plt.plot(df['Temperature [K]'], df['sim'], label=label_name, color='tab:purple')
    if 'TGA [wt %] bio, df' in df.columns:
        plt.plot(df['Temperature [K]'], df['TGA [wt %] bio, df'], label=label_name, marker='.', markevery=10)
    if 'TGA [wt %] bio' in df.columns:
        plt.plot(df['Temperature [K]'], df['TGA [wt %] bio'], label=label_name, marker='.')  # plot data from the dataframe
    if 'TGA [wt %] alg' in df.columns:
        plt.plot(df['Temperature [K]'], df['TGA [wt %] alg'], label=label_name, marker='x')
      #, marker='o')  #label='mark',

# format
plt.xlabel('Temperature [K]')
plt.ylabel('TGA [wt %]')
plt.title('Algal, Biomass, and Lumped Sugar TGA data')
plt.legend()
#plt.show()

#---------------------------------------------------------------------------------------------------------------------#
# next
# experimental and simulated sugar data

# input folder path containing the CSV files
folder_path_2 = '/Users/michellegee/Desktop/skool/grad/CIRE:NRG/data f elliott/tga'

# get list of CSV files in the folder
csv_files = [f for f in os.listdir(folder_path_2) if f.endswith('.csv')]

# initialize figure
plt.figure(figsize=(10, 6))

# iterate through each CSV file
for csv_file in csv_files:
    df = pd.read_csv(os.path.join(folder_path_2, csv_file))  # read the CSV file into a dataframe
    label_name = os.path.splitext(csv_file)[0]  #.replace('_', ' ')  # format legend entries
    if 'TGA [wt %]' in df.columns:
        plt.plot(df['Temperature [K]'], df['TGA [wt %]'], color='tab:purple', label=label_name)
    if 'mass %' in df.columns:
        plt.plot(df['T [K]'], df['mass %'], label=label_name, linestyle='--')  # plot data from the dataframe


# format
plt.xlabel('Temperature [K]')
plt.ylabel('TGA [wt %]')
plt.title('Experimental and Simulated Sugar TGA Data')
plt.legend()
#plt.show()

#---------------------------------------------------------------------------------------------------------------------#
# next
#overlaid simulated TGA data only

# input folder path containing the CSV files
folder_path_3 = '/Users/michellegee/Desktop/skool/grad/CIRE:NRG/data f elliott/tga/sugar_csv'

# get list of CSV files in the folder
csv_files = [f for f in os.listdir(folder_path_3) if f.endswith('.csv')]

# initialize figure
plt.figure(figsize=(10, 6))

# iterate through each CSV file
for csv_file in csv_files:
    df = pd.read_csv(os.path.join(folder_path_3, csv_file))  # read the CSV file into a dataframe
    label_name = os.path.splitext(csv_file)[0]  #.replace('_', ' ')  # format legend entries
    if 'TGA [wt %], creck' in df.columns:
        plt.plot(df['Temperature [K]'], df['TGA [wt %], creck'], label=label_name, linestyle='--')
    if 'TGA [wt %]' in df.columns:
        plt.plot(df['Temperature [K]'], df['TGA [wt %]'], label=label_name, color='tab:purple')  # plot data from the dataframe


# format
plt.xlabel('Temperature [K]')
plt.ylabel('TGA [wt %]')
plt.title('Overlaid Simulated TGA Sugar Data')
plt.legend()
#plt.show()

#---------------------------------------------------------------------------------------------------------------------#
# next
# DTG plots

# input folder path containing the CSV files
folder_path_3 = '/Users/michellegee/Desktop/skool/grad/CIRE:NRG/data f elliott/tga/dtg'

# get list of CSV files in the folder
csv_files = [f for f in os.listdir(folder_path_3) if f.endswith('.csv')]

# initialize figure
plt.figure(figsize=(10, 6))

# iterate through each CSV file
for csv_file in csv_files:
    df = pd.read_csv(os.path.join(folder_path_3, csv_file))  # read the CSV file into a dataframe
    label_name = os.path.splitext(csv_file)[0]  #.replace('_', ' ')  # format legend entries
    if 'negative DTG' in df.columns:
        plt.plot(df['T [K]'], df['negative DTG'], label=label_name, linestyle='--')
    if 'neg DTG' in df.columns:
        plt.plot(df['T [K]'], df['neg DTG'], label=label_name, color='tab:purple')  # plot data from the dataframe

# format
plt.xlabel('Temperature [K]')
plt.ylabel('DTG/[%/min]')
plt.title('Experimental and Simulated Sugar DTG')
plt.legend()
plt.show()