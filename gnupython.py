#!/usr/bin/env python3

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio import analog
from gnuradio import blocks
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
from PyQt5 import Qt
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
import osmosdr
import time
import sip
import re
from termcolor import colored

# Import the custom block
from bruteforceblock import bruteforceblock

class generatesignalunlock1(gr.top_block, Qt.QWidget):

    def __init__(self,number_start,number_finish,freq,dictionary,time):
        gr.top_block.__init__(self, "Brute Force 20-bit Code", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Brute Force 20-bit Code")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except BaseException as exc:
            print(f"Qt GUI: Could not set Icon: {str(exc)}", file=sys.stderr)
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "generatesignalunlock1")

        try:
            geometry = self.settings.value("geometry")
            if geometry:
                self.restoreGeometry(geometry)
        except BaseException as exc:
            print(f"Qt GUI: Could not restore geometry: {str(exc)}", file=sys.stderr)

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 2e6

        ##################################################
        # Blocks
        ##################################################

        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
            1024, #size
            samp_rate, #samp_rate
            "", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0.enable_stem_plot(False)


        labels = ['Signal 1']
        widths = [1]
        colors = ['blue']
        alphas = [1.0]
        styles = [1]
        markers = [-1]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_win)
        self.osmosdr_sink_0 = osmosdr.sink(
            args="numchan=" + str(1) + " " + ""
        )
        self.osmosdr_sink_0.set_time_unknown_pps(osmosdr.time_spec_t())
        self.osmosdr_sink_0.set_sample_rate(samp_rate)
        self.osmosdr_sink_0.set_center_freq(freq, 0)#here is 370e6,0
        self.osmosdr_sink_0.set_freq_corr(0, 0)
        self.osmosdr_sink_0.set_gain(24, 0)
        self.osmosdr_sink_0.set_if_gain(24, 0)
        self.osmosdr_sink_0.set_bb_gain(24, 0)
        self.osmosdr_sink_0.set_antenna('', 0)
        self.osmosdr_sink_0.set_bandwidth(0, 0)
        # Replace vector source with custom source block
        self.custom_source = bruteforceblock(number_start,number_finish,dictionary,time)
        self.blocks_throttle2_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate, True, 0 if "auto" == "auto" else max( int(float(0.1) * samp_rate) if "auto" == "time" else int(0.1), 1) )
        self.blocks_repeat_0 = blocks.repeat(gr.sizeof_gr_complex*1, 600)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_complex_to_mag_squared_0 = blocks.complex_to_mag_squared(1)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_SIN_WAVE, freq, 4, 0, 0) #freq=370000000

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.blocks_complex_to_mag_squared_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_throttle2_0, 0))
        self.connect((self.blocks_repeat_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.blocks_throttle2_0, 0), (self.blocks_complex_to_mag_squared_0, 0))
        self.connect((self.blocks_throttle2_0, 0), (self.osmosdr_sink_0, 0))
        self.connect((self.custom_source, 0), (self.blocks_repeat_0, 0))
        

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "generatesignalunlock1")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.blocks_throttle2_0.set_sample_rate(self.samp_rate)
        self.osmosdr_sink_0.set_sample_rate(self.samp_rate)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)

    def brute_force_check(self):
        if not self.brute_force_complete:
            if self.custom_source.current_combination >= self.max_combinations:
                print("Brute force complete, exiting principal desde programa principal")
                self.brute_force_complete = True
                self.stop()

    def stop(self):
        # Método para detener el flujo de datos del bloque bruteforceblock
        self.custom_source.stop()

#Finished Class

#Start Main Method
def chip2bits(chip):
    chip = ''.join(re.findall(r'\d+', chip))
    dictionary = {}
    if chip in ["2240", "1527", "1528", "2241", "1530", "2280"]:
        print("-> The chip is a learning code chip") 
        n = 20
        encoding = {1: "1110", 0: "1000", "preamble": '10000000000000000000000000000000'}
        dictionary = {"n": n, "encoding": encoding,"t":2}
    if chip in ["2264", "2272", "2294"]:
        print("-> The chip is a fixed code chip")
        n = 12
        encoding = {1: "11101110", 0: "10001000", "f":"10001110","preamble": '10000000000000000000000000000000'}
        dictionary = {"n": n, "encoding": encoding,"t":3}
    if chip in ["2260"]:
        print("->The chip is a fixed code chip")
        n = 10
        encoding = {1: "11101110", 0: "10001000", "f":"10001110","preamble": '10000000000000000000000000000000'}
        dictionary = {"n": n, "encoding": encoding,"t":2}
    return dictionary

def main(top_block_cls=generatesignalunlock1, options=None):
    chip = input("--> Enter the learning/fixed code chip name (e.g., HS2241): ")
    print("--[INFORMATION]:")
    print(f"-> Chip entered: {chip}")
    dictionary = chip2bits(chip)
    total = int(dictionary["t"])**int(dictionary["n"])
    print(f"-> The chip {chip} has "+str(dictionary["n"])+" bits of code, therefore there are "+str(total)+" possibles codes")
    number_start = int(input(f"--> Enter the number to start brute force, between {0}-{total}: "))
    number_finish = int(input(f"--> Enter the number to finish brute force, between {0}-{total}: "))
    freq = int(input("--> Enter the frequency Tx in MHz (e.g., 315/370/433): ")+"000000")
    time = int(input("--> Enter the time between each code in miliseconds (e.g., 60/50/30): "))

    qapp = Qt.QApplication(sys.argv)
    tb = top_block_cls(number_start,number_finish,freq,dictionary,time)

    tb.start()
    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()
        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    qapp.exec_()

if __name__ == '__main__':
    main()
