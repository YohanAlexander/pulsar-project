#! /usr/bin/python
# -*- coding: utf-8 -*-

# Generic/Built-in
import time
import csv

# Other Libs
import serial
import pandas as pd
import streamlit as st
import plotly.graph_objs as go


def main():
    """
    Python script to obtain and plot data from the simulated pulsar on a interactive interface.
    """

    st.title(" >  >  > Simulated Pulsar LightCurve")

    check = st.checkbox('Capture from serial device ?')

    if check:

        porta = st.text_input(" >  >  > Port of the serial device:")

        if porta is not None:

            try:

                with st.spinner("### >  >  > Conecting..."):
                    arduino = serial.Serial(
                        port=porta, baudrate=115200, timeout=1)

                if arduino.isOpen():
                    st.success("### >  >  > Device connected !")

            except:
                st.error("### >  >  > Conection failed")

            expo = st.slider(" >  >  > How long to capture data ?", 100, 1000)

            expo *= 10

            start = st.checkbox(' > > > Start to capture data !')

            if start:

                tzero = int(round(time.time() * 1000))

                try:

                    with st.spinner("### >  >  > Capturing data..."):

                        with open(f'data.csv', mode='w', newline='') as tabela:

                            for i in range(expo):
                                linha = arduino.readline().decode('utf-8').strip('\r\n')
                                tempo = int(round(time.time() * 1000)) - tzero
                                arquivo = csv.writer(tabela, delimiter=",")
                                arquivo.writerow([tempo, linha])

                            st.success(" ### >  >  > Data Captured")

                except:
                    st.warning("### >  >  >  Conection Interrupted !")

            display = st.checkbox(' > > >  Plot the data !')

            if display:

                try:

                    df = pd.read_csv(f'data.csv', delimiter=',')
                    df.columns = ['Time', 'Lux']

                    table = st.checkbox(' >  >  > Show dataset !')

                    if table:
                        st.dataframe(df)

                    plot = st.slider(" >  >  > Slice of the data to plot: ", 100, 1000)

                    plot *= 10

                    st.write("### >  >  > Plot of the lightcurve\n")

                    graph = go.Scatter(x=df['Time'][:plot], y=df['Lux'][:plot], marker={
                                       'color': 'crimson'})
                    layout = go.Layout(yaxis={'title': 'Lux'}, xaxis={
                                       'title': 'Time (ms)'})
                    fig = go.Figure(data=[graph], layout=layout)
                    st.plotly_chart(fig)

                except:
                    st.error('### > > > Error reading the dataset')

    else:

        data = st.text_input(" >  >  > Name of the dataset: ")

        try:

            if data is not None:
                df = pd.read_csv(f'{data}.csv', delimiter=',')
                df.columns = ['Time', 'Lux']

                table = st.checkbox(' >  >  > Show dataset !')
                if table:
                    st.dataframe(df)

                plot = st.slider(" >  >  > Slice of the data to plot: ", 100, 1000)

                st.write("### >  >  > Plot of the lightcurve")

                graph = go.Scatter(x=df['Time'][:plot], y=df['Lux'][:plot], marker={
                                   'color': 'crimson'})
                layout = go.Layout(yaxis={'title': 'Lux'}, xaxis={
                                   'title': 'Time (ms)'})
                fig = go.Figure(data=[graph], layout=layout)
                st.plotly_chart(fig)

        except:
            st.error(" ### >  >  > Invalid name !")


if __name__ == "__main__":
    main()
