import numpy as np
from gnuradio import gr
import time
#Mycar: K1 370 unassembled: 360600
#Mycar: K2 370 assembled: 351236
#Hrmana mrcdez car: K3 370: 562168
#Concesionaria K1 433: 761661

class bruteforceblock(gr.sync_block):
    def __init__(self,number_start,number_finish,dictionary,time):
        gr.sync_block.__init__(self,
            name="custom_source_20bit",
            in_sig=None,
            out_sig=[np.complex64])
        self.current_combination = number_start  # Start at the desired range, works with 360590...no less
        self.max_combinations = number_finish
        self.complete = False
        self.call_count = 0  # Contador de llamadas a work
        self.nbits = dictionary["n"]
        self.dictionary = dictionary["encoding"]
        self.time = time
    

    def work(self, input_items, output_items):
        if self.complete:
            return 0
        out = output_items[0]
        nbin = '0'+str(self.nbits)+'b'
        bits_pre = list(map(int, format(self.current_combination, nbin)))#20 bits
        
        #20 bits codification
        print(f"Trying decimal code------------------------------------------->: {self.current_combination}")
        self.current_combination += 1  # Increment the combination counter
        print(bits_pre)
        encoded_result = []

        encoding = {key: self.dictionary[key] for key in list(self.dictionary)[:2]}
        preamble = {key: self.dictionary[key] for key in list(self.dictionary)[2:]}

        for bit in bits_pre:
            encoded_result.extend([int(char) for char in encoding[bit]])
        
        #Preambule&mode codification
        preamble = preamble['preamble']
        mode = [0,0,1,0]  # unlock'
        mode_result = []
        for bit in mode:
            mode_result.extend([int(char) for char in encoding[bit]])

        
        bits = [int(char) for char in preamble] + encoded_result + mode_result
        bits = bits*2
        #signal = np.array([complex(bit) for bit in bits], dtype=np.complex64)
        signal = [complex(bit) for bit in bits]
        
        # Ensure output buffer length matches the signal length
        noutput_items = min(len(out), len(signal))
        out[:noutput_items] = signal[:noutput_items]

        if self.current_combination > self.max_combinations:
            self.complete = True
            print("Task completed, exiting...")
            exit()
        

        time.sleep(self.time/1000)#Transform from miliseconds to seconds
        return noutput_items

    def stop(self):
        # Puede ser necesario implementar acciones de limpieza si las hay
        exit()
