import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np
from datetime import datetime

def create_hum_plot() -> plt:
    df = pd.read_csv("csv/data.csv")
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df["hours"] = df["timestamp"].dt.hour
    name_count = pd.value_counts(df["hours"])
    get_x = dict(name_count).keys()
    y = df["humidity"]
    x = [*get_x]
    plt.plot(x,y)
    plt.title(f"Humitdity_graph {__get_current_date()}")
    plt.ylabel("Humidity in %")
    plt.xlabel("Hours")
    plt.savefig(f"static/plots/{__get_current_date()}humidity_plot.png")
    return plt

def create_temp_plot() -> plt:
    df = pd.read_csv("csv/data.csv")
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df["hours"] = df["timestamp"].dt.hour
    name_count = pd.value_counts(df["hours"])
    get_x = dict(name_count).keys()
    y = df["temperature"]
    x = [*get_x]
    plt.plot(x,y)
    plt.title(f"Temperaure_graph {__get_current_date()}")
    plt.ylabel("Temperature in %")
    plt.xlabel("Hours")
    plt.savefig(f"static/plots/{__get_current_date()}temperature_plot.png") # TODO add cureent datetime to plt name
    return plt

def __get_current_date() -> datetime:
    return datetime.utcnow().strftime("%Y-%m-%d")